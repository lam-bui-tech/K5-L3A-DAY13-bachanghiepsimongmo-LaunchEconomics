# Báo cáo cá nhân · Nguyễn Huy Thứ · 2A202603356

## 1. Thông tin thành viên

- Họ tên: Nguyễn Huy Thứ
- MSSV: 2A202603356
- Email: 26ai.thunh@vinuni.edu.vn
- Vai trò: Phụ trách viết code và tính chi phí cho CP1–CP2.

## 2. Phần việc phụ trách

Tôi phụ trách triển khai A1–A4 và B1–B4 trong `src/lab13.py`, chạy trên 2 CSV của lab và điền kết quả vào bảng chi phí nhóm. Tôi cũng chuẩn bị kế hoạch triển khai, công thức tính tay và số liệu tham khảo để nhóm thảo luận pilot.

## 3. Đóng góp cụ thể

- **CP1 · A1–A4.** Hoàn thành ba phép thử A1 với kết quả **1,20 · 1,25 · 1,25**. Cộng chi phí của 1.624 lượt chạy và thời gian xử lý của nhân viên, rồi chia cho 978 yêu cầu thành công để ra CPS **4.472 đ** `simulated`. Tách chi phí theo bốn loại yêu cầu. Trong phạm vi nội địa và hàng nặng, CPS gồm cố định là **4.599 đ** ở 45.000 yêu cầu/tháng và **5.784 đ** ở 22.500 yêu cầu/tháng `simulated`.
- **CP2 · B1–B4.** Chạy 9 kịch bản đơn và 1 kịch bản kết hợp. Làm lại gấp đôi làm CPS tăng **51,8%**. Giới hạn 2 lượt cho chi phí hệ thống thấp nhất, **6.901.220 đ** trên 1.200 yêu cầu. Xem lại 100% gợi ý đưa CPS lên **11.743–12.415 đ**, tùy thời gian làm lại. Các kết quả chi phí là `simulated`. [Bảng chi phí](bang_chi_phi.md)
- **Tài liệu hỗ trợ.** Chuẩn bị hướng dẫn tính tay có công thức, nguồn biến và ví dụ LogiX-VN. Tính thử cỡ mẫu cho phương án pilot nội bộ với 20 nhân viên và 5.980 yêu cầu mỗi nhánh ở mức chênh 6 điểm phần trăm.

## 4. Bằng chứng

- CP1 và CP2 đã được đẩy lên nhánh `2A202603356_NguyenHuyThu`. Mỗi commit cập nhật code và bảng chi phí của checkpoint tương ứng. [CP1 · `3123d5d`](https://github.com/lam-bui-tech/K5-L3A-DAY13-bachanghiepsimongmo-LaunchEconomics/commit/3123d5df85f7c69ad9a76ab2831fa3ad3912a62e) · [CP2 · `5263f80`](https://github.com/lam-bui-tech/K5-L3A-DAY13-bachanghiepsimongmo-LaunchEconomics/commit/5263f80814693aaea615c26fc3ab08bc985f031c)
- Chạy `python -X utf8 lab13.py` trong `src/` để tái lập ba phép thử A1 và các bảng A2–A4, B1–B4. [Code](../../src/lab13.py) · [Hai CSV và công thức](../../docs/du_lieu_va_cong_thuc.md)

## 5. Công cụ AI đã dùng

Tôi dùng ChatGPT Codex để đọc đề, giải thích công thức, hỗ trợ triển khai code và soạn tài liệu. Kết quả được kiểm tra bằng ba phép thử A1, bằng cách chạy `lab13.py` và bằng phép tổng hợp độc lập trực tiếp từ hai CSV. Ví dụ, A2 có `4.373.585,132 / 978 ≈ 4.472 đ` `simulated`. Ở B1, mức giảm khi chia đôi chi phí xem lại bằng đúng một nửa mức tăng khi gấp đôi, trước khi làm tròn.

## 6. Tự đánh giá

Từ B3, tôi rút ra rằng cần theo dõi cả CPS của trợ lý và chi phí hệ thống. Giới hạn **1 lượt** cho CPS **4.111 đ** `simulated` nhưng để lại thêm **85 yêu cầu** cho nhân viên so với giới hạn **2 lượt**. Điểm cần kiểm chứng trong pilot là số phút xem lại và làm lại đo thực tế. Khi xem lại 100% gợi ý và làm lại trung bình khoảng **15,3 phút/ca** theo CSV, CPS ước tính **12.415 đ** `simulated`, vượt mốc làm tay 12.000 đ/yêu cầu.
