from sklearn.linear_model import LogisticRegression
import numpy as np

class Predictor:
    def __init__(self):
        self.model = LogisticRegression()

    def train_model(self, X, y):
        self.model.fit(X, y)

    def predict_disaster(self, data_point):
        # Ensure the model is fitted before prediction
        if not hasattr(self.model, "coef_"):
            raise ValueError("The model has not been trained yet. Please train the model before prediction.")
        prediction = self.model.predict(np.array([[data_point.value]]))
        return prediction

# Example training data (replace with actual historical data)
X_train = np.array([[15], [18], [20], [25]])
y_train = np.array([0, 0, 1, 1])

# Example usage
predictor = Predictor()
predictor.train_model(X_train, y_train)
