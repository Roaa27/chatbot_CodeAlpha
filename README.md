# 🤖 Chatbot AI

**Chatbot AI** is a smart multilingual chatbot (Arabic + English) based on an **FAQ database**.  
It supports **text + voice responses** and includes a **History Sidebar** to display previous questions.  
The user interface is designed with a **dark purple theme** and clear text for a professional look.

---

## ✅ Features

- 🧠 **Advanced AI FAQ**: Advanced questions and answers about AI  
- 💬 **Multilingual**: Supports Arabic and English  
- 🔊 **Text-to-Speech**: Replies with both text and voice using gTTS  
- 🕘 **History Sidebar**: View previous questions at a glance  
- 🎨 **Beautiful UI**: Dark purple background with readable text  
- 📱 **Send button**: Easy to use on mobile devices  

---

## 🛠️ Run Locally

1. Install required packages:

```bash
pip install streamlit pandas scikit-learn gTTS
streamlit run app.py
🌐 Try Online

##Try the chatbot live on Streamlit:
Chatbot AI Online :https://imkpbcdaonnwubeswoyrnj.streamlit.app/

📂 Project Files
app.py – Main Streamlit app code
faq.csv – FAQ database with Arabic and English questions and answers
💡 How it Works
User types a question in Arabic or English.
Chatbot finds the most similar FAQ using TF-IDF + cosine similarity.
Displays the answer in text and plays it in voice.
Keeps chat history in the sidebar.
🎨 UI Preview
Dark purple background
Clear readable text
Current question and answer displayed in main screen
Sidebar shows past questions
