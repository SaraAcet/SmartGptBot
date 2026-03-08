# SmartGptBot – PDF ve CSV Tabanlı Akıllı Chatbot
# SmartGptBot – Intelligent Chatbot Based on PDF and CSV

---

## Proje Hakkında | About the Project

**SmartGptBot**, PDF ve CSV veri kaynaklarını kullanarak sorulara cevap verebilen akıllı bir chatbot sistemidir.  
Proje, belge tabanlı soru cevaplama için **RAG (Retrieval-Augmented Generation)** yaklaşımını kullanır.

Kullanıcılar sisteme soru sorabilir ve chatbot, yüklenen PDF ve CSV verilerinden ilgili bilgileri bularak cevap üretir.

**SmartGptBot** is an intelligent chatbot system that answers questions using **PDF and CSV data sources**.  
The project uses the **Retrieval-Augmented Generation (RAG)** approach for document-based question answering.

Users can ask questions and the chatbot retrieves relevant information from the uploaded documents.

---

## Özellikler | Features

- PDF dosyalarından bilgi çıkarma  
- CSV veri setlerinden soru cevaplama  
- Retrieval-Augmented Generation (RAG) mimarisi  
- Basit ve kullanıcı dostu arayüz  
- Doküman tabanlı chatbot sistemi  
- Python tabanlı modüler yapı

- Extract information from PDF documents  
- Question answering from CSV datasets  
- Retrieval-Augmented Generation (RAG) architecture  
- Simple and user-friendly interface  
- Document-based chatbot system  
- Modular Python structure

---

## Kullanılan Teknolojiler | Technologies Used

- Python
- Gradio
- Pandas
- NLP techniques
- Retrieval-Augmented Generation (RAG)

---

## Proje Yapısı | Project Structure
SmartGptBot
│
├── app.py # Ana chatbot uygulaması
├── rag.py # RAG mimarisi ve veri çekme işlemleri
├── pdf_utils.py # PDF veri işleme fonksiyonları
├── dialog.csv # Konuşma veri seti
├── source.pdf # Chatbot bilgi kaynağı
├── requirements.txt # Gerekli kütüphaneler
└── README.md


---

## Kurulum | Installation

Projeyi çalıştırmak için:
```bash
git clone https://github.com/SaraAcet/SmartGptBot.git
cd SmartGptBot


---


## Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt


---


## Çalıştırma | Run the Project
python app.py
Uygulama çalıştırıldığında chatbot arayüzü açılacaktır.


---


## Kullanım | Usage
Chatbot uygulamasını başlatın
Kullanıcı sorusunu girin
Sistem PDF ve CSV kaynaklarını analiz ederek cevap üretir

---

## Önemli Not | Important Note
Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.
Projedeki veri dosyaları örnek amaçlıdır.

This project was developed for educational and research purposes.
The datasets used in the project are for demonstration purposes.


---


## Geliştirici | Developer
Sara Acet
GitHub:
https://github.com/SaraAcet
