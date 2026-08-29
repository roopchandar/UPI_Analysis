# Notebooks
This folder contains the Jupyter Notebook used for the full experimental analysis of missing-value imputation in UPI payment data.

## Main Notebook
- `test(1).ipynb` — Complete end-to-end implementation of the study.
The notebook contains the following stages:

1. **Data Preprocessing**
2. **Artificial Missingness Generation**
3. **Imputation Techniques**
   - Mean
   - Median
   - KNN
   - MICE
   - Time-Series Interpolation
4. **Accuracy Evaluation**
   - RMSE
   - MAE
5. **Distribution Preservation**
   - KS Statistic
   - Variance Ratio
6. **Autocorrelation Preservation**
   - ACF RMSE
   - ACF MAE
   - ACF Correlation
7. **Consolidated Comparison**
8. **Robustness Analysis**
   - Multiple random seeds
   - 5%, 10%, and 20% missingness
