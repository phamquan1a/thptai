# 🚀 Hệ thống Nhận Diện Khuôn Mặt Thời Gian Thực

Dự án triển khai một hệ thống nhận diện khuôn mặt thời gian thực sử dụng **Docker**, bao gồm:

- 👤 **Frontend người dùng**: giao diện nhận diện khuôn mặt.
- 🔐 **Admin dashboard**: giao diện quản trị người dùng.
- ⚙️ **Backend xử lý AI**: xử lý nhận diện khuôn mặt theo thời gian thực.

---

## 🧾 Hướng Dẫn Sử Dụng

### 1. Lưu File Cấu Hình `docker-compose.yml`

Tải và lưu file `docker-compose.yml`.

### 2. Khởi Động Hệ Thống Bằng Docker

Mở terminal tại thư mục chứa project và chạy các lệnh sau:

```bash
docker-compose pull
docker-compose up -d
```

### 3. Truy Cập Ứng Dụng

Sau khi các container đã được khởi chạy thành công, bạn có thể truy cập các thành phần của hệ thống tại:

- 👤 **Giao diện nhận diện khuôn mặt (Frontend người dùng)**:  
  http://localhost:3000/

- 🔐 **Trang quản trị người dùng (Admin Dashboard)**:  
  http://localhost:8000/admin/

---

## 📦 Yêu Cầu

- Docker
- Docker Compose

