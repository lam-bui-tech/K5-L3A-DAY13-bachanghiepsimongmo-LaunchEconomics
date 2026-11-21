# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25× giá một lần chạy |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | `logix_runs.csv`, mọi lần chạy | đo từ trace |
| Tool | 84.000 đ | 5.600 lần gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | Token và tool với `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated`, 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated`, 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` trong `logix_requests.csv` | đếm từ CSV |
| Chi phí mỗi việc thành công | 4.472 đ | Tổng chi phí / 978 việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 đ | (Token + tool) / 1.200 yêu cầu | đo từ trace và số yêu cầu |

- Chi phí mỗi việc thành công gấp **16,3 lần** hóa đơn bình quân `simulated`.
- **Làm lại** chiếm tỷ trọng lớn nhất, **51,8%** trên tổng chi phí `simulated`.
- Để so cùng đơn vị với 12.000 đ/yêu cầu làm tay, cộng chi phí nhân viên xử lý 222 yêu cầu chưa thành công theo quy ước B3. Chi phí hệ thống là `(4.373.585 + 222 × 12.000) / 1.200 ≈ 5.865 đ/yêu cầu` `simulated`, trước chi phí cố định.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công `simulated` | So với 12.000 đ `simulated` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Để nhân viên xử lý `quoc_te`: thành công **27,3%**, CPS **22.515 đ** `simulated`. Chạy lần 3 chỉ có thêm **2 trace `ok` trên 93 lượt**, tương đương **2,2%**.
- Giới hạn pilot ở `noi_dia` và `hang_nang`. `doi_tac` có điều khoản riêng và CPS **10.215 đ** `simulated`, sát mốc 12.000 đ.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong mẫu toàn mạng có 1.200 yêu cầu, 982 thuộc phạm vi pilot và 900 thành công trong phạm vi đó. Dự phóng số việc thành công từ lưu lượng toàn mạng bằng tỷ lệ **900/1.200**. CPS trước cố định là **3.414 đ** `simulated`. Phân bổ **40 triệu đ/tháng** cho số việc thành công dự phóng.

| Khối lượng toàn mạng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định `simulated` | So với 12.000 đ `simulated` |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- CPS gồm cố định vẫn dưới mốc 12.000 đ ở cả hai mức. Khi lưu lượng giảm một nửa, cố định tăng từ **1.185** lên **2.370 đ/việc** và CPS lên **5.784 đ** `simulated`.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...
