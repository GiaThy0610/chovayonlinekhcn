STV=float(input("NHẬP SỐ TIỀN MUỐN VAY (TRIỆU ĐỒNG): "))
TGV=float(input("NHẬP THỜI GIAN VAY (SỐ NĂM): "))
LSV=float(input("NHẬP LÃI SUẤT CHO VAY (SỐ THẬP PHÂN): "))
TN=float(input("NHẬP THU NHẬP HÀNG THÁNG(TRIỆU ĐỒNG/THÁNG): "))
SNTGD=float(input("NHẬP NGƯỜI TRONG GIA ĐÌNH(sỐ nGƯỜI): "))
CPSH=5
PTMC=float(input("NHẬP SỐ TỐ TIỀN PHẢI TRẢ CHO KHOẢN VAY CŨ (TRIỆU ĐỒNG):"))
PTMM=(STV/(TGV*12))+(STV*(LSV/12))
DTI=(PTMC+PTMM)/(TN-SNTGD*CPSH)
GTTSDB=float(input("NHẬP GIÁ TRỊ TSDB (TRIỆU ĐỒNG):"))
LTV=STV/GTTSDB
print(f"chỉ số DTI là: {DTI*100}%")
print(f"chỉ số LTV là: {LTV*100}%")
if DTI<= 0.7:
  print("ĐƯỢC CHO VAY")
else:
  print("KHÔNG ĐƯỢC CHO VAY")
