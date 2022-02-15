import pandas as pd

s = pd.Series([3, 2, 4, 5], index=['p', 'q', 'r', 's'])
s = s.sort_index()
a = pd.Series([10, 50, 200, 80,100], index=['p', 'q', 'r', 's','f'])
a = a.sort_index()

result = s.div(a)
print("----s---")
print(s)
print("----a---")
print(a)
print("-result-")
print(result)
