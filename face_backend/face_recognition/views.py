from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
import numpy as np
import cv2
from deepface import DeepFace
from numpy.linalg import norm
import json

from scipy.spatial.distance import cosine
import json

def find_identity(face_embedding, database):
    threshold = 8
    best_match = None
    min_dist = float('inf')

    for user in database:

        if not user.embedding:
            continue
        ref_embedding = np.array(json.loads(user.embedding))
        dist = norm(np.array(face_embedding) - ref_embedding)
        if dist < threshold and dist < min_dist:
            best_match = user.name
            min_dist = dist
    return best_match

# @api_view(['POST'])
# def register_user(request):
#     try:
#         name = request.data.get('name', None)
#         file = request.FILES.get('image', None)
#
#         if not name or not file:
#             return Response({'error': 'Missing name or image'}, status=status.HTTP_400_BAD_REQUEST)
#
#         img_array = np.frombuffer(file.read(), np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         if img is None:
#             return Response({'error': 'Invalid image'}, status=status.HTTP_400_BAD_REQUEST)
#
#         result = DeepFace.represent(img=img, model_name='Facenet', enforce_detection=True)
#
#         if not result:
#             return Response({'error': 'No face detected'}, status=status.HTTP_400_BAD_REQUEST)
#
#         embedding = json.dumps(result[0]['embedding'])
#
#         if User.objects.filter(name=name).exists():
#             return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Tạo user, lưu ảnh lên field photo
#         user = User(name=name, embedding=embedding)
#         # lưu file image vào trường photo
#         user.photo.save(file.name, file, save=False)
#         user.save()
#
#         return Response({'message': f'User {user.name} registered successfully'})
#
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def find_user_by_embedding(target_embedding, users, threshold=0.4):
    for user in users:
        if not user.embedding:
            continue
        user_embedding = json.loads(user.embedding)
        distance = cosine(user_embedding, target_embedding)
        if distance < threshold:
            return user  # trả về user object
    return None

@api_view(['POST'])
def recognize_user(request):
    try:
        file = request.FILES.get('image', None)

        if not file:
            return Response({'error': 'Missing image'}, status=status.HTTP_400_BAD_REQUEST)

        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            return Response({'error': 'Invalid image'}, status=status.HTTP_400_BAD_REQUEST)

        result = DeepFace.represent(img_path=img, model_name='Facenet', enforce_detection=False)
        if not result:
            return Response({'identity': 'Unknown'})

        embedding = result[0]['embedding']
        users = User.objects.all()
        matched_user = find_user_by_embedding(embedding, users)

        if not matched_user:
            return Response({'identity': 'Unknown'})

        user = matched_user
        data = {
            'identity': user.name,
            'age': user.age,
            'gender': user.gender,
            'address': user.address,
            'id_number': user.id_number,
            'photo_url': request.build_absolute_uri(user.photo.url) if user.photo else None
        }
        return Response(data)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
