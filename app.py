from flask import Flask, request, jsonify
from flask_cors import CORS
from PushUpCounter import process_frame

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_image():
    frame = request.files['frame'].read()
    count, feedback = process_frame(frame)
    return jsonify({'count': count, 'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
