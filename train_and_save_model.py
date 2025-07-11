from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib

# Data load
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model train
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'final_model.pkl')
