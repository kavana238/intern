import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import sqlite3

# Load Dataset

data = pd.read_csv("E:/intership/challenge4/manufacturing_quality_dataset_new.csv")

target_weight = 100
underweight_limit = 90   # As per question (Mean=100, Std=5)

# 1️ Normal Distribution Check


mean = data['weight'].mean()
median = data['weight'].median()
std = data['weight'].std()
skew = data['weight'].skew()

print("=== NORMAL DISTRIBUTION CHECK ===")
print("Mean:", round(mean,2))
print("Median:", round(median,2))
print("Standard Deviation:", round(std,2))
print("Skewness:", round(skew,2))

if abs(skew) < 0.5:
    print("Conclusion: Distribution is approximately NORMAL\n")
else:
    print("Conclusion: Distribution is SKEWED\n")

# Histogram + Normal Curve
sns.set(style='whitegrid')
plt.figure(figsize=(10,6))

sns.histplot(data['weight'], bins=30, stat='density', alpha=0.5)

x = np.linspace(data['weight'].min(), data['weight'].max(), 200)
normal_curve = norm.pdf(x, mean, std)

plt.plot(x, normal_curve, color='red', linewidth=3)
plt.axvline(mean, color='green', linestyle='-', linewidth=2, label='Mean')
plt.axvline(median, color='blue', linestyle='--', linewidth=2, label='Median')

plt.title("Weight Distribution with Normal Curve")
plt.xlabel("Weight")
plt.ylabel("Density")
plt.legend()
plt.show()


# 2️ Defective Batch Analysis


defective = data[data['weight'] < underweight_limit]

print("=== DEFECTIVE PART ANALYSIS ===")
print("Total parts:", len(data))
print("Underweight parts:", len(defective))

defective_batches = defective['batch_id'].unique()

print("Number of defective batches:", len(defective_batches))
print("Defective batch IDs:", defective_batches)

batch_defect_rate = data.groupby('batch_id')['weight'].apply(
    lambda x: (x < underweight_limit).mean()
)

print("\nTop 5 Worst Batches (Highest Defect Rate):")
print(batch_defect_rate.sort_values(ascending=False).head(), "\n")


# 3️ Probability Using Z-score


print("=== PROBABILITY ANALYSIS (Z-SCORE METHOD) ===")

# Z-score for 90g
z_value = (90 - 100) / 5
theoretical_probability = norm.cdf(z_value)

print("Z-score for 90g:", z_value)
print("P(weight < 90g):", round(theoretical_probability,4))
print("Percentage:", round(theoretical_probability*100,2), "%")

# P(95g < weight < 105g)
z1 = (95 - 100) / 5
z2 = (105 - 100) / 5
range_probability = norm.cdf(z2) - norm.cdf(z1)

print("\nP(95g < weight < 105g):", round(range_probability,4))
print("Percentage:", round(range_probability*100,2), "%\n")


# 4️ Central Limit Theorem


sample_means = []

for batch in data['batch_id'].unique():
    batch_data = data[data['batch_id'] == batch]['weight']
    if len(batch_data) >= 40:
        sample = batch_data.sample(40)
        sample_means.append(sample.mean())

plt.figure(figsize=(8,5))
plt.hist(sample_means, bins=10, density=True, alpha=0.6)
plt.title("Sampling Distribution of Mean (n=40)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()

print("CLT Conclusion: Sampling distribution appears approximately NORMAL\n")


# 5 Process Control Using Z-score


data['z_score'] = (data['weight'] - mean) / std
z_defects = data[abs(data['z_score']) > 2.5]

print("=== Z-SCORE DEFECT DETECTION ===")
print("Parts with |Z| > 2.5:", len(z_defects))

# Control Limits (3 Sigma Rule)
UCL = mean + 3*std
LCL = mean - 3*std

out_of_control = data[(data['weight'] > UCL) | (data['weight'] < LCL)]

print("\n=== PROCESS STABILITY CHECK ===")
print("UCL:", round(UCL,2))
print("LCL:", round(LCL,2))
print("Out-of-control parts:", len(out_of_control))

if len(out_of_control) == 0:
    print("Conclusion: Process is STABLE\n")
else:
    print("Conclusion: Process requires investigation\n")


# Control Chart
plt.figure(figsize=(12,6))
plt.plot(data['weight'], marker='o', linestyle='-', markersize=3)

plt.axhline(mean, color='green', linewidth=2, label='Mean')
plt.axhline(UCL, color='red', linestyle='--', linewidth=2, label='UCL')
plt.axhline(LCL, color='red', linestyle='--', linewidth=2, label='LCL')

plt.title("Process Control Chart")
plt.xlabel("Part Index")
plt.ylabel("Weight")
plt.legend()
plt.show()


# FINAL SUMMARY

print("=== FINAL MANAGEMENT SUMMARY ===")
print("1. Normal Distribution:", "YES" if abs(skew) < 0.5 else "NO")
print("2. Defective Batches Found:", len(defective_batches))
print("3. Underweight Probability:", str(round(theoretical_probability*100,2)) + "%")
print("4. Z-score Defects (|Z|>2.5):", len(z_defects))
print("5. Process Stability:", "STABLE" if len(out_of_control)==0 else "UNSTABLE")



#task 2

# -----------------------------
# 1. Create Database & Tables
# -----------------------------
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INTEGER
)
""")

cursor.execute("""
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE marks (
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
)
""")

# -----------------------------
# 2. Insert Sample Data
# -----------------------------
students_data = [
    (1, 'Alice', 'Computer Science', 1),
    (2, 'Bob', 'Computer Science', 2),
    (3, 'Charlie', 'Mathematics', 1),
    (4, 'David', 'Mathematics', 2),
    (5, 'Eva', 'Physics', 1),
    (6, 'Frank', 'Physics', 2),
    (7, 'Grace', 'Computer Science', 3),
    (8, 'Helen', 'Mathematics', 3),
    (9, 'Ian', 'Physics', 3),
    (10, 'Jack', 'Computer Science', 4)
]

subjects_data = [
    (101, 'Data Structures', 'Computer Science'),
    (102, 'Algorithms', 'Computer Science'),
    (201, 'Linear Algebra', 'Mathematics'),
    (202, 'Statistics', 'Mathematics'),
    (301, 'Quantum Mechanics', 'Physics'),
    (302, 'Thermodynamics', 'Physics')
]

marks_data = [
    (1, 101, 85),(1, 102, 90),
    (2, 101, 78),(2, 102, 82),
    (3, 201, 88),(3, 202, 92),
    (4, 201, 75),(4, 202, 70),
    (5, 301, 95),(5, 302, 89),
    (6, 301, 60),(6, 302, 65),
    (7, 101, 99),(7, 102, 97),
    (8, 201, 55),(8, 202, 58),
    (9, 301, 72),(9, 302, 68),
    (10,101, 91),(10,102, 94)
]

cursor.executemany("INSERT INTO students VALUES (?,?,?,?)", students_data)
cursor.executemany("INSERT INTO subjects VALUES (?,?,?)", subjects_data)
cursor.executemany("INSERT INTO marks VALUES (?,?,?)", marks_data)

conn.commit()

# -----------------------------
# 3. JOIN Strategy
# -----------------------------
query = """
SELECT s.student_id, s.name, s.department, sub.subject_name, m.marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
JOIN subjects sub ON m.subject_id = sub.subject_id
"""
df = pd.read_sql_query(query, conn)

print("\n--- Joined Data ---")
print(df)

# -----------------------------
# 4. Statistical Calculations
# -----------------------------
mean_marks = df['marks'].mean()
count_marks = df['marks'].count()
variance_marks = df['marks'].var()
std_marks = df['marks'].std()

print("\n--- Overall Statistics ---")
print("Mean:", mean_marks)
print("Count:", count_marks)
print("Variance:", variance_marks)
print("Standard Deviation:", std_marks)

# -----------------------------
# 5. Top 5% Students (by Average)
# -----------------------------
student_avg = df.groupby(['student_id','name'])['marks'].mean().reset_index()
student_avg = student_avg.sort_values(by='marks', ascending=False)

top_5_percent_count = max(1, int(len(student_avg) * 0.05))
top_students = student_avg.head(top_5_percent_count)

print("\n--- Top 5% Students ---")
print(top_students)

# -----------------------------
# 6. Abnormal Performance (Z-score)
# -----------------------------
df['z_score'] = (df['marks'] - mean_marks) / std_marks
outliers = df[np.abs(df['z_score']) > 2]

print("\n--- Abnormal Performance (|Z| > 2) ---")
print(outliers[['student_id','name','marks','z_score']])

# -----------------------------
# 7. Compare Distribution by Department
# -----------------------------
dept_stats = df.groupby('department')['marks'].agg(
    mean='mean',
    count='count',
    variance='var',
    std_dev='std'
).reset_index()

print("\n--- Department Comparison ---")
print(dept_stats)

conn.close()