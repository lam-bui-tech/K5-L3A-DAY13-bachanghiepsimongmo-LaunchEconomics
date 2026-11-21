# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Đăng Khoa · Người gắn nhãn 2: Bùi Văn Lâm (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 (Khoa) | Nhãn người 2 (Lâm) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = **100%**

## Quy tắc phân biệt cho các ca dễ nhầm lẫn

Nhóm đạt đồng thuận 100% (20/20 ca) ngay trong lần so nhãn đầu tiên. Các quy tắc phân biệt nguyên nhân gốc cốt lõi được thống nhất như sau:

- **Ca 6 và Ca 9 là lỗi Do người dùng (không phải Hệ thống):** Nguyên nhân gốc là khách hàng chủ động chọn sai phân loại hoặc nhập mã sàn TMĐT thay vì mã vận đơn nội bộ; việc trợ lý chưa gợi ý kịp thời là cơ hội cải tiến trải nghiệm người dùng, nằm ở phần hành động khắc phục chứ không thay đổi bản chất gốc của lỗi.
- **Ca 8 và Ca 15 là lỗi Hệ thống (không phải Ngầm):** Lỗi đã biểu hiện trực tiếp ra bên ngoài (trích dẫn sai chính sách nhìn thấy được trên màn hình hoặc nhân viên phát hiện ngay khi kiểm tra ticket), khác với lỗi ngầm là hoàn toàn không ai nhận ra.
- **Ca 18 là lỗi Ngữ cảnh:** Số tiền hoàn 50% được tính toán hoàn toàn chuẩn xác theo đúng chính sách hoàn cước trễ hạn của công ty; lỗi phát sinh do giả định "khách hàng tự hiểu cách tính" không khớp với ngữ cảnh thực tế của khách.
- **Ca 12 là lỗi Ngầm:** Câu trả lời cuối cùng vẫn đúng nghiệp vụ nhưng phát sinh lỗi lặp công cụ khiến chi phí token bị đội lên gấp 3 lần suốt 3 tuần mà không ai phát hiện cho tới khi kiểm tra dữ liệu log.
- **Ca 13 là Giới hạn hệ thống:** Đơn hàng quốc tế nằm ngoài phạm vi xử lý và dữ liệu được cung cấp cho trợ lý; dù trợ lý chuyển tiếp vụ việc vụng về thì nguyên nhân gốc vẫn là giới hạn hệ thống.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Mỗi giải pháp khắc phục đều có phương thức phát hiện đo lường được (event, ngưỡng cảnh báo, tần suất) và một vai trò chịu trách nhiệm cụ thể, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| **9** | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ này vượt quá 2% tổng số yêu cầu trong ngày | Tự động nhận diện định dạng mã sàn TMĐT (Shopee, Lazada, TikTok Shop) và tra cứu tự động sang mã vận đơn nội bộ; nếu không tra được thì hiển thị hướng dẫn kèm hình ảnh trực quan | PM trợ lý hoàn phí |
| **7** | Hệ thống | Đối soát tự động mỗi giờ: phát hiện tin nhắn "đã hoàn tiền" gửi cho khách nhưng không tồn tại bản ghi sổ cái OK cùng `trace_id`; ngưỡng báo động: $\ge 1$ ca | Chỉ gửi thông báo hoàn tiền khi dịch vụ sổ cái trả về HTTP 200 OK; nếu lỗi 503 sau 3 lần retry thì thông báo "hệ thống đang xử lý" và tự động chuyển ticket cho nhân viên | Kỹ sư trưởng agent |
| **18** | Ngữ cảnh | Theo dõi tỷ lệ khách hàng mở lại ticket vì thắc mắc số tiền hoàn mà khi rà soát thấy hệ thống tính đúng chính sách; ngưỡng cảnh báo: $> 3\%$/tuần | Chuẩn hóa mẫu tin nhắn phản hồi: luôn giải thích công thức tính toán chi tiết và minh bạch (ví dụ: *Cước vận chuyển 30.000 đ × 50% hoàn cước trễ hạn = 15.000 đ*) | Trưởng nhóm CSKH |
| **4** | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `thieu_du_lieu_doi_tac`, thống kê định kỳ theo tuần | Giữ nguyên luồng chuyển tiếp nhân viên kèm bản tóm tắt tự động thông tin đơn hàng; loại bỏ hoàn toàn các loại yêu cầu đối tác phức tạp khỏi phạm vi pilot | PM trợ lý hoàn phí |
| **17** | Ngầm | Kiểm toán mẫu ngẫu nhiên 100 đơn hoàn phí mỗi tuần so với bảng giá hiện hành; ngưỡng báo động: tỷ lệ lệch tiền $> 1\%$ số đơn | Thiết lập cơ chế tự động xóa bộ nhớ đệm (cache) khi ban hành bảng giá mới; bắt buộc ghi nhận phiên bản bảng giá áp dụng vào thuộc tính trace | Kế toán trưởng |
