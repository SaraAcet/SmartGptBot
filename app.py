import gradio as gr
from gtts import gTTS
from rag import SmartGptBot

bot = SmartGptBot("dialog.csv", "source.pdf")
gecmis = []

def chatbot_gradio(soru):
    yanit = bot.cevap_ver(soru)
    gecmis.append(f"👤 {soru}\n🤖 {yanit}")

    tts = gTTS(yanit, lang='tr')
    tts.save("cevap.mp3")

    return "\n\n".join(gecmis[-5:]), "cevap.mp3"

demo = gr.Interface(
    fn=chatbot_gradio,
    inputs=gr.Textbox(lines=2, placeholder="Sorunuzu yazın...", label="Soru"),
    outputs=[
        gr.Textbox(lines=10, label="Sohbet Geçmişi"),
        gr.Audio(label="Sesli Cevap")
    ],
    title="SMARTGPTBOT 🤖",
    description="CSV ve PDF destekli chatbot"
)

if __name__ == "__main__":
    print("Başlatılıyor...")
    demo.launch()
