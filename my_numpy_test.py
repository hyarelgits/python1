import numpy as np
import pandas as pd
print(np.array([1000, 500, 2000]) + 100)

users_balance = np.zeros(5)
print(users_balance)

#array creation 
user_ids = np.arange(1, 6)
print(user_ids)

#array vs list
balances_list = [1000, 500, 2000]
new_list = []
for b in balances_list:
    new_list.append(b + 100)
print(new_list)

balances_np = np.array([1000, 550, 2000])
print(balances_np + 100)

#indexing and slicing 

all_cibil = np.array([750, 600, 800, 550, 700, 650])
print(all_cibil[0])
print(all_cibil[0:3])
print(all_cibil[-1])


#math operator

balances = np.array([1000, 500, 2000, 200, 400, 700])
interest = np.array([100, 50, 200, 100, 200, 100])
print(balances + interest)
print(balances * 1.1)


#aggration
print("Total", balances.sum())
print(*"averages", balances.mean())
print("max", balances.max())
print("min", balances.min())


#reshape

table = balances.reshape(2,3)
print(table)


#broadcasting

bal = np.array([[1000, 500], [1000, 3000]])
print(bal + 100)

#random

#random

fake_cibil = np.random.randint(500, 800, 6)
print(fake_cibil)



#real data scisnce use i project nympy + pandas

bal2 = np.array([1000, 500, 2000, 3000])
df = pd.DataFrame({"name": ["Hyarel", "Priya", "Rahul", "Amit"] , "balances": bal2})
df["bal3"] = df["balances"] + 100
print(df)
print("average", np.mean(df["balances"]))



#pandas

s = pd.Series([10, 20, 30, 40])

print(s)




df = pd.DataFrame({
"Name": ["Alice", "Bob", "John"],
"Age": [23, 30, 40]
})

print(df)



df = pd.DataFrame({
"Name": ["A", "B", "C"],
"Salary": [50000, 70000, 90000]
})


print(df)




data = [
[1, "A"],
[2, "B"],
[3, "C"]
]

df = pd.DataFrame(data,
columns=["ID", "Name"])

print(df)
