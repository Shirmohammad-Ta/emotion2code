import sys
from models.emotion_classifier import classify_emotion
from codegen.generator import generate_code

def main():
    print("🎭 Welcome to Emotion2Code!")
    user_input = input("How are you feeling today? 👉 ")
    emotion = classify_emotion(user_input)
    print(f"🔍 Detected emotion: {emotion}")
    code_output = generate_code(emotion)
    print("\n💡 Here's something based on your emotion:\n")
    print(code_output)

if __name__ == "__main__":
    main()
