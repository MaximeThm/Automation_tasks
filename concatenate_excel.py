import os
import pandas as pd

root = '/Users/maximethomas/Desktop/CORSAIR/From_Client/Excel-new'
df = pd.DataFrame()
files = os.listdir(root)


for file in files:
    file = os.path.join(root, file)
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True)

print(df)
#df.to_excel('output.xlsx')
