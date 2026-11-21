# Bảng chi phí · Nhiệm vụ A và B

Phần A được tái tính từ `src/logix_runs.csv` và `src/logix_requests.csv` bằng PowerShell (`Import-Csv`, `Group-Object`, `Measure-Object -Sum`), theo [công thức của lab](../../docs/du_lieu_va_cong_thuc.md) và đối chiếu [bảng nghiệm thu A1–A4](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Ghép theo `request_id`. Giữ số gốc khi tính, chỉ làm tròn khi trình bày. Mọi con số tính từ cột `_simulated` ghi nhãn `[simulated]`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | **1,20 lần** = (1 − 0,2²) / 0,8 |
| Số lần chạy trung bình, chạy đến khi đúng | **1,25 lần** = 1 / 0,8 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | **1,25×** = [(1 − 0,2³) / 0,8] / (1 − 0,2³) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, (26 × token vào + 130 × token ra) / 1.000, cộng mọi lần chạy | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lượt gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | `attempt > 1`, tổng token + tool đã tính trong hai dòng trên | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`, 890 phút × 2.000 đ | [simulated] |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`, 1.132 phút × 2.000 đ | [simulated] |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | [simulated] |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đếm từ trace |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí / 978 việc thành công | [simulated] |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585,132 đ / 1.200 yêu cầu | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu (4.472 / 274,7) [simulated]. Cả hai cùng tính bằng đồng, nhưng mẫu số lần lượt là 978 việc thành công và 1.200 yêu cầu. Nếu cùng chia cho 1.200 yêu cầu thì chi phí là 3.644,7 đ/yêu cầu, gấp **13,27 lần** hoá đơn [simulated].
- **Làm lại** lớn nhất, 2.264.000 đ, chiếm **51,8%** [simulated]. Xem lại là 1.780.000 đ, chiếm **40,7%** [simulated]. Cả hai chiếm **92,5%** trên tổng chi phí 4.373.585,132 đ, gồm cả token và tool [simulated].

## A3 · Tách theo loại yêu cầu

Tỉ lệ thành công = số yêu cầu có `ket_qua == 'thanh_cong'` / số yêu cầu cùng loại. Số lần chạy trung bình = số dòng run / số yêu cầu cùng loại. Chi phí mỗi việc thành công = tổng chi phí cùng loại theo A2 / số việc thành công, rồi chia cho 12.000 đ để ra tỷ số.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% (783/824) | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% (117/158) | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% (41/150) | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% (37/68) | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

- `quoc_te` không đáng xử lý trong phạm vi pilot vì chỉ thành công **27,3%** và tốn **22.515 đ/việc thành công**, bằng **1,88×** mốc 12.000 đ [simulated]. Hướng dẫn ưu tiên hai nhóm có biên tiết kiệm và tỷ lệ thành công cao hơn. `doi_tac` vẫn dưới mốc ở **0,85×** [simulated], nhưng chỉ thành công **54,4%** và có điều khoản riêng nên chưa được ưu tiên.
- Với `quoc_te`, tỷ lệ `status == 'ok'` trong số lượt chạy ở từng lần là **45/150 = 30,0%**, **12/105 = 11,4%**, **2/93 = 2,2%**. Theo `ket_qua` và `so_lan_chay`, 32 việc thành công ở lần 1, thêm 9 ở lần 2 và thêm 0 ở lần 3.
- Lần 2 phát sinh khoảng **23.917 đ** token + tool (18.427 + 5.490), tương đương khoảng **2.657 đ** tiền máy mỗi việc thành công bổ sung. Lần 3 phát sinh khoảng **22.302 đ** (17.667 + 4.635) mà không thêm việc thành công. Trace cho biết tiền máy phát sinh, còn phút nhân viên chỉ ghi ở cấp yêu cầu nên chưa xác định được chi phí biên đầy đủ nếu dừng sớm.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Dùng chi phí biến đổi trong đúng phạm vi pilot là **3.072.513,274 / 900 = 3.413,9036 đ/việc thành công** [simulated]. Theo quy ước nghiệm thu, 45.000 và 22.500 là khối lượng yêu cầu toàn hệ thống trước khi lọc. Giữ nguyên cơ cấu và kết quả của mẫu ở cả hai quy mô, nên số việc thành công trong phạm vi pilot bằng khối lượng × (982/1.200) × (900/982) = khối lượng × **75%**.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Cả hai quy mô vẫn dưới **12.000 đ/việc**. Khi số việc thành công giảm một nửa, cùng **40.000.000 đ/tháng** chia cho ít việc hơn nên chi phí cố định mỗi việc tăng gấp đôi. Tổng mỗi việc tính bằng 40.000.000 đ / số việc thành công rồi cộng chi phí biến đổi chưa làm tròn.
- Nếu 45.000 và 22.500 chỉ đếm yêu cầu đã lọc vào pilot, tỷ lệ phù hợp là **900/982 = 91,65%**. Khi đó dự kiến khoảng **41.242** và **20.621** việc thành công, chi phí cố định lần lượt **970 đ** và **1.940 đ/việc**, tổng khoảng **4.384 đ (0,37×)** và **5.354 đ (0,45×)** [simulated]. Chênh lệch với mốc nghiệm thu đến từ mẫu số khối lượng.

## B1 · Đổi từng yếu tố

Tái tính từ hai CSV trong `src/` bằng `mo_hinh` của nhánh Thu (`3123d5d`) trong bản sao tạm. Mốc A2 là **4.472 đ/việc thành công** [simulated]. Tính thay đổi bằng (chi phí mỗi việc thành công của kịch bản / chi phí mỗi việc thành công gốc − 1) × 100% trên số chưa làm tròn. Với giới hạn chạy, bỏ lượt vượt giới hạn, chuyển yêu cầu tương ứng cho nhân viên và đặt phút xem lại/làm lại của trợ lý về 0 cho các yêu cầu đó.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% [simulated] |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% [simulated] |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% [simulated] |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% [simulated] |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% [simulated] |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% [simulated] |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% [simulated] |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% [simulated] |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% [simulated] |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi cho **6.543 đ/việc thành công (+46,3%)** [simulated]. Số việc thành công giữ nguyên, nên hai mức tăng chi phí cộng lại (+5,6% và +40,7% sau làm tròn) [simulated].
- Xếp theo độ lớn phần trăm thay đổi trong các kịch bản B1, ba yếu tố ảnh hưởng mạnh nhất là **1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)** [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống cho 1.200 yêu cầu = tổng chi phí trợ lý + 12.000 đ × (1.200 − số việc thành công), theo quy ước B3 về phần nhân viên làm thay. Ở giới hạn 3 lần, 222 việc chưa thành công gồm 148 ca chuyển nhân viên và 74 ca làm lại. Chia 7.037.585 đ cho 1.200 cho khoảng **5.865 đ/yêu cầu** trước chi phí cố định [simulated], khớp phép so cùng đơn vị ở nhánh Thu.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | **4.111 đ** [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | **6.901.220 đ** [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- **2 lần** có tổng chi phí thấp nhất. So với 1 lần, phần trợ lý tăng khoảng 471.440 đ [simulated] và giảm 85 việc làm thay (1.020.000 đ). Lượt thứ 3 chỉ giảm thêm 12 việc làm thay (144.000 đ) trong khi phần trợ lý tăng khoảng 280.365 đ [simulated]. **1 lần** có chi phí trợ lý trên mỗi việc thành công thấp nhất, **4.111 đ** [simulated], vì phép tính này chỉ lấy chi phí trợ lý chia cho số việc trợ lý hoàn thành.

## B4 · Nếu phải xem lại tất cả

- Trong `noi_dia` + `hang_nang`, tính tiền token/tool của cả 982 yêu cầu (224.513,274 đ), xem lại 5 phút cho mỗi yêu cầu có ít nhất một lượt `ok` (948 yêu cầu), và làm lại 48 ca với giá 2.000 đ/phút. Chia tổng cho 900 việc thành công. Với **9 phút làm lại/ca**, kết quả là **11.743 đ/việc (0,98×)** [simulated]. Với **15,3 phút/ca**, tính được **12.414,79 đ**, làm tròn thành **12.415 đ/việc (1,03×)** [simulated]. Mốc hướng dẫn là **12.414 đ/việc (1,03×)** [simulated].
- Pilot cần đo mức giảm tỉ lệ xem lại vẫn giữ được chất lượng, đồng thời đo và rút ngắn thời gian mỗi lượt. Nếu vẫn xem lại cả 948 yêu cầu có lượt `ok`, ngưỡng hòa vốn là **5,12 phút/lượt** với 9 phút làm lại và **4,80 phút/lượt** với 15,3 phút làm lại [simulated]. Tính ngưỡng bằng (12.000 × 900 − tiền token/tool − tiền làm lại) / (948 × 2.000).
