#!/usr/bin/env python3
"""
Linear Regression Analysis Tool
================================

A comprehensive tool for generating synthetic data, performing linear regression
using vector operations, and calculating model performance metrics.

Author: Data Science Team
Version: 1.0.0
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Dict, Any
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LinearRegressionAnalyzer:
    """
    A class to perform linear regression analysis with synthetic data generation,
    vector-based calculations, and comprehensive visualization.
    """
    
    def __init__(self, sample_size: int = 10000, random_seed: int = None):
        """
        Initialize the Linear Regression Analyzer.
        
        Args:
            sample_size (int): Number of data points to generate
            random_seed (int): Random seed for reproducibility
        """
        self.sample_size = sample_size
        if random_seed is not None:
            np.random.seed(random_seed)
        
        self.points = None
        self.beta0 = None
        self.beta1 = None
        self.r_squared = None
        self.results = {}
        
        logger.info(f"LinearRegressionAnalyzer initialized with sample_size={sample_size}")
    
    def step1_generate_synthetic_data(self, true_slope: float = 0.6, true_intercept: float = 0.3, 
                                    noise_range: float = 0.3) -> np.ndarray:
        """
        Step 1: Generate synthetic 2D points with linear relationship and noise.
        
        Formula: y = true_slope * x + true_intercept + noise
        
        Args:
            true_slope (float): True slope of the underlying relationship
            true_intercept (float): True intercept of the underlying relationship
            noise_range (float): Range of random noise to add (±noise_range)
        
        Returns:
            np.ndarray: Array of generated points with shape (n, 2)
        """
        logger.info("Step 1: Generating synthetic data...")
        
        # Generate x-coordinates randomly between 0 and 1
        x_coords = np.random.rand(self.sample_size)
        
        # Generate y-coordinates based on linear formula with noise
        random_noise = -noise_range + (2 * noise_range) * np.random.rand(self.sample_size)
        y_coords = true_slope * x_coords + true_intercept + random_noise
        
        # Combine into points array
        self.points = np.column_stack((x_coords, y_coords))
        
        logger.info(f"Generated {self.sample_size} synthetic data points")
        return self.points
    
    def step2_calculate_means(self) -> Tuple[float, float]:
        """
        Step 2: Calculate means of x and y coordinates.
        
        Returns:
            Tuple[float, float]: Mean of x-coordinates and mean of y-coordinates
        """
        logger.info("Step 2: Calculating means...")
        
        if self.points is None:
            raise ValueError("Data not generated. Call step1_generate_synthetic_data() first.")
        
        mean_x = np.mean(self.points[:, 0])
        mean_y = np.mean(self.points[:, 1])
        
        self.results['mean_x'] = mean_x
        self.results['mean_y'] = mean_y
        
        logger.info(f"Mean X: {mean_x:.6f}, Mean Y: {mean_y:.6f}")
        return mean_x, mean_y
    
    def step3_calculate_deviations(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Step 3: Calculate deviations from means for both coordinates.
        
        Returns:
            Tuple[np.ndarray, np.ndarray]: X deviations and Y deviations
        """
        logger.info("Step 3: Calculating deviations from means...")
        
        mean_x, mean_y = self.results['mean_x'], self.results['mean_y']
        
        x_deviations = self.points[:, 0] - mean_x
        y_deviations = self.points[:, 1] - mean_y
        
        logger.info("Deviations calculated successfully")
        return x_deviations, y_deviations
    
    def step4_calculate_slope(self, x_deviations: np.ndarray, y_deviations: np.ndarray) -> float:
        """
        Step 4: Calculate slope using vector operations.
        
        Formula: beta1 = dot(x_deviations, y_deviations) / dot(x_deviations, x_deviations)
        
        Args:
            x_deviations (np.ndarray): Deviations of x from mean
            y_deviations (np.ndarray): Deviations of y from mean
        
        Returns:
            float: Calculated slope (beta1)
        """
        logger.info("Step 4: Calculating slope using vector operations...")
        
        numerator = np.dot(x_deviations, y_deviations)
        denominator = np.dot(x_deviations, x_deviations)
        
        self.beta1 = numerator / denominator
        self.results['beta1'] = self.beta1
        
        logger.info(f"Calculated slope (beta1): {self.beta1:.6f}")
        return self.beta1
    
    def step5_calculate_intercept(self) -> float:
        """
        Step 5: Calculate intercept using the formula.
        
        Formula: beta0 = mean_y - beta1 * mean_x
        
        Returns:
            float: Calculated intercept (beta0)
        """
        logger.info("Step 5: Calculating intercept...")
        
        mean_x, mean_y = self.results['mean_x'], self.results['mean_y']
        
        self.beta0 = mean_y - self.beta1 * mean_x
        self.results['beta0'] = self.beta0
        
        logger.info(f"Calculated intercept (beta0): {self.beta0:.6f}")
        return self.beta0
    
    def step6_calculate_r_squared(self) -> float:
        """
        Step 6: Calculate R-squared value to measure model performance.
        
        Formula: R² = 1 - (SSR / SST)
        where SSR = sum of squared residuals, SST = total sum of squares
        
        Returns:
            float: R-squared value
        """
        logger.info("Step 6: Calculating R-squared value...")
        
        # Calculate predicted y-values
        y_predicted = self.beta1 * self.points[:, 0] + self.beta0
        
        # Calculate total sum of squares (SST)
        mean_y = self.results['mean_y']
        sst = np.sum((self.points[:, 1] - mean_y)**2)
        
        # Calculate residual sum of squares (SSR)
        ssr = np.sum((self.points[:, 1] - y_predicted)**2)
        
        # Calculate R-squared
        self.r_squared = 1 - (ssr / sst)
        
        self.results.update({
            'y_predicted': y_predicted,
            'sst': sst,
            'ssr': ssr,
            'r_squared': self.r_squared
        })
        
        logger.info(f"R-squared value: {self.r_squared:.6f}")
        return self.r_squared
    
    def step7_visualize_results(self, figsize: Tuple[int, int] = (12, 5)) -> None:
        """
        Step 7: Create comprehensive visualization of results.
        
        Args:
            figsize (Tuple[int, int]): Figure size for the plots
        """
        logger.info("Step 7: Creating visualizations...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
        
        # Plot 1: Original data points
        ax1.scatter(self.points[:, 0], self.points[:, 1], s=5, alpha=0.6)
        ax1.set_title(f'Original Data Points\n({self.sample_size} Random Points)')
        ax1.set_xlabel('X-coordinate')
        ax1.set_ylabel('Y-coordinate')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Data points with regression line
        ax2.scatter(self.points[:, 0], self.points[:, 1], s=5, alpha=0.6, 
                   label='Data Points', color='blue')
        
        # Generate regression line
        x_line = np.array([0, 1])
        y_line = self.beta1 * x_line + self.beta0
        ax2.plot(x_line, y_line, color='red', linewidth=2, 
                label=f'Regression Line\ny = {self.beta1:.3f}x + {self.beta0:.3f}')
        
        ax2.set_title(f'Linear Regression Analysis\nR² = {self.r_squared:.4f}')
        ax2.set_xlabel('X-coordinate')
        ax2.set_ylabel('Y-coordinate')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
        
        logger.info("Visualizations created successfully")
    
    def step8_generate_report(self) -> Dict[str, Any]:
        """
        Step 8: Generate comprehensive analysis report.
        
        Returns:
            Dict[str, Any]: Complete analysis results and interpretation
        """
        logger.info("Step 8: Generating analysis report...")
        
        # Interpret R-squared value
        r2_interpretation = self._interpret_r_squared(self.r_squared)
        
        report = {
            'data_summary': {
                'sample_size': self.sample_size,
                'mean_x': self.results['mean_x'],
                'mean_y': self.results['mean_y']
            },
            'regression_coefficients': {
                'slope_beta1': self.results['beta1'],
                'intercept_beta0': self.results['beta0'],
                'equation': f"y = {self.results['beta1']:.6f}x + {self.results['beta0']:.6f}"
            },
            'model_performance': {
                'r_squared': self.results['r_squared'],
                'r_squared_percentage': self.results['r_squared'] * 100,
                'interpretation': r2_interpretation,
                'total_sum_squares': self.results['sst'],
                'residual_sum_squares': self.results['ssr']
            },
            'analysis_insights': self._generate_insights()
        }
        
        logger.info("Analysis report generated successfully")
        return report
    
    def _interpret_r_squared(self, r_squared: float) -> str:
        """Interpret R-squared value based on common thresholds."""
        if r_squared >= 0.8:
            return "Excellent fit - model explains most variance in the data"
        elif r_squared >= 0.6:
            return "Good fit - model explains substantial variance in the data"
        elif r_squared >= 0.4:
            return "Moderate fit - model explains moderate variance in the data"
        elif r_squared >= 0.2:
            return "Weak fit - model explains limited variance in the data"
        else:
            return "Poor fit - model explains very little variance in the data"
    
    def _generate_insights(self) -> list:
        """Generate analytical insights based on results."""
        insights = []
        
        r2_percent = self.results['r_squared'] * 100
        insights.append(f"The model explains {r2_percent:.2f}% of the variance in the dependent variable.")
        
        if self.results['beta1'] > 0:
            insights.append("The relationship between X and Y is positive.")
        else:
            insights.append("The relationship between X and Y is negative.")
        
        insights.append(f"For every unit increase in X, Y increases by approximately {self.results['beta1']:.4f} units.")
        
        return insights
    
    def run_complete_analysis(self) -> Dict[str, Any]:
        """
        Execute the complete linear regression analysis workflow.
        
        Returns:
            Dict[str, Any]: Complete analysis results
        """
        logger.info("Starting complete linear regression analysis...")
        
        # Execute all steps
        self.step1_generate_synthetic_data()
        self.step2_calculate_means()
        x_dev, y_dev = self.step3_calculate_deviations()
        self.step4_calculate_slope(x_dev, y_dev)
        self.step5_calculate_intercept()
        self.step6_calculate_r_squared()
        self.step7_visualize_results()
        report = self.step8_generate_report()
        
        logger.info("Complete linear regression analysis finished")
        return report


def main():
    """Main function to demonstrate the linear regression analysis."""
    print("Linear Regression Analysis Tool")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = LinearRegressionAnalyzer(sample_size=10000, random_seed=42)
    
    # Run complete analysis
    report = analyzer.run_complete_analysis()
    
    # Display results
    print("\n" + "="*50)
    print("ANALYSIS RESULTS")
    print("="*50)
    
    print(f"\nData Summary:")
    print(f"  Sample Size: {report['data_summary']['sample_size']:,}")
    print(f"  Mean X: {report['data_summary']['mean_x']:.6f}")
    print(f"  Mean Y: {report['data_summary']['mean_y']:.6f}")
    
    print(f"\nRegression Equation:")
    print(f"  {report['regression_coefficients']['equation']}")
    print(f"  Slope (β₁): {report['regression_coefficients']['slope_beta1']:.6f}")
    print(f"  Intercept (β₀): {report['regression_coefficients']['intercept_beta0']:.6f}")
    
    print(f"\nModel Performance:")
    print(f"  R-squared: {report['model_performance']['r_squared']:.6f}")
    print(f"  R-squared (%): {report['model_performance']['r_squared_percentage']:.2f}%")
    print(f"  Interpretation: {report['model_performance']['interpretation']}")
    
    print(f"\nKey Insights:")
    for insight in report['analysis_insights']:
        print(f"  • {insight}")
    
    # Save results to JSON
    with open('linear_regression_results.json', 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"\nResults saved to 'linear_regression_results.json'")


if __name__ == "__main__":
    main()