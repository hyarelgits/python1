import pandas as pd 

data = {
     'name': [ "Hyarel", "Priya", "Rahul" ],
     'cibil': [ 800, 600, 500 ]
}

df = pd.DataFrame(data)
print(df)
print(df['cibil'].mean())
