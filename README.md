# 🚀 Hệ thống Nhận Diện Khuôn Mặt Thời Gian Thực


## Thành viên tham gia
- Phạm Quân 23020418
- Nông Phi Long 
- Chu Thanh Tùng 23020431
- Hoàng Nam 
- Phạm Hải Tiến


## Mô tả dự án 
Dự án triển khai một hệ thống nhận diện khuôn mặt thời gian thực sử dụng **Docker**, bao gồm:
- 👤 **Frontend người dùng**: giao diện nhận diện khuôn mặt.
- 🔐 **Admin dashboard**: giao diện quản trị người dùng.
- ⚙️ **Backend xử lý AI**: xử lý nhận diện khuôn mặt theo thời gian thực.


## ✨Tính năng nổi bật
- **Nhận diện khuôn mặt thời gian thực**: Sử dụng các thuật toán tiên tiến để nhận diện khuôn mặt nhanh chóng.
- **Quản lý người dùng tập trung**: Giao diện quản trị dễ sử dụng để thêm, sửa, xóa thông tin người dùng.
- **Triển khai dễ dàng với Docker**: Toàn bộ hệ thống được đóng gói trong các container Docker, giúp việc triển khai và mở rộng trở nên đơn giản.
- **Kiến trúc microservices**: Tách biệt các thành phần Frontend, Backend AI và Admin Dashboard, tăng tính linh hoạt và khả năng mở rộng, tạo điều kiện phát triển ứng dụng trong tương lai.


## 🛠️ Yêu Cầu Hệ Thống
Để khởi chạy hệ thống này, bạn cần cài đặt:
- **Docker, Python, Vscode**: Phiên bản mới nhất.
- **Docker Compose**: Phiên bản mới nhất (thường được cài đặt kèm Docker Desktop).


## 🧾 Hướng Dẫn Sử Dụng
### 1. Sử dụng Docker để liên kết với các Docker images sau:
https://hub.docker.com/repository/docker/quan23020418/ait_backend/general
https://hub.docker.com/repository/docker/quan23020418/ait_frontend/general


### 2. Clone repository của dự án
Clone repository của dự án về máy tính và thực hiện mở thư mục chứa dự án trong Vscode.

### 3. Khởi Động Hệ Thống
Sử dụng Vscode, mở terminal tại thư mục chứa project dự án và chạy các lệnh sau đợi container được khởi chạy:
```bash
docker-compose pull
docker-compose up -d
```


### 3. Truy Cập Ứng Dụng
Sau khi các container đã được khởi chạy thành công, bạn có thể truy cập các thành phần chính của hệ thống như sau:

- 👤 **Giao diện nhận diện khuôn mặt (Frontend người dùng)**:  
  http://localhost:3000/

- 🔐 **Trang quản trị người dùng (Admin Dashboard)**:  
  http://localhost:8000/admin/

---
