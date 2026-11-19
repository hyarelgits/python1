import pandas as pd

df = pd.DataFrame({
    'name': ['Hyarel', 'Priya', 'Rahul'],
    'cibil': [750, None, 550]  # Priya CIBIL missing
})

print(df.isnull().sum())  # Find missing
print(df.fillna(660))  # Fill missing with average 660
print(df.dropna())  # Or delete Priya row
