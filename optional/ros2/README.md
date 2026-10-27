# ROS 2 Humble — mở rộng tùy chọn

Phần lõi chạy bằng Python, không phụ thuộc ROS. Chưa có node hay package ROS trong kho này.

Nếu sau này cần ROS 2 Humble trên Ubuntu 22.04, cài theo [hướng dẫn chính thức](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html). Giữ workspace ROS riêng, ví dụ `~/ros2_ws`, và dùng terminal riêng đã source môi trường ROS. Không thêm phụ thuộc ROS vào `requirements.txt` của phần lõi.

Ý tưởng tương lai: chuyển góc khớp của ví dụ 2-DOF thành thông điệp JointState. Chưa triển khai hoặc kiểm thử ý tưởng này.
