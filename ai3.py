import pandas as pd 

sales = pd.DataFrame({
    'customer': ['Hyarel', 'Priya', 'Hyarel'],
    'item': ['Sugar', 'Rice', 'Oil'],
    'price': [90, 250, 150]
})
print(sales)
print(sales['price'].sum()) # Total selling = 490
