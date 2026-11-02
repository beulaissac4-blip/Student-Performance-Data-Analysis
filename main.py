import subprocess
import sys
import pandas as pd

print("=" * 45)
print(" STUDENT PERFORMANCE DATA ANALYSIS SYSTEM")
print("=" * 45)

# Step 1: Data Cleaning
print("\n1. DATA CLEANING")
subprocess.run([sys.executable, "data_cleaning.py"], check=True)

# Step 2: Data Analysis
print("\n2. DATA ANALYSIS")
subprocess.run([sys.executable, "analysis.py"], check=True)

# Step 3: Data Visualization
print("\n3. DATA VISUALIZATION")
subprocess.run([sys.executable, "visualization.py"], check=True)

# Step 4: API Integration
print("\n4. REST API INTEGRATION")
subprocess.run([sys.executable, "api_data.py"], check=True)

# Step 5: Generate Report
df = pd.read_csv("cleaned_students.csv")

subjects = ["Maths", "Science", "English"]
df["Average"] = df[subjects].mean(axis=1)

with open("analysis_report.txt", "w") as file:
    file.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Total Students: {len(df)}\n")
    file.write(f"Overall Average: {df['Average'].mean():.2f}\n")
    file.write(f"Highest Average: {df['Average'].max():.2f}\n")
    file.write(f"Average Attendance: {df['Attendance'].mean():.2f}\n")

print("\n5. REPORT GENERATED SUCCESSFULLY!")
print("\nPROJECT COMPLETED SUCCESSFULLY!")