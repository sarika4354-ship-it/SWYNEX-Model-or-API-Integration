import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student_performance_dataset.csv")

# Input features
X = data[["study_hours", "attendance", "previous_mark", "assignment_score"]]

# Target
y = data["result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Student Performance Risk Classification")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Example student
student = [[3, 65, 55, 60]]

prediction = model.predict(student)

print("Example Student Prediction:", prediction[0])