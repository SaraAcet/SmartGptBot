import fitz

def pdf_metnini_ayikla(pdf_path):
    doc = fitz.open(pdf_path)
    tam_metin = ""
    for sayfa in doc:
        tam_metin += sayfa.get_text("text") + "\n"

    paragraflar = [p.strip() for p in tam_metin.split("\n\n") if len(p.strip()) > 30]
    return paragraflar
