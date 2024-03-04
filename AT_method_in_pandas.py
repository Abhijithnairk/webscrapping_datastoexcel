import pandas as pd

data = {'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]}

df=pd.DataFrame(data)

print(df.at[0,'A'])
print(df.at[1,'B'])
print(df.at[2,'C'])

print(df) 

