import streamlit as st
import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gtts import gTTS
import tempfile

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Chatbot AI", page_icon="🤖", layout="wide")

# -----------------------------
# Custom UI (Purple Theme 💜)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #1e1b2e;
}
.main {
    background-color: #1e1b2e;
}
.stTextInput input {
    background-color: #2d2a4a;
    color: white;
    border-radius: 10px;
}
.stButton button {
    background-color: #7c3aed;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    width: 100%;
}
.chat-box {
    background-color: #2d2a4a;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}
.title {
    color: #c4b5fd;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown("<h1 class='title'>🤖 Chatbot AI</h1>", unsafe_allow_html=True)

# -----------------------------
# Load Data (FAQ CSV)
# -----------------------------
df = pd.read_csv("faq.csv")
questions = df["question"].tolist()
answers = df["answer"].tolist()

# -----------------------------
# Preprocess
# -----------------------------
def preprocess(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    return text.strip()

processed_questions = [preprocess(q) for q in questions]

# -----------------------------
# Vectorization
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

# -----------------------------
# Chatbot Logic
# -----------------------------
def get_response(user_input):
    user_input = preprocess(user_input)
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    best_match = similarity.argmax()
    score = similarity[0][best_match]
    if score < 0.3:
        return "❌ مش فاهم سؤالك / I don't understand"
    return answers[best_match]

# -----------------------------
# Text-to-Speech
# -----------------------------
def speak(text):
    lang = "ar" if any("\u0600" <= c <= "\u06FF" for c in text) else "en"
    tts = gTTS(text=text, lang=lang)
    file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(file.name)
    return file.name

# -----------------------------
# Session State
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "current" not in st.session_state:
    st.session_state.current = None

# -----------------------------
# Sidebar (History)
# -----------------------------
st.sidebar.title("🕘 History")
for i, item in enumerate(st.session_state.history):
    if st.sidebar.button(item["question"], key=i):
        st.session_state.current = item

# -----------------------------
# Input
# -----------------------------
user_input = st.text_input("💬 اكتب سؤالك / Type your question", key="input")
send = st.button("Send 📤")  # زرار تحت النص

# -----------------------------
# On Send
# -----------------------------
if send and user_input:
    response = get_response(user_input)
    chat = {"question": user_input, "answer": response}
    st.session_state.history.append(chat)
    st.session_state.current = chat

# -----------------------------
# Display Current Chat
# -----------------------------
if st.session_state.current:
    st.markdown(f"<div class='chat-box'>🧑 {st.session_state.current['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-box'>🤖 {st.session_state.current['answer']}</div>", unsafe_allow_html=True)
    audio_file = speak(st.session_state.current['answer'])
    st.audio(audio_file)