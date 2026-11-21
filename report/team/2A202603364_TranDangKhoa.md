# Báo cáo cá nhân · Trần Đăng Khoa · 2A202603364

## 1. Thông tin thành viên

- Họ tên: Trần Đăng Khoa
- MSSV: 2A202603364
- Email: 26ai.khoatd2@vinuni.edu.vn
- Vai trò: Người kiểm số & Báo cáo, Gắn nhãn 1

## 2. Phần việc phụ trách

Tôi phụ trách kiểm định số liệu độc lập từ hai file CSV gốc (`logix_runs.csv` và `logix_requests.csv`), đối chiếu kết quả với các công thức của lab và hoàn thiện báo cáo [bang_chi_phi.md](bang_chi_phi.md) (Nhiệm vụ A và B). Đồng thời, tôi tham gia gắn nhãn độc lập 20 ca lỗi ở CP3 (Người gắn nhãn 1) để xây dựng bảng kiểm soát chất lượng dịch vụ trong [bang_loi.md](bang_loi.md).

## 3. Đóng góp cụ thể

- **Nhiệm vụ A (CP1):** Tái tính toán độc lập bằng công cụ bảng tính/PowerShell các chỉ số A1–A4 từ dữ liệu trace thô, xác nhận khớp 100% với ba phép thử đáp án biết trước (1,20 · 1,25 · 1,25) và CPS gốc là 4.472 đ [simulated]. Phân tích chi phí cố định 40 triệu đ/tháng cho phạm vi nội địa và hàng nặng ở hai mức quy mô lưu lượng.
- **Nhiệm vụ B (CP2):** Thẩm định kết quả 9 kịch bản độ nhạy B1, xác nhận tính tuyến tính của mô hình ở kịch bản B2 (token x2 + xem lại x2 = +46,3% [simulated]). Phân tích bài toán tối ưu chi phí toàn hệ thống ở B3, chỉ ra giới hạn 2 lần chạy là tối ưu cho công ty (6.901.220 đ [simulated]). Cảnh báo bẫy chi phí xem lại 100% ở B4 (vọt lên 11.743–12.415 đ [simulated]).
- **Nhiệm vụ C (CP3):** Đóng vai trò Người gắn nhãn 1, tiến hành gắn nhãn độc lập 20 ca lỗi theo 5 nhóm của Google PAIR trong 8 phút không trao đổi, đối chiếu với Người gắn nhãn 2 đạt tỷ lệ đồng thuận 100% (20/20 ca).

## 4. Bằng chứng

- Các commit hoàn thành báo cáo chi phí và độ nhạy trên nhánh `dangkhoa`: Commit `c146915` (Báo cáo A1–A4) và Commit `008909d` (Báo cáo độ nhạy B1–B4).
- File báo cáo [bang_chi_phi.md](bang_chi_phi.md) và bảng lỗi [bang_loi.md](bang_loi.md).

## 5. Công cụ AI đã dùng

- **Trợ lý AI:** Claude Code và Antigravity.
- **Mục đích:** Hỗ trợ kiểm tra cú pháp công thức xác suất, rà soát tính hợp lý của các kịch bản độ nhạy và đối chiếu định nghĩa lỗi của Google PAIR.
- **Tự kiểm tra:** Tự tay viết lệnh tổng hợp dữ liệu trực tiếp từ file CSV thô để kiểm chứng độc lập với mã nguồn Python của bạn Thư, đảm bảo sai số không vượt quá 2%.

## 6. Tự đánh giá

- Hoàn thành đầy đủ trách nhiệm của Người kiểm số và Người gắn nhãn 1, đảm bảo tính liêm chính và độ chính xác của mọi số liệu báo cáo trước khi trình Hội đồng Gate 2a.
