import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno

# Load RBI dataset
df_rbi = pd.read_csv('RBI_Cleaned_Final.csv')

# Fix date column
df_rbi['Date'] = pd.to_datetime(df_rbi['Date'], format='%b-%Y', errors='coerce')
df_rbi = df_rbi.sort_values('Date').reset_index(drop=True)

# Select a RELEVANT SUBSET of columns (mix of high and low missingness)
# This prevents the plot from being overcrowded
selected_cols = [
    '2.7 UPI @_Volume (Lakh)',          # UPI - missing before 2019
    '2.7 UPI @_Value( Rupees Crores )',
    '2.4 IMPS_Volume (Lakh)',           # IMPS - mostly complete
    '2.6 NEFT_Volume (Lakh)',           # NEFT - mostly complete
    '1 Credit Transfers - RTGS (1.1 to 1.2)_Volume (Lakh)',  # RTGS - complete
    '1.1.2 Repo_Volume (Lakh)',         # Repo - many missing
    '1.1.3 Tri-party Repo_Volume (Lakh)', # Tri-party - many missing
    '1.2 Forex Clearing_Volume (Lakh)', # Forex - partial
    '3.1 BHIM Aadhaar Pay @_Volume (Lakh)', # Newer indicator - missing in early years
    '5.1 Wallets_Volume (Lakh)'         # Wallets - partial
]

# Keep only columns that actually exist
existing_cols = [col for col in selected_cols if col in df_rbi.columns]
df_rbi_subset = df_rbi[existing_cols]

# Remove rows that are all NaN (to avoid empty white bands at the top)
df_rbi_subset = df_rbi_subset.dropna(how='all')

# --- PROPER SCALING ---
n_rows, n_cols = df_rbi_subset.shape

# Dynamic figure size: wider for more columns, taller for more rows
fig_width = max(12, n_cols * 1.2)   # at least 12 inches wide
fig_height = max(6, n_rows * 0.3)   # at least 6 inches tall

plt.figure(figsize=(fig_width, fig_height))

# Plot matrix with proper settings
msno.matrix(
    df_rbi_subset, 
    sparkline=False,          # Remove right-side sparkline (saves space)
    fontsize=11,              # Readable font
    color=(0.2, 0.4, 0.8),    # Professional blue
    labels=True               # Show column names
)

# Rotate x-axis labels to prevent overlapping
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Add title and adjust layout
plt.title('Missing Value Pattern in RBI Payment System Dataset\n(Selected Indicators)', 
          fontsize=14, pad=20)
plt.xlabel('Payment System Columns', fontsize=12)
plt.ylabel('Time (Months)', fontsize=12)

# Tight layout with extra padding
plt.tight_layout(pad=2.0)

# Save with high DPI
plt.savefig('rbi_missing_matrix_scaled.png', dpi=300, bbox_inches='tight')
plt.show()

# Load and clean UPI data
df_upi = pd.read_csv('upi_data_enhanced.csv')
df_upi = df_upi.replace([np.inf, -np.inf], np.nan)

# Dynamic figure size
n_cols = len(df_upi.columns)
fig_width = max(8, n_cols * 0.8)

plt.figure(figsize=(fig_width, 6))

# Bar chart with proper scaling
msno.bar(df_upi, fontsize=11, color='steelblue')

plt.xticks(rotation=30, ha='right', fontsize=10)
plt.title('Missing Value Counts per Column (UPI Dataset)', fontsize=14, pad=15)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Number of Missing Values', fontsize=12)

plt.tight_layout()

plt.show()