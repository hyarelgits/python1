import pandas as pd
from sklearn.linear_model import LogisticRegression

x = [[750], [600], [590], [600]]
y = [1, 0, 0, 0]

model = LogisticRegression()
model.fit(x, y)

print(model.predict([[700]]))


