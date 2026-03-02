import torch
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from pdf_utils import pdf_metnini_ayikla

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class SmartGptBot:
    def __init__(self, csv_path, pdf_path):
        self.df = pd.read_csv(csv_path)
        self.sorular = self.df["Soru"].tolist()
        self.cevaplar = self.df["Cevap"].tolist()

        self.soru_embeddings = model.encode(self.sorular, convert_to_tensor=True)

        self.pdf_paragraflar = pdf_metnini_ayikla(pdf_path)
        self.pdf_embeddings = model.encode(self.pdf_paragraflar, convert_to_tensor=True)

    def cevap_ver(self, kullanici_sorusu):
        soru_embedding = model.encode(kullanici_sorusu, convert_to_tensor=True)

        benzerlik_csv = util.cos_sim(soru_embedding, self.soru_embeddings)
        en_yakin_csv = torch.argmax(benzerlik_csv)
        skor_csv = benzerlik_csv[0][en_yakin_csv].item()

        benzerlik_pdf = util.cos_sim(soru_embedding, self.pdf_embeddings)
        en_yakin_pdf = torch.argmax(benzerlik_pdf)
        skor_pdf = benzerlik_pdf[0][en_yakin_pdf].item()

        if skor_csv >= skor_pdf and skor_csv > 0.5:
            return self.cevaplar[en_yakin_csv]
        elif skor_pdf > 0.5:
            cevap = self.pdf_paragraflar[en_yakin_pdf]
            return cevap[:1000]
        else:
            return "Üzgünüm, bu konuyla ilgili net bir cevabım yok."
