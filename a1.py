import pandas as pd

data = {
    'name': ['Hyarel', 'Priya', 'Rahul'],
    'cibil': [750, 680, 550]
}

df = pd.DataFrame(data)
print(df)
print(df['cibil'].mean()) # Average CIBIL
