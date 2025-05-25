from django.contrib import admin
from .models import User
from deepface import DeepFace
from deepface import DeepFace
import numpy as np
import cv2
import json

from django.contrib import admin, messages
from deepface import DeepFace
import numpy as np
import cv2
import json

class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.photo and not obj.embedding:
            try:
                # Đọc file ảnh từ obj.photo (ImageField)
                file = obj.photo.file
                img_bytes = file.read()
                np_arr = np.frombuffer(img_bytes, np.uint8)
                img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

                # Trích xuất embedding
                result = DeepFace.represent(img_path=img, model_name='Facenet', enforce_detection=True)

                if result:
                    embedding = result[0]['embedding']
                    obj.embedding = json.dumps(embedding)

                # Tiếp tục lưu
                super().save_model(request, obj, form, change)
                messages.success(request, "Người dùng đã được lưu và embedding đã được tạo.")

            except Exception as e:
                # Thông báo lỗi và không lưu object
                messages.error(request, f"Lỗi khi trích xuất embedding: {e}")
        else:
            # Không có ảnh hoặc embedding đã tồn tại → lưu như bình thường
            super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
