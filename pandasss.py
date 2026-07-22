'''import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)'''

import pandas as pd
data = {
   'Name': ['John', 'Anna', 'Peter'],
   'Age': [28, 24, 35]
}
df = pd.DataFrame(data)
print(df)
import pandas as pd
info = {
   "name": ["rasi", "alwin", "milesh", "rohit"],
   "age": [20, 30, 40, 50],
   "city": ["Salem", "Kovai", "Chennai", "Bengaluru"],
   "Fees": [20000, 30000, 40000, 50000]
}
d = pd.DataFrame(info)
print(d)
print(d["Fees"].values)