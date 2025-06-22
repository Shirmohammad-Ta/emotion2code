from transformers import pipeline

# بارگذاری pipeline تشخیص احساسات
emotion_classifier = pipeline("sentiment-analysis")

def classify_emotion(text: str) -> str:
    result = emotion_classifier(text)
    label = result[0]['label'].lower()
    # نگاشت ساده برچسب‌ها به احساسات کلیدی
    if 'joy' in label or 'happy' in label:
        return 'happy'
    elif 'sad' in label or 'sadness' in label:
        return 'sad'
    elif 'anger' in label or 'angry' in label:
        return 'angry'
    elif 'fear' in label or 'nervous' in label:
        return 'nervous'
    elif 'excited' in label:
        return 'excited'
    else:
        return 'neutral'
