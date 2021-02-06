from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas as pd

directory = r'/Users/maximethomas/Desktop/PDF'
excel = r'/Users/maximethomas/Desktop/test.xlsx'

df = pd.read_excel(excel)
pdf_names = df['Nom pdf']
pdf_pages = df['Page pdf'].values.tolist()
fournisseur = df['fournisseur'].values.tolist()

i = 0

for names in pdf_names:
    pdf_file_path = str(directory + '/' + names + '.pdf')
    print(pdf_file_path)

    pdf = PdfFileReader(pdf_file_path)

    input = pdf
    if input.isEncrypted:
        input.decrypt('')

    pages = pdf_pages[i]
    pdfWriter = PdfFileWriter()

    pdfWriter.addPage(pdf.getPage(pages - 1))

    new_name = names + str("_") + str(fournisseur[i])

    with open('{0}.pdf'.format(new_name), 'wb') as f:
        pdfWriter.write(f)
        f.close()

    i = i+1
