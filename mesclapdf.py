import os
from PyPDF2 import PdfMerger

diretorio = 'pdf/'

# Nome do arquivo PDF mesc
pdf_mesclado = 'resultado.pdf'

# Lista para armazenar os nomes de arquivos PDF
arquivos_pdf = []

# Verifique cada arquivo no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.pdf'):
        arquivos_pdf.append(os.path.join(diretorio, arquivo))

# Ordene a lista de arquivos PDF por nome
arquivos_pdf.sort()

# Crie um objeto PDF vazio para o PDF resultante
pdf_merger = PdfMerger()

# Adicione cada arquivo PDF à mesclagem
for arquivo_pdf in arquivos_pdf:
    pdf_merger.append(arquivo_pdf)

# Salve o PDF resultante
pdf_merger.write(pdf_mesclado)

print(f'O PDF resultante foi criado em: {pdf_mesclado}')
