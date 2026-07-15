import requests

EMOTION_PREDICT_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
EMOTION_PREDICT_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def run_emotion(text_to_analyze: str):
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        EMOTION_PREDICT_URL,
        headers=EMOTION_PREDICT_HEADERS,
        json=payload
    )

    response.raise_for_status()

    # Chuyển response thành dictionary
    result = response.json()

    # Lấy dictionary chứa các điểm số cảm xúc
    emotions = result["emotionPredictions"][0]["emotion"]

    # Tìm cảm xúc có điểm cao nhất
    dominant_emotion = max(emotions, key=emotions.get)

    # Trả về đúng format yêu cầu
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }