# Definisi class PenggunaOnCam
class PenggunaOnCam:
    def __init__(self, nama, status_on_cam=False):
        self.nama = nama
        self.status_on_cam = status_on_cam
    
    # Method untuk mengaktifkan on cam
    def nyalakan_kamera(self):
        self.status_on_cam = True
        print(f"{self.nama} telah menyalakan kamera!")
    
    # Method untuk mematikan on cam
    def matikan_kamera(self):
        self.status_on_cam = False
        print(f"{self.nama} telah mematikan kamera!")
    
    # Method untuk menampilkan status on cam
    def cek_status(self):
        if self.status_on_cam:
            print(f"{self.nama} sedang on cam.")
        else:
            print(f"{self.nama} belum on cam.")

# Contoh penggunaan class
pengguna1 = PenggunaOnCam("Roy")
pengguna2 = PenggunaOnCam("Robin", status_on_cam=True)

# Mengecek status pengguna
pengguna1.cek_status()  # Output: Roy belum on cam.
pengguna2.cek_status()  # Output: Robin sedang on cam.

# Mengubah status pengguna1 menjadi on cam
pengguna1.nyalakan_kamera()  # Output: Roy telah menyalakan kamera!
pengguna1.cek_status()        # Output: Roy sedang on cam.
