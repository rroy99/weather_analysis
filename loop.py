# Jumlah perulangan
jumlah = 10

for i in range(1, jumlah + 1):
    if i % 3 == 0:  # Setiap 3 iterasi
        print(f"Perulangan {i}: Ayo semangat, kamu pasti bisa on cam!")
    elif i % 5 == 0:  # Setiap 5 iterasi
        print(f"Perulangan {i}: Jangan lupa nyalakan kamera!")
    else:
        print(f"Perulangan {i}: Saya akan ikut on cam!")
