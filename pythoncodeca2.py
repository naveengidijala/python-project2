import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

#loading the dataset by using path address
path = "C:\\Users\\AUAS\\Downloads\\Employee_Salaries_-_2020 (1) (1).csv"
data = pd.read_csv(path)

data['Total Pay'] = (
    data['Base Salary'].fillna(0) +
    data['2020 Overtime Pay'].fillna(0) +
    data['2020 Longevity Pay'].fillna(0)
)

#objective 1. Salary Distribution
average_pay = data['Total Pay'].mean()
median_pay = data['Total Pay'].median()
pay_std_dev = data['Total Pay'].std()
print(f"--- Salary Stats ---")
print(f"Average Pay: ${average_pay:,.2f}")
print(f"Median Pay: ${median_pay:,.2f}")
print(f"Standard Deviation: ${pay_std_dev:,.2f}")
plt.figure(figsize=(10,6))
plt.hist(data['Total Pay'], bins=50, color='skyblue', edgecolor='black')
plt.title('Total Pay Distribution')
plt.xlabel('Total Pay ($)')
plt.ylabel('Number of Employees')
plt.grid(True)
plt.tight_layout()
plt.show()

#objective 2. Top 10 Best-Paying Job Divisions
top_divisions = data.groupby('Division')['Total Pay'].mean().sort_values(ascending=False).head(10)
top_divisions.plot(kind='barh', figsize=(10,6), color='orange')
plt.title('Top 10 Highest Paying Divisions')
plt.xlabel('Average Total Pay ($)')
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()

#objective 3. Average Pay by Department
average_by_department = data.groupby('Department Name')['Total Pay'].mean().sort_values(ascending=False)
plt.figure(figsize=(12,6))
average_by_department.plot(kind='bar', color='seagreen')
plt.title('Average Total Pay by Department')
plt.ylabel('Average Total Pay ($)')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#objective 4. Line Graph of Sorted Total Pay 
sorted_pay = data['Total Pay'].dropna().sort_values().reset_index(drop=True)

plt.figure(figsize=(10,6))
plt.plot(sorted_pay, color='purple')
plt.title('Line Graph of Total Pay (Sorted)')
plt.xlabel('Employees (Sorted by Pay)')
plt.ylabel('Total Pay ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

#objective 5. Gender Pay Comparison
average_pay_by_gender = data.groupby('Gender')['Total Pay'].mean()
print("Average Pay by Gender")
print(average_pay_by_gender)

average_pay_by_gender.plot(kind='bar', color=['blue', 'pink'], figsize=(6, 6))
plt.title('Average Total Pay by Gender')
plt.ylabel('Average Total Pay ($)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
