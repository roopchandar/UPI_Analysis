"""
UPI Data Exploratory Visualizations
Figures:
  1. UPI Growth Trajectory (Volume vs Banks Live, dual-axis)
  2. Correlation Heatmap of numeric features
  3. Missing Value Matrix
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import missingno as msno


# Load and clean data

upi_data = pd.read_csv('upi_data_enhanced.csv')
upi_data_clean = upi_data.replace([float('inf'), float('-inf')], float('nan'))

# Parse "Aug-25" style strings into real dates, then sort chronologically
# (the raw CSV is stored newest-first, which reverses/breaks any time plot)
upi_data_clean['Month'] = pd.to_datetime(upi_data_clean['Month'], format='%b-%y')
upi_data_clean = upi_data_clean.sort_values('Month').reset_index(drop=True)

# Figure 1: UPI Growth Trajectory

fig, ax1 = plt.subplots(figsize=(14, 7))
ax2 = ax1.twinx()

ax1.plot(upi_data_clean['Month'], upi_data_clean['Volume (in Mn)'],
         color='blue', linewidth=2, label='Transaction Volume')
ax2.plot(upi_data_clean['Month'], upi_data_clean['No. of Banks live on UPI'],
         color='green', linewidth=2, label='Banks Live')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Volume (Millions)', color='blue', fontsize=12)
ax2.set_ylabel('Banks Live', color='green', fontsize=12)
plt.title('UPI Growth Trajectory: Transaction Volume vs. Banks Live', fontsize=14)

ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
fig.autofmt_xdate(rotation=0)

fig.tight_layout()
plt.show()



# Figure 2: Correlation Heatmap

numeric_features = ['No. of Banks live on UPI', 'Volume (in Mn)',
                     'Value (in Cr.)', 'Avg_Txn_Value_INR']
upi_numeric = upi_data_clean[numeric_features]
correlation_matrix = upi_numeric.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=0.5)
plt.title('Correlation Heatmap of UPI Features', fontsize=14)
plt.tight_layout()
plt.show()

