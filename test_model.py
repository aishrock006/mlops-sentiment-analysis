# test_model.py
from model import train_model


def test_accuracy():
    accuracy = train_model()
    assert accuracy > 0.7, f"Accuracy is too low: {accuracy}"
    print(f"Test passed with accuracy: {accuracy}")


if __name__ == "__main__":
    test_accuracy()
