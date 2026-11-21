# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Ba chàng hiệp sĩ mộng mơ (L3A) - 2A202603400 (Bùi Văn Lâm), 2A202603356 (Nguyễn Huy Thư), 2A202603364 (Trần Đăng Khoa)
- Nhóm được chấm: Nhóm 4people (L3A) - Repo: Dovanngoc05/K5-L3A-DAY13-4people-LaunchEconomics

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 6 / 10 | Phân tích sâu các con số bất lợi (CPS 4.471,97 đ gấp 16.3x tiền điện; rủi ro đội chi phí 83,8 tr/tháng; Power cụm chỉ đạt 0.64). Tuy nhiên, đề xuất "Go có điều kiện" bị mâu thuẫn số liệu: Mục 3 hồ sơ ghi CPS hệ thống 5.864,65 đ (kịch bản 3 lần) thay vì số tối ưu 5.751,02 đ (kịch bản 2 lần ở B3); đồng thời đề xuất Go khi Mục 5 thừa nhận "Chưa" đạt tỷ lệ đồng thuận gắn nhãn ≥ 80%. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 / 10 | Gắn nhãn [simulated] đầy đủ ở 100% các bảng ước tính. Thu hẹp phạm vi pilot rất rõ nét: chỉ áp dụng cho nhóm tra cứu trạng thái đơn/SLA tiêu chuẩn, loại trừ hoàn toàn nhóm khiếu nại đền bù/pháp lý dựa trên bằng chứng độ trễ P95 (5.8s) và CPS mô hình. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 6 / 10 | Thiết kế Cluster RCT xuất sắc: n = 859 ca/nhánh (k=10 kho, m=86, ICC=0.03), có nhóm đối chứng song song; luật dừng có ngưỡng rõ (escalate > 15%, ngân sách vượt > 15%). Tuy nhiên, người có quyền dừng trong hồ sơ giao cho vai trò bài tập học tập ("Người kiểm số", "Đội kỹ thuật") thay vì chức danh quản trị doanh nghiệp (Lead AI Engineer, COO); đề xuất pilot vẫn ghi "dự thảo chưa phải quyết định cuối". |
| **Tổng** | | | | **22 / 30** | Điểm số phản ánh năng lực toán học xuất sắc nhưng hồ sơ thiếu điều kiện tiên quyết CP3 và thẩm quyền quản trị. |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** 
1. Năng lực tính toán tài chính, phân tích độ trễ và mô hình hóa A/B testing (Cluster RCT) của nhóm đạt độ chuẩn xác rất cao, có tính phản biện và nhận diện rõ rủi ro kinh tế (vượt chi phí 83,8 triệu/tháng).
2. Tuy nhiên, nhóm chưa hoàn thành nhiệm vụ tiên quyết CP3 (Nhiệm vụ C): Bảng lỗi 20 ca mới chỉ có Người 1 gắn nhãn, Người 2 hoàn toàn để trống (`...`), tỷ lệ đồng thuận chưa được tính toán.
3. Hội đồng chỉ chuẩn thuận cho phép chuyển sang giai đoạn Pilot NẾU nhóm đáp ứng 3 điều kiện tiên quyết ràng buộc trong 24 giờ tới:
   - Điều kiện 1: Hoàn thành độc lập nhãn của Người 2 trên 20 ca và chứng minh tỷ lệ đồng thuận đạt ≥ 80%.
   - Điều kiện 2: Chuẩn hóa phân quyền dừng pilot và chịu trách nhiệm trong hồ sơ sang chức danh doanh nghiệp (Kỹ sư trưởng AI, Quản lý Vận hành, Kế toán trưởng).
   - Điều kiện 3: Hiệu chỉnh thống nhất con số chi phí phiên hệ thống tại Mục 3 hồ sơ về đúng mức tối ưu 5.751,02 đ.

**Một câu hỏi cho đội trình:** 
"Tại sao nhóm tự tin đưa ra đề xuất 'Go có điều kiện' trong khi bảng lỗi CP3 mới chỉ có 1 người gắn nhãn và tỷ lệ đồng thuận người 2 vẫn để trống (Mục 5 ghi 'Chưa')? Nếu sau khi gắn nhãn người 2, tỷ lệ đồng thuận dưới 80% và lộ ra thêm lỗi nhận diện sai SLA, nhóm sẽ kích hoạt kịch bản phòng vệ nào để không làm bùng nổ rủi ro 83,8 triệu VND/tháng?"

**Câu trả lời của đội trình (ghi lại tại buổi):** 
*(Ghi nhận trực tiếp phản hồi của nhóm 4people tại phiên bảo vệ Gate 2a)*
