# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `(dong_trong_24h == 1) & (mo_lai_trong_7_ngay == 0)` chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1` chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được nhân viên mở bằng trợ lý | Số yêu cầu nhóm can thiệp có ít nhất một event `agent_suggestion_shown` chia tổng yêu cầu nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai số tiền qua kiểm toán mẫu hằng tuần | Số đơn phát hiện sai lệch số tiền từ event `audit_sample_checked` chia tổng số đơn kiểm toán mẫu hằng tuần | Không cần tính |

*Lưu ý:* Chỉ số trong đợt chạy thử là 82,83%, không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Hệ thống ghi nhận 10 event telemetry thời gian thực, tất cả đều có trường `trace_id` để liên kết xuyên suốt hành trình xử lý:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Trợ lý hoàn phí | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy agent (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên xác nhận xem lại |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn thành làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý hoàn phí | `reason`, `tom_tat`, `trace_id` | Khi chuyển ca cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `duration_minutes`, `trace_id` | Khi đóng ticket yêu cầu |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại ticket trong 7 ngày |
| `audit_sample_checked` | Kế toán trưởng | `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Định kỳ kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:**
- Chỉ số chính: Đo từ thời điểm giữa `refund_request_created` và `ticket_closed` ($\le 24$h) và không xuất hiện `ticket_reopened` trong vòng 7 ngày sau đó cùng `trace_id`.
- Chỉ số dùng: Tính từ tỷ lệ các bản ghi `staff_review_decision` có giá trị `sua` hoặc `bo` trên tổng số event `staff_review_decision`.
- Chỉ số an toàn: Đếm số event `ticket_reopened` có `reopened_at - closed_at <= 7 days` chia tổng số event `ticket_closed`.
- Chỉ số dùng tự đề xuất: Tỷ lệ các yêu cầu có event `agent_suggestion_shown` trong nhóm có `arm == 'intervention'`.
- Chỉ số an toàn tự đề xuất: Tỷ lệ các bản ghi `audit_sample_checked` có `lech_tien == true`.

## E2 · Rủi ro kinh tế

Các rủi ro kinh tế lớn được trích xuất từ bảng độ nhạy (`bang_chi_phi.md`):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng +51,8%, lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp phạm vi về riêng noi_dia, trích xuất và rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí tăng vọt lên 11.743 đ (0,98× của 12.000 đ) hoặc 12.414 đ (1,03×) [simulated], triệt tiêu hiệu quả kinh tế | Tỉ lệ yêu cầu được xem lại vẫn > 50% ở cuối bước rollout 0.25 | Kích hoạt lộ trình giảm xem lại theo bậc khi tỉ lệ sửa+bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng bị đội lên: +1.185 đ/việc ở mức 45.000 yc/tháng, tăng lên +2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Số việc thành công thực tế theo tuần < 50% kế hoạch pilot | Tạm hoãn mở rộng pilot, đàm phán lại hợp đồng chi phí cố định với đơn vị cung cấp giải pháp | PM trợ lý hoàn phí |
