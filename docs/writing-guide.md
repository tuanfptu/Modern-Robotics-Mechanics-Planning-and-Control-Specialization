# Academic Writing and Study Guide

Áp dụng cho README, notes, exercises, notebooks và phần mô tả thí nghiệm. Tài liệu này quy định cách viết; không phải ghi chú đã hoàn thành bài học.

## Language and Terminology

- Giữ nguyên thuật ngữ chuyên ngành bằng tiếng Anh: configuration space, rigid body, forward kinematics, Jacobian, twist, wrench, trajectory, feedback control… Không thay thuật ngữ bằng một bản dịch tiếng Việt trong tiêu đề hoặc lập luận.
- Use English for headings, technical summaries, definitions when practical, and all code. Use Vietnamese for intuition or detailed reasoning when it improves comprehension. Do not duplicate every paragraph in both languages.
- Lần đầu dùng thuật ngữ, giải thích ngắn và chính xác. Ví dụ: “Forward kinematics xác định pose của end-effector từ các joint variables khi mô hình hình học đã biết.” Sau đó dùng nhất quán thuật ngữ đó.
- Định nghĩa viết tắt ở lần đầu xuất hiện trong mỗi bài: degrees of freedom (DOF), configuration space (C-space), product of exponentials (PoE). Không giả định người đọc đã đọc bài khác.
- Giữ nguyên tên chính thức của course, chapter, API và tên biến trong code. Tiêu đề chapter dùng tên trong sách; trong câu văn thông thường dùng chữ thường, trừ tên riêng và ký hiệu.

## Lesson Structure

1. **Câu hỏi và trực giác:** bài học giải quyết vấn đề gì, có ý nghĩa vật lý nào?
2. **Định nghĩa:** nêu chính xác đối tượng và technical terms cần dùng.
3. **Giả thiết và quy ước:** reference frame, đơn vị, chiều dương, cách biểu diễn và miền giá trị.
4. **Lập luận và công thức:** giải thích vì sao mỗi bước hợp lệ; không bỏ qua bước then chốt.
5. **Ví dụ tự xây dựng:** cho input, dự đoán, phép tính và cách diễn giải output.
6. **Kiểm chứng và giới hạn:** kiểm tra đơn vị, matrix dimensions, trường hợp đặc biệt và phạm vi áp dụng.
7. **Nguồn và câu hỏi mở:** dẫn chương/mục hoặc URL cụ thể; phân biệt nội dung từ nguồn với nhận xét cá nhân.

Không cần kéo dài bài để có vẻ học thuật. Ưu tiên câu ngắn, định nghĩa chính xác và lập luận kiểm tra được. Nếu chưa chứng minh hoặc kiểm chứng một nhận xét, ghi rõ đó là giả thuyết hay câu hỏi.

## Mathematical Notation

- Định nghĩa từng ký hiệu trước hoặc ngay sau công thức; nêu vector/matrix dimensions và đơn vị khi cần.
- Phân biệt scalar, vector và matrix; dùng nhất quán quy ước trong Modern Robotics ở từng bài. Nếu đổi quy ước, giải thích rõ.
- Với transformation hoặc velocity, nêu rõ reference frame và thứ tự các thành phần; không dùng “tọa độ” mà thiếu frame khi có thể gây nhầm.
- Phân biệt position, orientation, pose và configuration; phân biệt path và trajectory. Không dùng chúng thay thế nhau chỉ vì cách dịch gần nghĩa.
- Dùng `$...$` cho công thức nội tuyến và `$$...$$` cho công thức riêng dòng. Giải thích ý nghĩa vật lý sau công thức.

## Sources and Academic Integrity

Chỉ viết ghi chú sau khi tự học. Dẫn nguồn khi sử dụng định nghĩa hoặc kết quả; diễn giải bằng lời của mình, không sao chép bài giảng hay graded assignment solutions. Không biến scaffold, ví dụ có sẵn hoặc danh mục thuật ngữ thành bằng chứng đã hoàn thành bài học. Chỉ công bố kết quả chạy code thực tế.
