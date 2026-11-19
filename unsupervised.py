
from sklearn.cluster import KMeans

# X only - No y - CIBIL + Spending
X = [
    [750, 5000],
    [680, 3000],
    [550, 1000],
    [720, 4500],
    [600, 1500],
    [800, 6000],
    [580, 1200],
    [700, 4000],
]

names = ['Hyarel', 'Priya', 'Rahul', 'Sneha', 'Amit', 'Ramesh', 'Suresh', 'Anjali']

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)  # Only X, No y

for name, group in zip(names, model.labels_):
    print(name, "-> Group", group)
