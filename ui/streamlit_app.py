import streamlit as st
from models.emotion_classifier import classify_emotion
from codegen.generator import generate_code
from speech.tts_output import speak_text

st.title("🎭 Emotion2Code")
st.write("Tell me how you feel, and I’ll generate something just for you!")

user_input = st.text_input("How are you feeling today?")

if user_input:
    emotion = classify_emotion(user_input)
    st.success(f"Detected emotion: {emotion}")
    output = generate_code(emotion)
    st.code(output, language='python')
    if st.button("🔊 Read it aloud"):
        speak_text(output)
