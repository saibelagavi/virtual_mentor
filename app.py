
from flask import Flask, request, jsonify

app = Flask(__name__)
stored_text = ""

@app.route('/gettext', methods=['GET'])
def get_text():
    global stored_text
    text = request.args.get('text')
    if text:
        stored_text = text
        return jsonify({"message": "Text stored successfully."})
    return jsonify({"error": "No text provided."}), 400

@app.route('/posttext', methods=['POST'])
def post_text():
    return jsonify({"stored_text": stored_text})

if __name__ == '__main__':
    app.run(debug=True)
