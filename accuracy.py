from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_real = [1, 1, 0, 1, 0]
y_pred = [1, 1, 0, 0, 0]

print("Accuracy:", accuracy_score(y_real, y_pred))
print("Precision:", precision_score(y_real, y_pred))
print("Recall:", recall_score(y_real, y_pred))
print("F1:", f1_score(y_real, y_pred))
