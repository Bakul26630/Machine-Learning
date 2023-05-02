# Implement a classification/ logistic regression problem. For example based on different 
# features of students data, classify, whether a student is suitable for a particular activity. Based on 
# the available dataset, a student can also implement another classification problem like checking
# whether an email is spam or not.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
# Load the student dataset
student_data = pd.read_csv("student_data.csv")
# Prepare the data
X = student_data[['feature1', 'feature2', 'feature3', 'feature4']] # Features
y = student_data['label'] # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a logistic regression model
model = LogisticRegression()
# Train the model
model.fit(X_train, y_train)
# Make predictions on the test data
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print("Accuracy:", accuracy)
print('Confusion matrix:\n', cm)
print('Classification report:\n', cr)