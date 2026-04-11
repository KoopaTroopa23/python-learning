import pandas as pd          # pandas library
import numpy as np           # numpy library
from sklearn.ensemble import RandomForestClassifier  # specific tool from sklearn
from sklearn.model_selection import train_test_split # specific tool from sklearn

# Sample access control data - connects to your ETL project
data = {
    "years_employed": [1, 5, 2, 8, 3, 7, 1, 4],
    "level": [1, 3, 1, 3, 2, 3, 1, 2],
    "has_access": [0, 1, 0, 1, 1, 1, 0, 1]
}

# Load data into pandas dataframe
df = pd.DataFrame(data)

# Features = what the model learns from
X = df[["years_employed", "level"]]

# Target = what the model predicts
y = df["has_access"]

# Split data - 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model trained successfully!")
print(f"Accuracy: {accuracy * 100:.1f}%")

# Predict access for a new person
new_person = pd.DataFrame({
    "years_employed": [3],
    "level": [2]
})
result = model.predict(new_person)
print(f"Access granted: {bool(result[0])}")