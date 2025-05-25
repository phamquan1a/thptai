# ai_backend/app.py
from flask import Flask, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép tất cả domain truy cập API (bạn có thể tùy chỉnh nếu cần)

# Load ảnh mẫu và trích xuất embedding
registered_users = {
    "Alice": "faces/alice.jpg",
    "Bob": "faces/bob.jpg",
    "Charlie": "faces/charlie.jpg",
    "quan": "faces/pig.jpg"
}

face_db = {}
for name, img_path in registered_users.items():
    embedding = DeepFace.represent(img_path=img_path, model_name='Facenet')[0]['embedding']
    face_db[name] = embedding

from numpy.linalg import norm


def find_identity(face_embedding):
    threshold = 8
    best_match = None
    min_dist = float('inf')

    for name, ref_embedding in face_db.items():
        dist = norm(np.array(face_embedding) - np.array(ref_embedding))
        if dist < threshold and dist < min_dist:
            best_match = name
            min_dist = dist
    return best_match


@app.route('/recognize', methods=['POST'])
def recognize():
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    result = DeepFace.represent(img_path=img, model_name='Facenet', enforce_detection=False)
    identity = None
    if result:
        identity = find_identity(result[0]['embedding'])
    return {'identity': identity if identity is not None else "Unknown"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
