# Terminology Reference

Bảng này thống nhất cách dùng từ trong kho. Phần giải thích ngắn giúp định hướng; khi viết bài học cần bổ sung định nghĩa toán học, giả thiết và nguồn cụ thể. Đây không phải ghi chú hoàn chỉnh hay xác nhận tiến độ học.

| English term | Conceptual explanation |
| --- | --- |
| degrees of freedom (DOF) | Số tham số độc lập cần để mô tả configuration, theo mô hình và constraints đang xét. |
| configuration space (C-space) | Tập tất cả configurations khả dĩ của hệ theo các constraints đã nêu. |
| rigid body | Mô hình vật có khoảng cách giữa mọi cặp điểm không đổi. |
| reference frame | Hệ trục có gốc và hướng xác định, dùng để biểu diễn các đại lượng hình học. |
| position / orientation / pose | Position mô tả vị trí; orientation mô tả hướng; pose kết hợp cả hai đối với một reference frame. |
| joint / link / end-effector | Joint mô tả liên kết cho phép hoặc ràng buộc chuyển động; link là vật thể trong cơ cấu; end-effector là bộ phận thực hiện nhiệm vụ ở đầu robot arm. |
| forward kinematics / inverse kinematics | Forward kinematics suy ra end-effector pose từ joint variables; inverse kinematics tìm joint variables phù hợp với pose yêu cầu. |
| Jacobian | Matrix liên hệ joint velocities với một biểu diễn end-effector velocity; phải nêu rõ biểu diễn và reference frame. |
| twist / wrench | Twist kết hợp angular và linear velocity; wrench kết hợp moment và force. Cần ghi rõ reference frame và thứ tự thành phần. |
| dynamics | Mô hình quan hệ giữa motion, inertia và forces/torques. |
| path / trajectory | Path mô tả đường đi; trajectory mô tả chuyển động có tham số thời gian. |
| feedback control | Cách xác định control input dựa trên thông tin đo hoặc ước lượng về trạng thái hoặc output của hệ. |
| mobile manipulation | Thao tác kết hợp chuyển động của mobile base và robot arm. |

Đối chiếu cách dùng trong [Modern Robotics — nguồn chính thức](https://modernrobotics.org/). Quy tắc trình bày nằm trong [writing-guide.md](writing-guide.md).
