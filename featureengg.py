import pandas as pd

df = pd.DataFrame({'cibil': [750, 680, 550]})

# New feature - Good if CIBIL > 650
df['is_good'] = df['cibil'].apply(lambda x: 1 if x > 650 else 0)
print(df)
