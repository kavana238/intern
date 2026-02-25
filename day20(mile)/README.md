# 🏭 Manufacturing Quality Stability Analysis

## 📌 Project Overview

This mini project evaluates manufacturing production stability using statistical process control techniques.

The project:
Detects defective products using Z-score
Measures variability using standard deviation
Estimates failure probability using normal distribution
Validates sampling reliability using the Central Limit Theorem (CLT)
Integrates analysis with SQL database storage
The goal is to determine whether the production process is stable and operating within acceptable quality limits.

---

## 📂 Project Structure
MINI_PROJECT_1/
│
├── data/
│ └── Piece_Dimension.csv
│
├── notebooks/
│ └── quality_analysis.py
│
├── outputs/
│ └── (saved plots / screenshots)
│
├── report/
│ └── Analytical_Report.docx
│
├── sql/
│ └── quality.sql
│
└── README.md


## 📊 Dataset

The dataset contains dimensional measurements of manufactured products:

- Item_No  
- Length  
- Width  
- Height  
- Operator  

To perform **multivariate quality analysis**, Length, Width, and Height were combined into a **composite quality metric** using their row-wise mean.

An artificial skewed batch was introduced using NumPy to simulate defective production.

---

## 🛠 Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- SciPy  
- SQLite  
- VS Code  

---

## ✅ Tasks Implemented

- Loaded real manufacturing dataset  
- Created composite quality metric (Length + Width + Height)  
- Generated normal distribution data (NumPy)  
- Introduced artificial skewed batch  
- Compared normal vs skewed production  
- Computed:
  - Mean  
  - Variance  
  - Standard Deviation  
- Applied Z-score defect detection (|Z| > 2.5)  
- Performed Before vs After Cleaning comparison  
- Calculated probability of failure using CDF  
- Stored results in SQLite database  
- Queried defective percentage  
- Demonstrated Central Limit Theorem  
- Compared Population vs Sample distribution  

---

## 📈 Key Results

- Approximately **3%** of products were classified as defective.
- Artificial skewed batch increased variability and shifted distribution.
- After cleaning, distribution became more stable and concentrated.
- Sampling distribution of means formed a normal curve, validating CLT.

---

## 🧠 Statistical Interpretation

- Mean represents expected composite product dimension.
- Standard deviation measures production consistency.
- Z-score identifies abnormal products beyond ±2.5 standard deviations.
- Probability calculation quantifies production failure risk.
- CLT confirms that sample-based inspection is statistically reliable.

---

## 🔎 Population vs Sample

- **Population Distribution**: All manufactured products (including defective batch).
- **Sample Distribution**: Distribution of sample means (sample size = 40).
- Even when the population is skewed, sample means follow a normal distribution.

---

## 💡 Insights

- Production is mostly stable but shows minor variability.
- Outlier removal significantly improves stability.
- Statistical monitoring can reduce defect rates.
- Sampling inspection is sufficient for quality control.

---

## 🚀 How to Run

1️⃣ Activate virtual environment:

```powershell
.\venv\Scripts\Activate.ps1

---
📄 Report

Detailed analysis is available in:

report/Analytical_Report.docx
