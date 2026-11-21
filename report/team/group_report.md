# Báo cáo nhóm

Báo cáo ngắn tóm tắt kết quả thực hiện Lab 13 (Launch & Economics · Gate 2a). Toàn bộ số liệu chi tiết nằm trong các file hồ sơ thuộc thư mục `report/team/`.

## 1. Thông tin nhóm

- Tên nhóm: Ba Chang Hiep Si Mong Mo
- Lớp: L3A
- Thành viên: Bùi Văn Lâm (Trưởng nhóm), Nguyễn Huy Thư (Coder), Trần Đăng Khoa (Analyst). Chi tiết phân công xem [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ hồ sơ launch v0 toàn diện cho trợ lý hoàn phí của LogiX-VN nhằm bảo vệ trước hội đồng Gate 2a, trả lời 4 câu hỏi cốt lõi:
1. **Có đáng chạy không:** Xây dựng mô hình tính chi phí thực tế cho mỗi việc thành công từ 1.624 lượt chạy trace và 1.200 yêu cầu, chứng minh chi phí agent thực tế gấp 16,3 lần hóa đơn token máy móc.
2. **Nhân viên có dùng không:** Thiết lập bộ 5 chỉ số (chính, dùng, an toàn) và hệ thống 10 event telemetry có `trace_id` để đo lường hành vi thực tế.
3. **Khi hỏng thì sao:** Phân loại 20 ca lỗi theo 5 nhóm nguyên nhân gốc của Google PAIR, đạt đồng thuận 100% và gán giải pháp khắc phục cụ thể cho từng vai trò.
4. **Pilot thiết kế thế nào để ra quyết định:** Thiết kế thử nghiệm đối chứng ngẫu nhiên theo nhân viên (20 đối chứng vs 20 can thiệp), tính toán cỡ mẫu hiệu dụng, chấp nhận đánh đổi thống kê và thiết lập 3 luật dừng 4 vế nghiêm ngặt.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Viết mã nguồn tính toán chi phí theo công thức chuẩn: tử số tính mọi lượt chạy (kể cả lỗi), mẫu số chỉ tính việc thành công. Chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (Phân tích độ nhạy):** Khảo sát 9 kịch bản biến động chi phí, chỉ ra chi phí nhạy cảm nhất với thời gian nhân viên (làm lại và xem lại chiếm 92,5%), không phụ thuộc nhiều vào giá token. Chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi và khắc phục):** Gắn nhãn độc lập 20 ca lỗi, xây dựng ma trận kiểm soát rủi ro cho 5 ca trọng yếu. Chi tiết tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Thiết kế kế hoạch thử nghiệm trong [pilot_plan.yaml](pilot_plan.yaml) với 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ, tích hợp cơ chế rollback 30 phút.
- **Nhiệm vụ E (Chỉ số & Hồ sơ Launch v0):** Hoàn thiện hồ sơ 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md) và đặc tả telemetry tại [chi_so.md](chi_so.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** `4.472 đ` [simulated] (gấp 16,3 lần hóa đơn token+tool `274,7 đ`).
- **So với nhân viên tự làm (12.000 đ):** Bằng `0,37×` tính riêng việc thành công và `0,49×` (`5.865 đ`) tính cho cả hệ thống gồm 148 ca chuyển giao thủ công [simulated].
- **Phạm vi pilot tối ưu:** Thu hẹp về `noi_dia` (0,22×) và `hang_nang` (0,69×); loại bỏ hoàn toàn `quoc_te` (1,88× đắt hơn người) và `doi_tac` (0,85×).
- **Đề xuất cuối cùng:** **Go có điều kiện** kèm 4 điều kiện ràng buộc về kỹ thuật (sửa lỗi sổ cái ca 7, 20), thống kê (chấp nhận MDE 6%), đo lường thực tế (bật telemetry 10 event) và lộ trình hạ tỷ lệ xem lại theo bậc.
- **Kết quả duyệt chéo Gate 2a:** Ghi nhận tại [phieu_cham.md](phieu_cham.md).

## 5. Khó khăn và cách xử lý

- *Giới hạn cỡ mẫu:* Với quy mô 40 nhân viên của LogiX-VN, không thể đạt MDE = 5% ở mức power 0,80 khi phân cụm theo nhân viên. Nhóm đã chủ động minh bạch hóa đánh đổi chấp nhận MDE = 6% ($n = 859$, power $0,64$) để bảo toàn thiết kế phân cụm 20 nhân viên mỗi nhóm, tránh nguy cơ tràn tác động nếu chia theo ticket.
- *Bẫy chi phí xem lại 100%:* Phân tích B4 cho thấy nếu duy trì xem lại 100%, chi phí vọt lên 11.743 đ (0,98×), trợ lý mất toàn bộ lợi thế kinh tế. Nhóm đã đề xuất điều kiện bắt buộc có lộ trình hạ tỷ lệ xem lại theo bậc khi tỷ lệ sửa/bỏ $< 15\%$.

## 6. Tổng hợp đóng góp

- **Bùi Văn Lâm (Trưởng nhóm):** Điều phối chung, xây dựng hồ sơ Launch v0, thiết kế kế hoạch pilot D, đặc tả chỉ số E, gắn nhãn độc lập 20 ca lỗi (Người 2), tổng hợp báo cáo nhóm. (100% trách nhiệm).
- **Nguyễn Huy Thư (Coder):** Xây dựng mã nguồn `src/lab13.py`, hoàn thành các hàm mô hình kinh tế A1–A4, phân tích độ nhạy B1–B4, tính toán cỡ mẫu D1. (100% trách nhiệm).
- **Trần Đăng Khoa (Analyst):** Kiểm định số liệu độc lập, hoàn thiện báo cáo bảng chi phí A1–A4 và độ nhạy B1–B4, gắn nhãn độc lập 20 ca lỗi (Người 1). (100% trách nhiệm).

## 7. Hạn chế và hướng cải thiện

- Dữ liệu thời gian xem lại và làm lại hiện tại là giả lập (`simulated`). Cần thay thế ngay bằng số liệu đo đạc thực tế từ event telemetry sau tuần 1 của pilot.
- Cần hoàn thiện cơ chế đối soát sổ cái bất đồng bộ trước khi mở rộng quy mô.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, "Errors + Graceful Failure".
