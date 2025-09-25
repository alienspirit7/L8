# Linear Regression Analysis Tool 📊

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](docs/)

A comprehensive Python tool for performing linear regression analysis using pure vector operations. Perfect for educational purposes, data science learning, and professional analysis with detailed reporting and visualizations.

## 🌟 Features

### Core Capabilities
- **📈 Synthetic Data Generation**: Create realistic datasets with configurable linear relationships and noise
- **🔢 Vector-Based Calculations**: Pure numpy implementation without sklearn dependency  
- **📊 Professional Visualizations**: Publication-ready plots with regression lines and statistics
- **📋 Comprehensive Reporting**: Detailed analysis reports with insights and interpretations
- **🎯 Model Performance**: R-squared calculation and interpretation
- **🔄 Reproducible Results**: Random seed support for consistent outputs

### Educational Value
- **Step-by-step process**: Each calculation step is clearly separated and documented
- **Mathematical transparency**: See exactly how regression coefficients are calculated
- **Vector operations focus**: Learn linear algebra applications in statistics
- **Comprehensive logging**: Understand what happens at each stage

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/linear-regression-tool.git
cd linear-regression-tool

# Install dependencies  
pip install numpy matplotlib

# Or install from requirements
pip install -r requirements.txt
```

### Basic Usage

```python
from linear_regression import LinearRegressionAnalyzer

# Create analyzer instance
analyzer = LinearRegressionAnalyzer(sample_size=10000, random_seed=42)

# Run complete analysis
results = analyzer.run_complete_analysis()

# Results are displayed automatically and saved to JSON
```

### Quick Example Output
```
Linear Regression Analysis Tool
==================================================

Step 1: Generating synthetic data...
Step 2: Calculating means...
Step 3: Calculating deviations from means...
Step 4: Calculating slope using vector operations...
Step 5: Calculating intercept...
Step 6: Calculating R-squared value...
Step 7: Creating visualizations...
Step 8: Generating analysis report...

==================================================
ANALYSIS RESULTS
==================================================

Data Summary:
  Sample Size: 10,000
  Mean X: 0.499832
  Mean Y: 0.599734

Regression Equation:
  y = 0.599924x + 0.299847
  Slope (β₁): 0.599924  
  Intercept (β₀): 0.299847

Model Performance:
  R-squared: 0.4967
  R-squared (%): 49.67%
  Interpretation: Moderate fit - model explains moderate variance in the data

Key Insights:
  • The model explains 49.67% of the variance in the dependent variable.
  • The relationship between X and Y is positive.
  • For every unit increase in X, Y increases by approximately 0.5999 units.
```

## 📚 Detailed Usage

### Step-by-Step Analysis

You can also run individual steps for educational purposes:

```python
# Initialize analyzer
analyzer = LinearRegressionAnalyzer(sample_size=5000, random_seed=123)

# Step 1: Generate synthetic data
points = analyzer.step1_generate_synthetic_data(
    true_slope=0.8, 
    true_intercept=0.2, 
    noise_range=0.1
)

# Step 2: Calculate means
mean_x, mean_y = analyzer.step2_calculate_means()
print(f"Data means: X={mean_x:.4f}, Y={mean_y:.4f}")

# Step 3: Calculate deviations
x_deviations, y_deviations = analyzer.step3_calculate_deviations()

# Step 4: Calculate slope using vector operations
slope = analyzer.step4_calculate_slope(x_deviations, y_deviations)
print(f"Calculated slope: {slope:.6f}")

# Step 5: Calculate intercept
intercept = analyzer.step5_calculate_intercept()
print(f"Calculated intercept: {intercept:.6f}")

# Step 6: Calculate R-squared
r_squared = analyzer.step6_calculate_r_squared()
print(f"R-squared value: {r_squared:.4f}")

# Step 7: Create visualizations
analyzer.step7_visualize_results(figsize=(14, 6))

# Step 8: Generate comprehensive report
report = analyzer.step8_generate_report()
```

### Custom Configuration

```python
# Advanced configuration
analyzer = LinearRegressionAnalyzer(
    sample_size=50000,    # Larger dataset
    random_seed=42        # For reproducibility
)

# Custom data generation
analyzer.step1_generate_synthetic_data(
    true_slope=1.5,       # Steeper slope
    true_intercept=-0.2,  # Negative intercept  
    noise_range=0.5       # More noise
)

# Continue with analysis...
results = analyzer.run_complete_analysis()
```

## 🎯 Use Cases

### Educational Applications
- **Statistics Courses**: Demonstrate linear regression concepts with clear step-by-step calculations
- **Data Science Learning**: Understand the mathematics behind regression without black-box libraries
- **Research Methods**: Show how vector operations apply to statistical analysis

### Professional Applications  
- **Baseline Analysis**: Quick regression analysis with comprehensive reporting
- **Model Validation**: Compare against other regression implementations
- **Client Presentations**: Generate professional visualizations and interpretations

### Development Applications
- **Algorithm Learning**: Study efficient vector-based statistical calculations  
- **Performance Benchmarking**: Test numpy optimization techniques
- **Educational Tools**: Build upon this foundation for more complex analyses

## 📊 Output Examples

### Visualization Output
The tool generates professional dual-panel visualizations:
- **Left Panel**: Original data scatter plot
- **Right Panel**: Data with fitted regression line, equation, and R-squared value

### Report Structure
```json
{
  "data_summary": {
    "sample_size": 10000,
    "mean_x": 0.499832,
    "mean_y": 0.599734
  },
  "regression_coefficients": {
    "slope_beta1": 0.599924,
    "intercept_beta0": 0.299847,
    "equation": "y = 0.599924x + 0.299847"
  },
  "model_performance": {
    "r_squared": 0.4967,
    "r_squared_percentage": 49.67,
    "interpretation": "Moderate fit - model explains moderate variance",
    "total_sum_squares": 835.41,
    "residual_sum_squares": 420.33
  },
  "analysis_insights": [
    "The model explains 49.67% of the variance in the dependent variable.",
    "The relationship between X and Y is positive.",
    "For every unit increase in X, Y increases by approximately 0.5999 units."
  ]
}
```

## 🔧 API Reference

### Main Class: `LinearRegressionAnalyzer`

#### Constructor
```python
LinearRegressionAnalyzer(sample_size=10000, random_seed=None)
```
- `sample_size` (int): Number of data points to generate (1,000 - 100,000)
- `random_seed` (int): Random seed for reproducible results

#### Key Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `step1_generate_synthetic_data()` | Generate synthetic dataset | `np.ndarray` |
| `step2_calculate_means()` | Calculate coordinate means | `Tuple[float, float]` |
| `step3_calculate_deviations()` | Calculate deviations from means | `Tuple[np.ndarray, np.ndarray]` |
| `step4_calculate_slope()` | Calculate slope using dot products | `float` |
| `step5_calculate_intercept()` | Calculate y-intercept | `float` |
| `step6_calculate_r_squared()` | Calculate R-squared metric | `float` |
| `step7_visualize_results()` | Create analysis plots | `None` |
| `step8_generate_report()` | Generate comprehensive report | `Dict[str, Any]` |
| `run_complete_analysis()` | Execute full workflow | `Dict[str, Any]` |

### Mathematical Formulas Implemented

#### Linear Relationship
```
y = β₁x + β₀ + ε
```
Where: β₁ = slope, β₀ = intercept, ε = noise

#### Slope Calculation (Vector Method)
```
β₁ = (Σ(x-x̄)(y-ȳ)) / (Σ(x-x̄)²) = dot(x_dev, y_dev) / dot(x_dev, x_dev)
```

#### Intercept Calculation  
```
β₀ = ȳ - β₁x̄
```

#### R-squared Calculation
```
R² = 1 - (SSR/SST) = 1 - (Σ(y-ŷ)²)/(Σ(y-ȳ)²)
```

## 🏗️ Project Structure

```
linear-regression-tool/
├── linear_regression.py          # Main implementation
├── requirements.txt              # Dependencies
├── README.md                    # This file
├── PRD.md                       # Product Requirements Document  
├── tasks.json                   # Detailed task breakdown
├── tests/                       # Unit tests
│   ├── test_data_generation.py
│   ├── test_calculations.py
│   └── test_integration.py
├── docs/                        # Documentation
│   ├── user_guide.md
│   ├── api_reference.md
│   └── mathematical_background.md
├── examples/                    # Usage examples
│   ├── basic_usage.py
│   ├── advanced_features.py
│   └── educational_examples.py
└── results/                     # Output directory
    └── linear_regression_results.json
```

## ⚡ Performance

### Benchmarks
- **Small datasets** (1K points): < 1 second
- **Medium datasets** (10K points): < 2 seconds  
- **Large datasets** (100K points): < 8 seconds
- **Memory usage**: < 100MB for 100K points

### Optimization Features
- Vectorized numpy operations for efficiency
- Memory-efficient array operations
- Minimal intermediate variable creation
- Optimized matplotlib rendering

## 🧪 Testing

Run the test suite:

```bash
# Install testing dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage report  
pytest --cov=linear_regression tests/

# Run specific test categories
pytest tests/test_calculations.py -v
```

### Test Categories
- **Unit Tests**: Individual method testing
- **Integration Tests**: End-to-end workflow testing  
- **Performance Tests**: Speed and memory benchmarks
- **Accuracy Tests**: Validation against scipy.stats.linregress

## 📖 Documentation

### Available Documentation
- **[User Guide](docs/user_guide.md)**: Comprehensive usage tutorials
- **[API Reference](docs/api_reference.md)**: Detailed method documentation  
- **[Mathematical Background](docs/mathematical_background.md)**: Theory and formulas
- **[PRD Document](PRD.md)**: Product requirements and specifications

### Generating Documentation
```bash
# Install documentation dependencies
pip install sphinx sphinx-rtd-theme

# Build HTML documentation
cd docs/
make html
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/your-username/linear-regression-tool.git

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests to verify setup
pytest tests/
```

### Contribution Guidelines
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-name`
3. **Make** your changes with tests
4. **Run** the test suite: `pytest`
5. **Commit** with descriptive messages
6. **Push** to your fork and **submit** a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Include type hints for all functions
- Write comprehensive docstrings
- Maintain >90% test coverage
- Update documentation for new features

## 🐛 Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'numpy'"
```bash
# Install required dependencies
pip install numpy matplotlib
```

#### "ValueError: Data not generated"  
```python
# Make sure to generate data first
analyzer = LinearRegressionAnalyzer()
analyzer.step1_generate_synthetic_data()  # Required before other steps
```

#### Poor R-squared values
```python
# Try reducing noise for clearer relationships
analyzer.step1_generate_synthetic_data(noise_range=0.1)  # Less noise
```

### Getting Help
- **Issues**: Report bugs on GitHub Issues
- **Questions**: Start a GitHub Discussion  
- **Documentation**: Check the [docs/](docs/) directory
- **Examples**: See [examples/](examples/) for common use cases

## 📈 Roadmap

### Version 2.0 (Planned)
- [ ] Multiple regression support
- [ ] Polynomial regression capabilities  
- [ ] Interactive web interface
- [ ] Advanced diagnostic plots
- [ ] Integration with pandas DataFrames

### Version 1.5 (Next Release)
- [ ] Confidence interval calculations
- [ ] Residual analysis plots
- [ ] Export to multiple formats (PDF, PNG, SVG)
- [ ] Batch processing capabilities

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NumPy Community** for excellent mathematical computing tools
- **Matplotlib Team** for comprehensive visualization capabilities  
- **Scientific Python Ecosystem** for inspiring educational tools
- **Contributors** who help improve this project

## 📧 Contact

- **Project Maintainer**: [Your Name](mailto:your.email@domain.com)
- **GitHub Issues**: [Report Issues](https://github.com/your-username/linear-regression-tool/issues)
- **Documentation**: [Project Wiki](https://github.com/your-username/linear-regression-tool/wiki)

---

**Made with ❤️ for the data science community**

*Happy analyzing! 📊✨*