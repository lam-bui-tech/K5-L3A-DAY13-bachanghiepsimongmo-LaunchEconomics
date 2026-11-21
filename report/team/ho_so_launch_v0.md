# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: bachanghiepsimongmo · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hóa đơn token+tool (274,7 đ); giờ nhân viên chiếm 92,5% tổng chi phí | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated] | Giả lập | Chuyên viên phân tích chi phí |
| 3 · So với nhân viên tự làm | 0,37× (4.472 đ / 12.000 đ tính riêng việc hoàn thành) hoặc 0,49× (5.865 đ / 12.000 đ tính cả hệ thống gồm 148 ca chuyển nhân viên) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số chính trong đợt chạy thử: 82,83% (994/1.200) · Tỉ lệ bỏ qua gợi ý: 27,12% (48/177) · Tỉ lệ mở lại 7 ngày: 4,25% (51/1.200) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Tỉ lệ đồng thuận nhóm: 100% (20/20 ca); đã lập bảng khắc phục cho 5 ca đại diện 5 loại lỗi (ca 9, 7, 18, 4, 17) kèm cơ chế đo lường cụ thể | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Đơn vị chia theo nhân viên (20 can thiệp vs 20 đối chứng); phạm vi hẹp noi_dia + hang_nang; cỡ mẫu n=859/nhóm (m≥299 yc/người); chấp nhận đánh đổi MDE=6%, power=0,64; 3 luật dừng 4 vế | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Nếu số ca làm lại gấp đôi: chi phí tăng lên 6.787 đ (+51,8%) [simulated]; Nếu xem lại 100%: chi phí tăng lên 11.743 đ (0,98×, mất sạch lợi ích kinh tế) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

**Bốn điều kiện tiên quyết trước khi triển khai pilot:**

1. **Sửa khóa chống trùng và đối soát sổ cái (Ca 7, 20):** Triển khai `idempotency_key` và chỉ xác nhận thành công khi dịch vụ sổ cái phản hồi OK; lỗi 503 phải có cơ chế chuyển giao nhân viên để loại trừ triệt để nguy cơ hoàn trùng tiền.  
   *Người phụ trách:* Kỹ sư trưởng agent · *Ngày kiểm tra:* 2026-11-28.
2. **Ký duyệt văn bản chấp nhận đánh đổi thống kê:** Giám đốc vận hành ký xác nhận chấp thuận mức chênh phát hiện tối thiểu MDE = 6% (thay vì 5%) với statistical power = 0,64 do giới hạn quy mô 40 nhân viên của LogiX-VN.  
   *Người phụ trách:* Giám đốc vận hành LogiX-VN · *Ngày kiểm tra:* 2026-11-30.
3. **Kích hoạt hạ tầng telemetry 10 event có trace_id:** Đảm bảo toàn bộ hành trình yêu cầu được ghi nhận event thời gian thực; thay thế toàn bộ dữ liệu phút xem lại/làm lại giả lập (`simulated`) bằng số liệu đo đạc thực tế sau tuần 1 của pilot.  
   *Người phụ trách:* PM trợ lý hoàn phí · *Ngày kiểm tra:* 2026-12-07.
4. **Thiết lập lộ trình cắt giảm tỷ lệ xem lại theo bậc:** Triển khai cơ chế giảm dần tỷ lệ xem lại từ 100% xuống dưới 30% khi tỷ lệ sửa/bỏ của nhân viên ổn định dưới 15%, ngăn chặn bẫy chi phí xem lại 100% làm triệt tiêu hiệu quả kinh tế của trợ lý.  
   *Người phụ trách:* Trưởng nhóm CSKH · *Ngày kiểm tra:* 2026-12-14.
