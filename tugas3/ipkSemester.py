nilai_Algoritma = float(input("masukan nilai Algoritma :"))
nilai_Perancangan_Objek = float(input("masukan nilai Perancangan Objek :"))
nilai_Kalkulus = float(input("masukan nilai Kalkulus :"))
nilai_Etika_Profesi = float(input("masukan nilai Etika Profesi :"))
nilai_Databases = float(input("masukan nilai Databases :"))
nilai_English = float(input("masukan nilai English :"))

#nilai sks mata kuliah
Algoritma = 3
Perancangan_Objek = 4
Kalkulus = 4
Etika_Profesi = 2
Databases = 3
English = 2

total_sks = Algoritma + Perancangan_Objek + Kalkulus + Etika_Profesi + Databases + English
total_nilai = (nilai_Algoritma * Algoritma) + (nilai_Perancangan_Objek * Perancangan_Objek) + (nilai_Kalkulus * Kalkulus) + (nilai_Etika_Profesi * Etika_Profesi) + (nilai_Databases * Databases) + (nilai_English * English)

#nilai 
ipk = total_nilai / total_sks

print("IPK Anda semester ini adalah :",ipk,"")

