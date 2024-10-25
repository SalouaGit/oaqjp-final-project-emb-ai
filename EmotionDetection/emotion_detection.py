import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        # Extraire les scores des émotions
        emotions = response.json()["emotionPredictions"][0]["emotion"]
        required_emotions = {emotion: emotions[emotion] for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}

        # Identifier l'émotion dominante
        dominant_emotion = max(required_emotions, key=required_emotions.get)
        required_emotions['dominant_emotion'] = dominant_emotion

        return required_emotions
    else:
        raise Exception(f"Request failed with status {response.status_code}")
