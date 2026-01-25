# ⏱️ Time Saving Analysis of Machine Learning Pipeline using Dagster

##  Project Overview
This project demonstrates how Dagster, a data orchestration tool, helps in building reproducible and efficient machine learning pipelines. The execution time of a traditional ML workflow (without Dagster) is compared with a Dagster-based pipeline using a Heart Disease Prediction dataset.

The main objective is to show how pipeline orchestration, step-wise execution, and dependency tracking improve experiment management and support faster iteration during development.

---

##  Problem Statement
Traditional machine learning workflows require rerunning the entire notebook even for small changes such as model tuning or feature updates. This leads to increased execution time, poor reproducibility, and inefficient experimentation. This project addresses these issues by orchestrating the ML workflow using Dagster.

---

##  Dataset Description
- Dataset Name: Heart Disease Prediction  
- Source: Kaggle  
- Records: 270  
- Features: 14  
- Target Variable: Heart Disease (Presence / Absence)  
- Missing Values: None  

---

##  Methodology

### 1. Traditional ML Pipeline (Without Dagster)
- Implemented using standard Python and Scikit-learn
- Steps include data loading, exploratory data analysis (EDA), feature engineering, model training, and evaluation
- The entire pipeline runs every time
- Execution time measured using the time module

Execution Time:2.39 seconds

---

### 2. Dagster-based ML Pipeline (With Dagster)
- Pipeline steps defined using `@op`
- Workflow composed using `@job`
- Pipeline steps:
- Dagster tracks execution and dependencies
- Logs show step-wise execution with RUN_START, STEP_START, and STEP_SUCCESS

Execution Time:7.19 seconds

---

##  Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Model Accuracy:
| Model | Accuracy |
|------|----------|
| Logistic Regression | 0.93 |
| Decision Tree | 0.70 |
| Random Forest | 0.87 |

Best Model: Logistic Regression

---

##  Time Comparison Summary
| Approach | Execution Time |
|---------|----------------|
| Without Dagster | 2.39 seconds |
| With Dagster | 7.19 seconds |

---

##  Key Observations
- Traditional workflows rerun all steps regardless of the scope of change
- Dagster introduces structured pipelines and execution tracking
- Initial Dagster execution may include orchestration overhead
- Dagster is especially useful for iterative development, model tuning, and larger datasets

---

##  Conclusion
This project concludes that Dagster is an effective orchestration tool for machine learning pipelines. While the first run may take slightly longer, Dagster improves reproducibility, maintainability, and efficiency during iterative experimentation by organizing workflows into well-defined pipeline steps.

---

##  Tools & Technologies Used
- Python
- Pandas
- Scikit-learn
- Dagster
- Google Colab

---

##  Repository Structure
