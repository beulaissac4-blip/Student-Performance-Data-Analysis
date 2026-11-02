import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numerical values
df = df.fillna(df.select_dtypes(include="number").mean())

print("\nCleaned Dataset:")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nData Cleaning Completed!")