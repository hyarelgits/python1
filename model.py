from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

model1 = LogisticRegression()
model1.fit(X_train, y_train)
print("Logistic:", model1.score(X_test, y_test))

model2 = RandomForestClassifier()
model2.fit(X_train, y_train)
print("Random Forest:", model2.score(X_test, y_test))
