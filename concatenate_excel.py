import os
import pandas as pd
from tkinter.filedialog import askdirectory

df = pd.DataFrame()

#ask user to select directory
root = askdirectory()
files = os.listdir(root)

#concatenate all excel files in one
for file in files:
    file = os.path.join(root, file)
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True)

print(df)
df.to_excel('output.xlsx')
