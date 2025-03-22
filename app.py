from flask import Flask, request, jsonify, render_template
from analyze import get_sentiment, compute_embeddings, classify_email
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    print("Home page")
    return render_template('index.html')

@app.route("/api/v1/update-classes", methods=['POST'])
def update_classes():
    if request.is_json:
        data = request.get_json()
        action = data.get('action')
        classes = data.get('classes', [])

        with open('email_classes.json', 'r') as f:
            email_classes = json.load(f)

        if action == 'add':
            email_classes['email_classes'].extend(classes)
        elif action == 'delete':
            email_classes['email_classes'] = [cls for cls in email_classes['email_classes'] if cls not in classes]
        else:
            return jsonify({"error": "Invalid action"}), 400

        with open('email_classes.json', 'w') as f:
            json.dump(email_classes, f, indent=4)

        return jsonify({"message": f"Classes {action}ed", "classes": classes}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400

@app.route("/api/v1/get-classes", methods=['GET'])
def get_classes():
    with open('email_classes.json', 'r') as f:
        email_classes = json.load(f)
    return jsonify({"classes": email_classes['email_classes']}), 200

@app.route("/api/v1/sentiment-analysis/", methods=['POST'])
def analysis():
    if request.is_json:
        data = request.get_json()
        sentiment = get_sentiment(data['text'])
        return jsonify({"message": "Data received", "data": data, "sentiment": sentiment}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400

@app.route("/api/v1/valid-embeddings/", methods=['GET'])
def valid_embeddings():
    embeddings = compute_embeddings()
    formatted_embeddings = []
    for text, vector in embeddings:
        formatted_embeddings.append({
            "text": text,
            "vector": vector.tolist() if hasattr(vector, 'tolist') else vector
        })
    embeddings = formatted_embeddings
    return jsonify({"message": "Valid embeddings fetched", "embeddings": embeddings}), 200

@app.route("/api/v1/classify/", methods=['POST'])
def classify():
    if request.is_json:
        data = request.get_json()
        text = data['text']
        classifications = classify_email(text)
        return jsonify({"message": "Email classified", "classifications": classifications}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400

@app.route("/api/v1/classify-email/", methods=['GET'])
def classify_with_get():
    text = request.args.get('text')
    classifications = classify_email(text)
    return jsonify({"message": "Email classified", "classifications": classifications}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)