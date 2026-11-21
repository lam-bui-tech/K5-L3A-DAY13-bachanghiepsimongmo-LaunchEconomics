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

CPS gốc A2 là **4.472 đ** `simulated`. Phần trăm thay đổi dùng CPS chưa làm tròn.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công `simulated` | Thay đổi `simulated` |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ đầu vào và 260 đ đầu ra cho 1.000 token, giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ đầu vào và 65 đ đầu ra cho 1.000 token | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ trace có `attempt > 2`, chuyển yêu cầu có `so_lan_chay > 2` cho nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Áp dụng cùng quy tắc với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng tăng gấp đôi đưa CPS lên **6.543 đ (+46,3%)** `simulated`. Vì hai khoản cộng độc lập và số thành công giữ nguyên, mức tăng bằng **5,6% + 40,7%**.
- Ba kịch bản làm CPS tăng mạnh nhất `simulated` lần lượt là làm lại gấp đôi **(+51,8%)**, xem lại gấp đôi **(+40,7%)**, lương tăng 25% **(+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống bằng tổng chi phí trợ lý cộng **12.000 đ × số yêu cầu không thành công**, theo quy ước của lab. Các mức dưới đây tính trên 1.200 yêu cầu, trước chi phí cố định.

| Giới hạn | Tổng chi phí trợ lý `simulated` | Số yêu cầu không thành công | Chi phí cả hệ thống `simulated` | Chi phí mỗi việc thành công `simulated` |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | **4.111 đ** |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **2 lần** cho chi phí cả hệ thống thấp nhất, **6.901.220 đ** `simulated`. Giới hạn **1 lần** cho CPS thấp nhất (**4.111 đ** `simulated`) nhưng để lại thêm **85 yêu cầu** cho nhân viên.

## B4 · Nếu phải xem lại tất cả

Trong 982 yêu cầu `noi_dia` và `hang_nang`, có **948 yêu cầu** với ít nhất một trace `ok`, **48 ca làm lại** và **900 việc thành công**. Tính 5 phút xem lại cho mỗi yêu cầu có trace `ok`, cộng phút làm lại và **224.513 đ** tiền token và tool. Mức **15,3 phút** là trung bình từ cột `phut_lam_lai_simulated` trên toàn bộ ca làm lại. Phép tính giữ giá trị chưa làm tròn.

| Phút làm lại/ca | Chi phí mỗi việc thành công `simulated` | So với 12.000 đ `simulated` | Thời gian xem lại tối đa để CPS hòa vốn `simulated` |
| --- | ---: | ---: | ---: |
| 9 phút theo đề bài | 11.743 đ | 0,98× | 5,1 phút/ca |
| 15,3 phút theo CSV `simulated` | 12.415 đ | 1,03× | 4,8 phút/ca |

- Xem lại 100% đưa CPS từ sát mốc lên vượt **12.000 đ** khi thời gian làm lại tăng từ **9** lên **15,3 phút/ca** `simulated`.
- Pilot cần đo phút xem lại, phút làm lại và tỷ lệ gợi ý cần xem lại để xác định mức giảm an toàn. Với kịch bản làm lại **15,3 phút/ca**, thời gian xem lại phải dưới khoảng **4,8 phút/ca** để CPS thấp hơn mốc 12.000 đ `simulated`, trước cố định và xử lý thay.
