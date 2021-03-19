from pdfminer.high_level import extract_text
import os
import pandas as pd
from tkinter.filedialog import askdirectory


Path = []
Type = []
Montant = []
Statut = []


#ask user to select pdf directory
rootdir = askdirectory()


i = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path = os.path.join(subdir, file)

        try:
            text = extract_text(path, page_numbers=range(1)).split("\n")

            Type.append(text[text.index('Action Name') + 2])
            Montant.append(text[text.index('Indemnisation') + 2])
            Statut.append(text[text.index('Statut approbation') + 2])
            print(i)
            i=i+1
            Path.append(path)

        except Exception:
            print("Error !")
            print(i)
            pass


df = pd.DataFrame(list(zip(Path, Type, Montant, Statut)))
print(df)
df.to_excel('output.xlsx')
