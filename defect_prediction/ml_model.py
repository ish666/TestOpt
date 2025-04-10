import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class DefectPredictor:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, data: pd.DataFrame, label_col: str = 'defective'):
        """
        Train the model on historical defect data.
        """
        X = data.drop(columns=[label_col])
        y = data[label_col]
        self.model.fit(X, y)

    def predict(self, new_data: pd.DataFrame) -> list:
        """
        Predict defect probability for new files/modules.
        """
        return self.model.predict_proba(new_data)[:, 1]  # return probability of being defective

    def evaluate(self, data: pd.DataFrame, label_col: str = 'defective') -> str:
        """
        Evaluate model performance using classification report.
        """
        X = data.drop(columns=[label_col])
        y = data[label_col]
        y_pred = self.model.predict(X)
        return classification_report(y, y_pred)
