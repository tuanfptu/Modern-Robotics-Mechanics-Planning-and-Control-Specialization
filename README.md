# Modern Robotics — Nhật ký học bằng tiếng Việt

Nhật ký tự học của Tuan Ha và tài nguyên giáo dục miễn phí cho sinh viên theo học **Modern Robotics: Mechanics, Planning, and Control** của Northwestern University trên Coursera. Kho này lưu cách hiểu cá nhân, mã thử nghiệm và bài tập tự đặt bằng tiếng Việt.

**Hiện trạng:** mới có khung cho sáu khóa, mẫu bài học và một ví dụ động học thuận đã kiểm thử. Chưa có ghi chú bài học hoàn chỉnh; chưa xác nhận hoàn thành khóa nào.

## Mục tiêu học tập

- Hiểu không gian cấu hình, biểu diễn chuyển động và hệ tọa độ.
- Tự triển khai và kiểm tra động học, động lực học, lập kế hoạch và điều khiển.
- Kết nối mô hình toán với mô phỏng, ghi rõ giả thiết và giới hạn.
- Rèn cách giải thích bằng tiếng Việt và đối chiếu thuật ngữ tiếng Anh.

## Kiến thức và công cụ cần có

Đại số tuyến tính (vector, ma trận), giải tích cơ bản, cơ học và Python cơ bản. Dùng Python **3.10 trở lên**, NumPy, Matplotlib, Jupyter và pytest. Không cần phần cứng robot hay ROS để bắt đầu.

## Lộ trình sáu khóa

| Khóa | Điều hướng | Chương sách tham chiếu | Tiến độ học |
| --- | --- | --- | --- |
| 1 | [Foundations of Robot Motion](courses/01-foundations-of-robot-motion/README.md) | 2, 3 | Chưa bắt đầu |
| 2 | [Robot Kinematics](courses/02-robot-kinematics/README.md) | 4, 5, 6, 7 | Chưa bắt đầu |
| 3 | [Robot Dynamics](courses/03-robot-dynamics/README.md) | 8, 9 | Chưa bắt đầu |
| 4 | [Robot Motion Planning and Control](courses/04-robot-motion-planning-and-control/README.md) | 10, 11 | Chưa bắt đầu |
| 5 | [Robot Manipulation and Wheeled Mobile Robots](courses/05-robot-manipulation-and-wheeled-mobile-robots/README.md) | 12, 13 | Chưa bắt đầu |
| 6 | [Capstone Project, Mobile Manipulation](courses/06-capstone-mobile-manipulation/README.md) | Tích hợp | Chưa bắt đầu |

Học theo thứ tự. Chương sách là mốc điều hướng; xem nội dung và yêu cầu hiện hành trên Coursera.

## Theo dõi tiến độ

- [ ] Course 1: Foundations of Robot Motion
- [ ] Course 2: Robot Kinematics
- [ ] Course 3: Robot Dynamics
- [ ] Course 4: Robot Motion Planning and Control
- [ ] Course 5: Robot Manipulation and Wheeled Mobile Robots
- [ ] Course 6: Capstone Project, Mobile Manipulation

Chỉ đánh dấu khi thực sự hoàn thành; việc có sẵn thư mục hoặc chạy ví dụ không đồng nghĩa hoàn thành bài học.

## Cài đặt trên Ubuntu 22.04

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
git clone https://github.com/tuanfptu/modern-robotics-vietnamese.git
cd modern-robotics-vietnamese
python3 --version  # yêu cầu >= 3.10
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Nếu đang dùng bản sao cục bộ chưa được xuất bản, vào thư mục đó và bắt đầu từ lệnh tạo `.venv`. Các khoảng phiên bản trong requirements giữ phụ thuộc gọn nhẹ; đây không phải lockfile tái lập chính xác mọi phiên bản tương lai.

## Chạy ví dụ và kiểm thử

Từ thư mục gốc của kho, sau khi kích hoạt `.venv`:

```bash
python courses/02-robot-kinematics/code/planar_2dof.py
python courses/02-robot-kinematics/code/planar_2dof.py --save outputs/planar_2dof.png
python -m pytest -q
jupyter notebook
```

Lệnh đầu in tọa độ; `--save` tạo hình và hoạt động cả khi không có màn hình. Dùng `--show` để mở cửa sổ đồ thị trên máy có giao diện. Trong Jupyter, mở mẫu ở `courses/01-foundations-of-robot-motion/notebooks/`.

Ví dụ robot phẳng 2R dùng hai khớp quay, độ dài dương theo mét, góc theo radian, chiều dương ngược kim đồng hồ; góc khớp 2 tương đối với khâu 1. Vị trí đầu công tác:

$$
x = l_1\cos\theta_1 + l_2\cos(\theta_1+\theta_2),\qquad
y = l_1\sin\theta_1 + l_2\sin(\theta_1+\theta_2).
$$

Với $l_1=l_2=1$, $\theta_1=\pi/4$, $\theta_2=\pi/2$, kết quả xấp xỉ $(0, 1.414214)$ m. Đây là ví dụ độc lập, không phải bài chấm điểm.

## Bắt đầu Course 1

1. Mở [tổng quan Course 1](courses/01-foundations-of-robot-motion/README.md).
2. Học từ nguồn chính thức rồi tự điền [mẫu chương 2](courses/01-foundations-of-robot-motion/notes/chapter-02.md).
3. Định nghĩa ký hiệu, đơn vị và tự đặt câu hỏi kiểm tra; ghi ngày học và bằng chứng.
4. Sao chép mẫu notebook khi cần thí nghiệm. Chỉ thêm mã đã chạy và kiểm thử; chưa làm thì giữ trạng thái chưa hoàn thành.

Mỗi khóa có `notes/`, `code/`, `notebooks/`, `exercises/` và `README.md`. Dùng tên tệp tiếng Anh dạng `snake_case` cho Python; giữ bài học ngắn, nguồn rõ và diễn giải bằng lời của mình.

## ROS 2 tùy chọn

Xem [kế hoạch ROS 2 Humble riêng](optional/ros2/README.md). Chưa có tích hợp ROS; phần lõi không yêu cầu ROS.

## Nguồn chính thức và bản quyền

- [Chuyên ngành trên Coursera](https://www.coursera.org/specializations/modernrobotics).
- [Modern Robotics: sách và phần mềm](https://modernrobotics.org/), Kevin M. Lynch và Frank C. Park, Cambridge University Press, 2017.
- [Tài nguyên bổ trợ của Northwestern](https://modernrobotics.northwestern.edu/).
- [Thư viện Modern Robotics chính thức](https://github.com/NxRLab/ModernRobotics) — chỉ tham khảo, chưa là phụ thuộc của kho.

Đây là **dự án giáo dục độc lập**, không trực thuộc, không được bảo trợ và không phải tài liệu chính thức của Northwestern University hoặc Coursera. Không lưu video, slide, bản sao giáo trình hay lời giải bài chấm điểm. Nội dung gốc của bên thứ ba thuộc chủ sở hữu tương ứng; hãy truy cập qua liên kết chính thức.

Mã và nội dung gốc trong kho được phát hành theo [MIT License](LICENSE), cho phép sử dụng, sửa đổi và phân phối với thông báo bản quyền. Giấy phép này không cấp quyền đối với tài liệu bên thứ ba được dẫn liên kết.
