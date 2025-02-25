import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(data_path):
    """Train a model to analyze responses."""
    df = pd.read_csv(data_path)

    # Assume 'Course recommendation based on relevance' is the target variable
    X = df.drop(columns=['Course recommendation based on relevance'])
    y = df['Course recommendation based on relevance']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    with open("outputs/model_results.txt", "w") as f:
        f.write(f"Model Accuracy: {accuracy:.2f}\n")

if __name__ == "__main__":
    train_model('outputs/preprocessed_data.csv')
