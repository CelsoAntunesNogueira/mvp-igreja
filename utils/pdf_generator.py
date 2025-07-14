# Em utils/pdf_generator.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def gerar_ata_pdf(dados_ata: dict, filename: str):
    c = canvas.Canvas(filename, pagesize=letter)
    # ... lógica para desenhar texto, linhas, etc. no PDF ...
    c.drawString(72, 800, f"Ata da Reunião - {dados_ata['igreja_nome']}")
    c.drawString(72, 780, f"Data: {dados_ata['data']}")
    # ... mais dados ...
    c.save()
    print(f"PDF '{filename}' gerado com sucesso.")