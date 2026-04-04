# R Programming Learning Journey

This folder documents my exploration and learning in R programming, focusing on statistical computing, data analysis, and visualization techniques.

## Chapter 1: Exploratory Data Analysis - Estimates of Location and Variability

### Overview

In this first chapter, I delved into fundamental concepts of exploratory data analysis using R. The project demonstrates statistical measures for understanding data distribution, including estimates of location (central tendency) and variability (spread), applied to real-world population data.

### Key Concepts Explored

- **Estimates of Location**: Mean, trimmed mean, weighted mean, median, and weighted median calculations to understand central tendencies in data.
- **Estimates of Variability**: Mean Absolute Deviation (MAD), standard deviation, variance, and Interquartile Range (IQR) for measuring data spread and detecting outliers.
- **Data Visualization**: Creating box plots and violin plots using ggplot2 to visualize data distributions and identify patterns.
- **Outlier Detection**: Using IQR method to establish bounds for identifying potential outliers in datasets.

### Implementation Highlights

- Loaded population data by country for 2020 from a CSV file.
- Computed various statistical measures on population metrics like total population, land area, population density, and median age.
- Implemented weighted calculations to account for population size in statistical measures.
- Created interactive visualizations to better understand data distributions and variability.
- Demonstrated practical applications of statistical concepts in real-world demographic analysis.

### Files

- `1_exploratory_data_analysis/1_estimates_of_location_and_variability.ipynb`: Jupyter notebook containing the complete exploratory data analysis implementation.
- `1_exploratory_data_analysis/population_by_country_2020.csv`: Dataset containing population statistics by country used for the analysis.

---

## Chapter 2: Exploratory Data Analysis - Correlation and Bivariate Analysis

### Overview

In this chapter, I explored correlation analysis and bivariate analysis techniques using R. The project demonstrates methods for analyzing relationships between two features (bivariate analysis) through both numeric-numeric relationships using correlation, and categorical-numerical relationships using visualization techniques.

### Key Concepts Explored

- **Correlation Analysis**: Computing correlation coefficients between numeric features to measure linear relationships and their strength/direction.
- **Correlation Matrix Visualization**: Creating correlation matrices and visualizing them using `corrplot` to identify patterns and relationships across all numeric variables.
- **Bivariate Visualization (Numeric vs Numeric)**:
  - Scatter plots for initial relationship visualization
  - Hexagonal binning plots for handling density in large datasets
  - 2D Density/Contour plots to reveal hidden density patterns and cluster areas
- **Categorical vs Numerical Analysis**:
  - Box plots to visualize distribution differences across categories
  - Violin plots to display density distribution and better understand data concentration patterns
- **Understanding Data Limitations**: Recognizing when standard plots are insufficient and choosing appropriate visualization strategies for different data characteristics.

### Implementation Highlights

- Loaded and analyzed the built-in `mtcars` dataset to compute and visualize correlations between variables.
- Calculated pairwise correlations (e.g., hp vs. wt, hp vs. mpg) and visualized the complete correlation matrix.
- Used the `diamonds` dataset from `ggplot2` to demonstrate various bivariate visualization techniques.
- Created scatter plots with transparency adjustment to handle overplotting.
- Implemented hexagonal binning to reveal density patterns in crowded visualizations.
- Generated 2D density/contour plots to identify clusters and density concentrations.
- Applied box plots and violin plots to compare price distributions across clarity categories in the diamonds dataset.
- Provided detailed interpretations of each visualization technique and their advantages.

### Files

- `1_exploratory_data_analysis/2_correlation_and_bivariate_anaylysis.ipynb`: Jupyter notebook containing the complete correlation and bivariate analysis implementation.

---

## Future Chapters

[To be added as new explorations are completed]
