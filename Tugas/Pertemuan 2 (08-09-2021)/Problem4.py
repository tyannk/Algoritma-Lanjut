# Tyan Nur Khollis
# 41520010057

TotalBeras = 86 #KG
Beras1Plasik = 6 #KG
JumlahPlastikYangDiisiberas = 1/4 #dari jumlah plastik milik Sidik

PlastikYangDigunakan = int(TotalBeras/Beras1Plasik)
SisaBeras = TotalBeras % Beras1Plasik

print("Sisa beras adalah :", SisaBeras,"KG")
print("Jumlah plastik yang diisi beras adalah :",PlastikYangDigunakan)

PlastikYangDimiliki = int (PlastikYangDigunakan / JumlahPlastikYangDiisiberas)
print("Jumlah plastik yang dimiliki sidik adalah :", PlastikYangDimiliki)
