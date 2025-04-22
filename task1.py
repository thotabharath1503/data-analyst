
import pandas as pd

# Step 1: Load the dataset
file_path = "customer personality analysis.csv"
df = pd.read_csv(file_path)
print("\n--- Original Dataset (First 5 Rows) ---")
print(df.head())

# Step 2: Basic Info and Checking Missing Values
print("\n--- Dataset Info ---")
df.info()

print("\n--- Missing Values ---")
print(df.isnull().sum())

# Step 3: Drop Duplicates if Any
initial_shape = df.shape
df.drop_duplicates(inplace=True)
print(f"\n--- Dropped Duplicates: {initial_shape[0] - df.shape[0]} rows removed ---")

# Step 4: Clean Column Names
# (Remove leading/trailing whitespaces or inconsistent formatting)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
print("\n--- Cleaned Column Names ---")
print(df.columns.tolist())

# Step 5: Handle Missing or Invalid Data (if any)
# Example: Filling missing numerical columns with median (if applicable)
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        print(f"Filled missing values in '{col}' with median: {median_val}")

# Step 6: Convert Data Types if Needed
# For example, ensuring 'income' is numeric
if df['income'].dtype != 'int64' and df['income'].dtype != 'float64':
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
    print("\nConverted 'income' column to numeric")

# Step 7: Standardize Text Columns
text_cols = ['gender', 'productcategory']
for col in text_cols:
    df[col] = df[col].str.strip().str.title()

print("\n--- Sample of Standardized Text Columns ---")
print(df[['gender', 'productcategory']].head())

# Step 8: Final Cleaned Data Output
print("\n--- Final Cleaned Dataset (First 5 Rows) ---")
print(df.head())

# Optional: Save Cleaned Data
df.to_csv("cleaned_customer_data.csv", index=False)
print("\nCleaned data saved as 'cleaned_customer_data.csv'")

