

import cv2
from deepface import DeepFace
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Tùy chọn: bật log nếu muốn xem chi tiết
import logging
logging.basicConfig(level=logging.INFO)

# Load webcam
cap = cv2.VideoCapture(0)

# Tạo danh sách người dùng đã đăng ký
# Có thể là các ảnh khuôn mặt trong một thư mục
registered_users = {
    "Alice": "faces/alice.jpg",
    "Bob": "faces/bob.jpg",
    "Charlie": "faces/charlie.jpg",
    "ngu như lợn": "faces/pig.jpg"
}

# Đọc ảnh và trích xuất embedding một lần duy nhất
face_db = {}
for name, img_path in registered_users.items():
    embedding = DeepFace.represent(img_path=img_path, model_name='Facenet')[0]['embedding']
    face_db[name] = embedding

from numpy.linalg import norm
import numpy as np

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


# Bắt đầu vòng lặp nhận diện
while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.represent(img_path=frame, model_name='Facenet', enforce_detection=False)
        if result:
            identity = find_identity(result[0]['embedding'])
            if identity:
                cv2.putText(frame, f"{identity}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    except Exception as e:
        print("Error:", e)

    cv2.imshow('Face Recognition (DeepFace)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
