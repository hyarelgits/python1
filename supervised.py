from sklearn.model_selection import train_test_split

X = [[750], [680], [550], [720], [600], [800], [580], [690]]
y = [1, 1, 0, 1, 0, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Train:", X_train)
print("Test:", X_test)
