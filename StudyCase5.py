from datetime import datetime

def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

    total_biaya = tarif * lama_menginap
    return total_biaya

jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
tanggal_checkin = input("Masukkan tanggal check-in (DD-MM-YYYY): ")
tanggal_checkout = input("Masukkan tanggal check-out (DD-MM-YYYY): ")

tanggal_masuk = datetime.strptime(tanggal_checkin, "%d-%m-%Y")
tanggal_keluar = datetime.strptime(tanggal_checkout, "%d-%m-%Y")

lama_menginap = (tanggal_keluar - tanggal_masuk).days
total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

print("===== DATA PEMESANAN HOTEL =====")
print("Jenis kamar        :", jenis_kamar)
print("Tanggal check-in   :", tanggal_checkin)
print("Tanggal check-out  :", tanggal_checkout)
print("Lama menginap      :", lama_menginap, "malam")
print("Total biaya        : Rp", total_biaya)