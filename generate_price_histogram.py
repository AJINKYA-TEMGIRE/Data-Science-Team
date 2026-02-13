import os
import pandas as pd
import matplotlib.pyplot as plt

# Paths
DATA_PATH = os.path.join('data', 'Pune_property_data.csv')
CLEANED_CSV = 'cleaned_pune_property_data.csv'
HISTOGRAM_IMG = os.path.join('plots', 'price_histogram.png')

# Ensure output directory exists
os.makedirs(os.path.dirname(HISTOGRAM_IMG), exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)

# Clean 'price' column: remove non-numeric characters, convert to numeric
def clean_price(value):
    if pd.isnull(value):
        return None
    # Convert to string and strip spaces
    s = str(value).strip()
    # Remove common currency symbols and commas
    s = s.replace('Rs.', '').replace('Rs', '').replace('INR', '')
    s = s.replace(',', '')
    # Remove any other non-digit characters (e.g., spaces, hyphens)
    s = ''.join(ch for ch in s if (ch.isdigit() or ch == '.'))
    try:
        return float(s) if s else None
    except ValueError:
        return None

df['price'] = df['price'].apply(clean_price)

# Drop rows where price is missing after cleaning
df_clean = df.dropna(subset=['price']).reset_index(drop=True)

# Save cleaned DataFrame
df_clean.to_csv(CLEANED_CSV, index=False)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(df_clean['price'], bins=50, edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(HISTOGRAM_IMG)
plt.close()

print('Cleaning and plotting completed.')
print(f'Cleaned CSV saved to: {CLEANED_CSV}')
print(f'Histogram image saved to: {HISTOGRAM_IMG}')