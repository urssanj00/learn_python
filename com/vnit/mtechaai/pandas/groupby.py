import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, 10, 20, 10, 30, 20]
}

df = pd.DataFrame(data)
print("Original DataFrame:")

# Group by 'Category' and aggregate with sum and mean
grouped = df.groupby('Category').agg({'Value': ['sum', 'mean']})
print("\nGrouped and Aggregated DataFrame:")
print(grouped)




# Find the number of elements in each group using count
count_grouped = df.groupby('Category').count()
print("\nCount of elements in each group (count):")
print(count_grouped)

# Find the total number of elements in each group using size
size_grouped = df.groupby('Category').size()
print("\nNumber of elements in each group (size):")
print(size_grouped)

a = (1,2,3,4)
print (a)

print (type(a))

b = [1,2,3,4]


print (b)

print (type(b))
