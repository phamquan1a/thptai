from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from admin_backend.models import Base, User

from flask import Flask, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np

from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # Cho phép tất cả domain truy cập API (bạn có thể tùy chỉnh nếu cần)


engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.orm import scoped_session

Session = scoped_session(sessionmaker(bind=engine))


@app.route('/register', methods=['POST'])
def register():
    session = Session()  # tạo session mới cho mỗi request

    try:
        name = request.form['name']
        file = request.files['image']
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        result = DeepFace.represent(img_path=img, model_name='Facenet', enforce_detection=False)

        if not result:
            return jsonify({'error': 'No face detected'}), 400

        embedding = result[0]['embedding']
        embedding_json = json.dumps(embedding)

        # Kiểm tra người dùng đã tồn tại chưa
        if session.query(User).filter_by(name=name).first():
            return jsonify({'error': 'User already exists'}), 400

        new_user = User(name=name, embedding=embedding_json)
        session.add(new_user)
        session.commit()

        return jsonify({'message': f'User {name} registered successfully'})

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

    finally:
        session.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


