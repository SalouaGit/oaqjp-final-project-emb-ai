from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Point de terminaison pour détecter l'émotion d'un texte donné.
    
    Récupère le texte du JSON reçu dans la requête POST, appelle la fonction
    emotion_detector pour analyser l'émotion et retourne la réponse.
    Si le texte est vide, retourne un message d'erreur.
    """
    data = request.get_json()
    text = data.get("text", "")

    response, status_code = emotion_detector(text)
    
    if status_code == 400 or response['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    return jsonify({
        "message": f"For the given statement, the system response is {response}."
    })

if __name__ == '__main__':
    app.run(debug=False)
