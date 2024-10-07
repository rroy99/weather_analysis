# Fungsi untuk menampilkan status on cam
def cek_status_on_cam(nama, on_cam):
    if on_cam:
        return f"{nama} sedang on cam!"
    else:
        return f"{nama} belum on cam, nyalakan kamera sekarang!"

# Contoh pemanggilan fungsi
nama_pengguna = "Roy"
status_on_cam = False  # Ganti ke False untuk mencoba kondisi lain

pesan = cek_status_on_cam(nama_pengguna, status_on_cam)
print(pesan)
