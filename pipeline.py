from dagster import op, job
import pandas as pd
import time

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


@op
def load_data():
    return pd.read_csv("/content/Heart_Disease_Prediction.csv")


@op
def eda(df):
    print("Shape:", df.shape)
    print(df.isnull().sum())
    return df


@op
def feature_engineering(df):
    X = df.drop("Heart Disease", axis=1)
    y = df["Heart Disease"]
    X = pd.get_dummies(X, drop_first=True)
    return X, y


@op
def train_models(data):
    X, y = data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=3000),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier()
    }

    print("\nModel Accuracy:")
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"{name}: {acc:.2f}")


@job
def heart_disease_pipeline():
    df = load_data()
    df = eda(df)
    data = feature_engineering(df)
    train_models(data)


if __name__ == "__main__":
    start = time.time()
    heart_disease_pipeline.execute_in_process()
    end = time.time()
    print("\nWITH Dagster Time:", round(end - start, 2), "seconds")
