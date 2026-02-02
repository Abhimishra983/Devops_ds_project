 Heart Disease Prediction – ML Pipeline with Dagster & Pure Python

This project implements a machine learning pipeline for heart disease prediction, comparing execution with Dagster orchestration versus pure Python execution.
The goal is to demonstrate pipeline modularity, execution tracking, and performance comparison using industry-grade workflow orchestration.

 Project Objectives

Predict heart disease using supervised machine learning

Compare Dagster-based pipeline vs Pure Python pipeline

Visualize asset lineage / pipeline flow

Measure execution time and model performance

Build a production-style ML workflow using best practices

 Dataset

Source: Kaggle – Heart Disease Dataset

Features: Age, sex, chest pain type, cholesterol, blood pressure, ECG results, etc.

Target Variable:

0 → No heart disease

1 → Heart disease present

 Models Used

The following classification models are implemented and compared:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

 Pipeline Architecture (Dagster)

The Dagster pipeline is built using software-defined assets, enabling clear dependency tracking and parallel execution.

Asset Flow:
raw_data
 ├── eda_heatmap
 └── features
       ├── model_dt
       ├── model_knn
       ├── model_lr
       └── model_rf
              ↓
        model_comparison


A visual DAG diagram is generated in Google Colab to represent this lineage.

 Pure Python Pipeline

A separate pipeline is implemented without Dagster to serve as a baseline comparison.

Steps:

Load dataset from Kaggle

Perform preprocessing & encoding

Train all models sequentially

Measure accuracy and execution time

Report best performing model

This allows direct comparison with Dagster’s orchestration overhead and benefits.

 Performance Comparison

Both pipelines measure:

Model Accuracy

Training Time per Model

Total Pipeline Execution Time

This highlights:

Dagster’s orchestration benefits

Trade-offs between modular pipelines and raw execution speed

📊 Evaluation Metrics

Accuracy Score

Execution Time (seconds)

 Visualizations

Correlation heatmap (EDA)

Dagster-style asset lineage diagram (generated in Colab)

Model performance comparison table

 How to Run (Google Colab)
1️ Install dependencies
pip install dagster kagglehub scikit-learn pandas matplotlib

2️ Run Pure Python pipeline
python pure_pipeline.py

3️ Run Dagster pipeline
dagster dev


Open the Dagster UI and materialize assets to visualize lineage.
