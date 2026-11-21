"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
KHOI_LUONG_TOAN_MANG_THANG = 45_000
LOAI_YEU_CAU_PILOT = ('noi_dia', 'hang_nang')


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    xac_suat_thanh_cong = ti_le_thanh_cong(p, k)
    if p == 0:
        return math.inf if k is None else k
    return xac_suat_thanh_cong / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong khoảng [0, 1]')
    if k is not None and k < 0:
        raise ValueError('k phải không âm')
    if k == 0 or p == 0:
        return 0.0
    if k is None or p == 1:
        return 1.0
    # Tính 1 - (1 - p)**k mà vẫn giữ độ chính xác khi p rất nhỏ.
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Bội số của giá một lần chạy, vô hạn nếu xác suất thành công bằng 0."""
    if ti_le_thanh_cong(p, k) == 0:
        return math.inf
    # Chia E[số lần chạy] cho P(thành công) thì P(thành công) triệt tiêu.
    return 1 / p


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí, số thành công và hóa đơn bình quân cho tập yêu cầu.

    Token và tool tính cả lần lỗi. Phút xem lại và làm lại lấy từ cột giả lập.
    Yêu cầu vượt giới hạn chạy được chuyển cho nhân viên, nên loại phút giả lập
    và kết quả của các yêu cầu đó khỏi chi phí và thành công của trợ lý.
    CPS là vô hạn khi không có việc thành công.
    """
    runs = runs.loc[runs['request_id'].isin(reqs['request_id'])]
    reqs_duoc_xu_ly = reqs
    if max_lan_chay is not None:
        runs = runs.loc[runs['attempt'] <= max_lan_chay]
        reqs_duoc_xu_ly = reqs.loc[reqs['so_lan_chay'] <= max_lan_chay]

    token_moi_lan = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tool_moi_lan = runs['tool_calls'] * gia_tool
    token = token_moi_lan.sum()
    tool = tool_moi_lan.sum()
    chay_lai = (token_moi_lan + tool_moi_lan).loc[runs['attempt'] > 1].sum()

    phut_xem_lai = reqs_duoc_xu_ly['phut_xem_lai_simulated'].sum()
    phut_lam_lai = reqs_duoc_xu_ly['phut_lam_lai_simulated'].sum()
    xem_lai = phut_xem_lai * luong_phut * he_so_xem_lai
    lam_lai = phut_lam_lai * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs_duoc_xu_ly['ket_qua'].eq('thanh_cong').sum()

    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.inf,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


# ---------- Nhiệm vụ A3 · Chi phí và kết quả chạy lại theo loại ----------
def in_ket_qua_a3(runs, reqs):
    print('\nA3 · Theo loại yêu cầu')
    print(f'{"Loại":12s} {"Yêu cầu":>8s} {"Thành công":>11s} {"Lần chạy/yêu cầu":>17s}'
          f' {"CPS (đ)":>10s} {"So với 12.000 đ":>16s} [simulated: CPS và so sánh]')
    for loai, reqs_theo_loai in reqs.groupby('loai'):
        ket_qua = mo_hinh(runs, reqs_theo_loai)
        ti_le = ket_qua['thanh_cong'] / len(reqs_theo_loai)
        lan_chay_binh_quan = reqs_theo_loai['so_lan_chay'].mean()
        cps = ket_qua['cps']
        print(f'{loai:12s} {len(reqs_theo_loai):>8,d} {ti_le:>11.1%}'
              f' {lan_chay_binh_quan:>17.2f} {cps:>10,.0f} {cps / BASELINE:>15.2f}×')

    runs_theo_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id',
                               validate='many_to_one')
    ti_le_ok = (
        runs_theo_loai.assign(la_ok=runs_theo_loai['status'].eq('ok'))
        .groupby(['loai', 'attempt'])['la_ok']
        .mean()
        .unstack('attempt')
    )
    print('\nTỉ lệ trace ok theo loại và lần chạy')
    print(ti_le_ok.to_string(na_rep='—', float_format=lambda ti_le: f'{ti_le:.1%}'))


# ---------- Nhiệm vụ A4 · Chi phí cố định trong phạm vi pilot ----------
def in_ket_qua_a4(runs, reqs):
    reqs_pilot = reqs.loc[reqs['loai'].isin(LOAI_YEU_CAU_PILOT)]
    ket_qua = mo_hinh(runs, reqs_pilot)
    thanh_cong = ket_qua['thanh_cong']
    # Lưu lượng tháng là toàn mạng, nên mẫu số gồm cả yêu cầu ngoài phạm vi pilot.
    ti_le_thanh_cong_toan_mang = thanh_cong / len(reqs)

    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    print(f'{thanh_cong:,} việc thành công / {len(reqs_pilot):,} yêu cầu đủ điều kiện, '
          f'trên {len(reqs):,} yêu cầu toàn mạng trong mẫu.')
    print(f'CPS biến đổi: {ket_qua["cps"]:,.0f} đ [simulated]')
    print(f'{"Yêu cầu/tháng":>14s} {"Thành công/tháng":>17s} {"Cố định/việc":>14s}'
          f' {"CPS + cố định":>14s} {"So với 12.000 đ":>16s} [simulated: CPS và so sánh]')
    for khoi_luong in (KHOI_LUONG_TOAN_MANG_THANG, KHOI_LUONG_TOAN_MANG_THANG // 2):
        viec_thanh_cong = khoi_luong * ti_le_thanh_cong_toan_mang
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / viec_thanh_cong if viec_thanh_cong else math.inf
        cps = ket_qua['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:>14,d} {viec_thanh_cong:>17,.0f} {co_dinh_moi_viec:>14,.0f}'
              f' {cps:>14,.0f} {cps / BASELINE:>15.2f}×')


# ---------- Nhiệm vụ B1–B3 · Độ nhạy và chi phí hệ thống ----------
def in_phan_tich_do_nhay(runs, reqs, cps_goc):
    gia_token_gap_doi = {'gia_vao': GIA_VAO * 2, 'gia_ra': GIA_RA * 2}
    kich_ban = {
        'Giá token gấp đôi': gia_token_gap_doi,
        'Giá token giảm một nửa': {'gia_vao': GIA_VAO / 2, 'gia_ra': GIA_RA / 2},
        'Tỉ lệ xem lại gấp đôi': {'he_so_xem_lai': 2},
        'Tỉ lệ xem lại giảm một nửa': {'he_so_xem_lai': 0.5},
        'Số ca làm lại gấp đôi': {'he_so_lam_lai': 2},
        'Số ca làm lại giảm một nửa': {'he_so_lam_lai': 0.5},
        'Lương nhân viên tăng 25%': {'luong_phut': LUONG_PHUT * 1.25},
    }
    theo_gioi_han = {
        gioi_han: mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        for gioi_han in (1, 2, 3)
    }
    cps_theo_kich_ban = {
        ten: mo_hinh(runs, reqs, **tham_so)['cps']
        for ten, tham_so in kich_ban.items()
    }
    cps_theo_kich_ban['Chỉ cho chạy tối đa 2 lần'] = theo_gioi_han[2]['cps']
    cps_theo_kich_ban['Chỉ cho chạy 1 lần'] = theo_gioi_han[1]['cps']

    print(f'\nB1 · Đổi từng yếu tố [simulated, CPS gốc {cps_goc:,.0f} đ]')
    print(f'{"Kịch bản":32s} {"CPS (đ)":>10s} {"Thay đổi":>10s}')
    for ten, cps in cps_theo_kich_ban.items():
        print(f'{ten:32s} {cps:>10,.0f} {cps / cps_goc - 1:>+10.1%}')

    cps_ket_hop = mo_hinh(runs, reqs, he_so_xem_lai=2, **gia_token_gap_doi)['cps']
    kich_ban_tang = (
        'Giá token gấp đôi',
        'Tỉ lệ xem lại gấp đôi',
        'Số ca làm lại gấp đôi',
        'Lương nhân viên tăng 25%',
    )
    xep_hang = sorted(kich_ban_tang, key=cps_theo_kich_ban.__getitem__, reverse=True)
    print('\nB2 · Đổi một cặp và xếp hạng [simulated]')
    print(f'Giá token và xem lại cùng gấp đôi: {cps_ket_hop:,.0f} đ ({cps_ket_hop / cps_goc - 1:+.1%})')
    print('Ba tác động tăng CPS lớn nhất: ' + ' > '.join(xep_hang[:3]))

    print('\nB3 · Chi phí theo giới hạn chạy [simulated: các cột chi phí]')
    print(f'{"Giới hạn":>8s} {"Tổng trợ lý (đ)":>17s} {"Không thành công":>17s}'
          f' {"Cả hệ thống (đ)":>17s} {"CPS (đ)":>10s}')
    for gioi_han, ket_qua in theo_gioi_han.items():
        so_khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        chi_phi_he_thong = ket_qua['tong'] + BASELINE * so_khong_thanh_cong
        print(f'{gioi_han:8d} {ket_qua["tong"]:17,.0f} {so_khong_thanh_cong:17,d}'
              f' {chi_phi_he_thong:17,.0f} {ket_qua["cps"]:10,.0f}')


# ---------- Nhiệm vụ B4 · Kịch bản xem lại 100% ----------
def in_ket_qua_b4(runs, reqs):
    reqs_pilot = reqs.loc[reqs['loai'].isin(LOAI_YEU_CAU_PILOT)]
    ket_qua = mo_hinh(runs, reqs_pilot)
    run_ok_pilot = runs['request_id'].isin(reqs_pilot['request_id']) & runs['status'].eq('ok')
    so_yeu_cau_ok = runs.loc[run_ok_pilot, 'request_id'].nunique()
    so_ca_lam_lai = reqs_pilot['ket_qua'].eq('lam_lai').sum()
    phut_lam_lai_trung_binh = reqs.loc[
        reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'
    ].mean()

    thanh_cong = ket_qua['thanh_cong']
    hoa_don = ket_qua['token'] + ket_qua['tool']
    phut_xem_lai = 5
    tien_xem_lai_moi_phut = so_yeu_cau_ok * LUONG_PHUT
    print('\nB4 · Xem lại 100% gợi ý trong phạm vi pilot [simulated]')
    print(f'{len(reqs_pilot)} yêu cầu, {so_yeu_cau_ok} có trace ok, {so_ca_lam_lai} ca làm lại, '
          f'{thanh_cong} thành công. Token và tool: {hoa_don:,.0f} đ.')
    print(f'{"Kịch bản":18s} {"Phút làm lại/ca":>16s} {"CPS (đ)":>10s}'
          f' {"So với 12.000 đ":>16s} {"Hòa vốn (phút xem lại/ca)":>25s}')
    for ten, phut_lam_lai in (('Giả định đề bài', 9), ('Trung bình CSV', phut_lam_lai_trung_binh)):
        chi_phi_ngoai_xem_lai = hoa_don + so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = chi_phi_ngoai_xem_lai + phut_xem_lai * tien_xem_lai_moi_phut
        cps = tong / thanh_cong
        phut_hoa_von = (BASELINE * thanh_cong - chi_phi_ngoai_xem_lai) / tien_xem_lai_moi_phut
        print(f'{ten:18s} {phut_lam_lai:16.1f} {cps:10,.0f} {cps / BASELINE:15.2f}×'
              f' {phut_hoa_von:25.1f}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        so_le = 2 if ten == 'hoa_don_moi_yc' else 0
        nhan = ' [simulated]' if ten in {'xem_lai', 'lam_lai', 'tong', 'cps'} else ''
        print(f'{ten:15s} {gia_tri:>14,.{so_le}f}{nhan}')
    in_ket_qua_a3(runs, reqs)
    in_ket_qua_a4(runs, reqs)
    in_phan_tich_do_nhay(runs, reqs, ket_qua['cps'])
    in_ket_qua_b4(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
