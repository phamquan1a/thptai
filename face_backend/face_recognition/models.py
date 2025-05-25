from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác'),
    ]

    name = models.CharField(max_length=100, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=True, null=True)  # Số căn cước

    embedding = models.TextField(blank=True, null=True)  # embedding lưu JSON string
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)  # ảnh upload
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
