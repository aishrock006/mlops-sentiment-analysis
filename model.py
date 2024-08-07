# model.py

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():
    # Load dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Train model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Test model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return accuracy


if __name__ == "__main__":
    accuracy = train_model()
    print('feature branch update!')
    print(f"Model Accuracy: {accuracy}")
