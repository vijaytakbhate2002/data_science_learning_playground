# Machine Learning

This folder is dedicated to machine learning projects, model implementations, and tutorials covering various algorithms and techniques.

## Chapter 1: Principal Component Analysis (PCA)

### Overview

In this chapter, I explored Principal Component Analysis (PCA), a dimensionality reduction technique used to transform high-dimensional data into a lower-dimensional space while preserving maximum variance. The project demonstrates how to compute principal components, understand their contribution to variance, and visualize relationships in reduced dimensions.

### Key Concepts Explored

- **What is PCA**: A mathematical technique that adjusts data dimensions by identifying principal components (PC1, PC2, PC3, etc.) that hold the largest information content or eigenvalues of the entire dataset.
- **Use Cases**: Feature reduction for high-dimensional datasets, identifying clusters, and representing high-dimensional data in lower dimensions.
- **Data Centering**: Computing mean vectors and centering data to ensure principal components are calculated correctly.
- **Eigenvalues and Eigenvectors**: Computing eigenvectors as the best-fit directions and understanding their role in PCA.
- **Variance Explanation**: Using scree plots to visualize the percentage of information retained by each principal component.
- **Dimensionality Reduction**: Projecting data onto principal components to create 2D visualizations from 3D data.

### Implementation Highlights

- Loaded and visualized 3D synthetic correlated data using interactive 3D scatter plots.
- Computed mean vectors and centered data to shift the origin to the mean.
- Performed Singular Value Decomposition (SVD) to extract principal components.
- Calculated unit eigenvectors (normalized principal components) for PC1, PC2, and PC3.
- Created visualizations showing all three eigenvectors in 3D space.
- Generated scree plot demonstrating that PC1 retains 96.93% of variance while PC2 adds only 2.66%.
- Projected centered data onto principal components to create 2D scatter plot of PC1 vs PC2.

### Files

- `1_principal_componenet_analysis/PCA.ipynb`: Jupyter notebook containing the complete PCA implementation and visualizations.
- `1_principal_componenet_analysis/Sythetic_Correlated_Data.csv`: Synthetic dataset with three correlated features used for PCA analysis.

---

## Chapter 2: Binomial Distribution

### Overview

In this chapter, I explored the binomial distribution, a fundamental probability distribution used to model the number of successes in a fixed number of independent trials with a constant probability of success. The project demonstrates both theoretical and empirical approaches to understanding and computing binomial probabilities.

### Key Concepts Explored

- **Binomial Distribution**: A discrete probability distribution describing the number of successes in n independent trials, each with probability p of success.
- **Parameters**: Understanding the role of n (number of trials) and p (probability of success) in shaping the distribution.
- **Probability Mass Function (PMF)**: Computing the probability of exactly k successes using the binomial formula.
- **Empirical vs Theoretical Probability**: Comparing probabilities derived from observed data with theoretical calculations.
- **Binomial Formula**: Using combinatorics and probability to calculate P(X = k) = C(n,k) × p^k × (1-p)^(n-k).

### Implementation Highlights

- Generated binomial data with n=10 trials, p=0.5 probability, and 1000 samples.
- Created frequency distribution showing counts of each number of successes.
- Generated histogram to visualize the binomial distribution shape.
- Calculated theoretical probabilities using scipy.stats.binom.pmf().
- Computed empirical probabilities from observed data and compared with theoretical values.
- Implemented binomial probability formula manually using combinatorics to verify results.
- Demonstrated agreement between empirical and theoretical probabilities (0.207 vs 0.205).

### Files

- `2_binomial_distribution/binomial_distribution.ipynb`: Jupyter notebook containing binomial distribution analysis, visualizations, and probability calculations.

---

## Future Chapters

[To be added as new explorations are completed]
