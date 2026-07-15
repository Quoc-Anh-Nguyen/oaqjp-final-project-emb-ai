"""Utility functions for detecting emotions using the Watson NLP API."""

import requests

EMOTION_PREDICT_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

EMOTION_PREDICT_HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}


def run_emotion(text_to_analyze: str):
    """Analyze the input text and return emotion scores."""

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        EMOTION_PREDICT_URL,
        headers=EMOTION_PREDICT_HEADERS,
        json=payload,
        timeout=30
    )

    # Handle blank input
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response.raise_for_status()

    result = response.json()

    emotions = result["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }