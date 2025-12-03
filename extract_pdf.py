import PyPDF2
import json

# Abrir y leer el PDF
with open('Informe_Cintas_02-12-2025 (3).pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Extraer todo el texto
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    print(text)
