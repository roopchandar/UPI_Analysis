# UPI Missing Data Imputation

A comparative study of missing-data imputation techniques on daily UPI transaction data.

## Objective

This project evaluates five imputation methods under different missingness patterns and levels:

- Mean
- Median
- KNN
- MICE
- Time-Series Interpolation

The methods are evaluated using:

- RMSE and MAE
- KS Statistic
- Variance preservation
- Autocorrelation preservation
- Robustness across multiple random seeds

## Key Result

**Time-Series Interpolation performed best overall**, ranking first across the consolidated evaluation and winning **30/30 robustness comparisons**.

It also showed the strongest preservation of the temporal structure of the UPI data.

## Dataset

Daily UPI transaction data containing:

- Transaction Volume (in millions)
- Transaction Value (in crores)

Period: **May 2021 – 2 August 2026**
