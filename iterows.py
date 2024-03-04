import pandas as pd

# Sample DataFrame
data = {'name': ['John', 'Alice', 'Bob'],
        'age': [25, 30, 22],
        'city': ['New York', 'San Francisco', 'Chicago']}

df = pd.DataFrame(data)


# Iterating through rows
#for index, row in df.iterrows():
    # print(f"Index: {index}")
    # print(f"Name: {row['name']}")
    # print(f"Age: {row['age']}")
    # print(f"City: {row['city']}")
    # print("--------------------")
alice=df[df['name']=='Alice']
print(alice)