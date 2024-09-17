import pandas as pd
data = {'name': ['Alice', 'Barbie', 'Dolly', 'Julee'],
        'age': [18, 20, 22, 19],
        'city': ['Mumbai', 'Delhi', 'Chennai', 'Bangaluru']
        }
df = pd.DataFrame(data)

print(df)

df = pd.read_csv('students.csv')
print(df.head())  # To display the first 5 rows
print(df.tail(2))

print (df.keys())

ages = df['age']

print(ages)

f_df = df[df['age']>20]
print(f_df)

f_df1 = df[df['age']<=20]
print(f_df1)

print(df.  isnull())

# Selecting rows where 'Age' > 25 and 'City' is 'New York'
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'New York')]
print(filtered_df)
