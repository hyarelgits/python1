import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.DataFrame({
    'name': ['Hyarel', 'Priya', 'Rahul', 'Sneha', 'Amit', 'Ramesh', 'Suresh', 'Anjali'],
    'cibil': [750, 680, 550, 720, 600, 800, 580, 690],
    'approved': [1, 1, 0, 1, 0, 1, 0, 1]
})

print(df)

X = df[['cibil']]
y = df['approved']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

print("X_train:", X_train.values.tolist())
print("X_test:", X_test.values.tolist())
print("Real:", y_test.tolist())
print("Predicted:", model.predict(X_test).tolist())
print("Accuracy:", model.score(X_test, y_test))

with open('loan_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model Saved - loan_model.pkl")
