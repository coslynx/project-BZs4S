```python
# aiPoweredModeration.py

import numpy as np
from sklearn.linear_model import LogisticRegression

class AiPoweredModeration:
    def __init__(self):
        self.model = LogisticRegression()

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate_model(self, X_test, y_test):
        return self.model.score(X_test, y_test)

    def save_model(self, filename):
        np.save(filename, self.model)

    def load_model(self, filename):
        self.model = np.load(filename)

# Example usage:
# ai_moderator = AiPoweredModeration()
# ai_moderator.train_model(X_train, y_train)
# prediction = ai_moderator.predict(X_test)
# accuracy = ai_moderator.evaluate_model(X_test, y_test)
# ai_moderator.save_model('ai_model.npy')
# ai_moderator.load_model('ai_model.npy')
```