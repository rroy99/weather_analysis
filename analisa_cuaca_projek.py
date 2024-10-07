import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API key 
API_KEY = '5420b6058393d8f1bf8de220869f344b'

# Daftar kota 
cities = [
    "Jakarta, Indonesia",
    "Kuala Lumpur, Malaysia",
    "Singapore, Singapore",
    "Bangkok, Thailand"
]

# mengambil data cuaca dari API
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Ambil data cuaca untuk setiap kota
weather_data = []
for city in cities:
    data = get_weather_data(city)
    if data.get("main"):  # Cek jika data 'main' ada
        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
        weather_data.append(weather_info)

# Simpan data ke dalam file CSV
df = pd.DataFrame(weather_data)
df.to_csv("weather_data.csv", index=False)

print("Data cuaca berhasil disimpan ke dalam weather_data.csv")

# Baca data dari CSV
df = pd.read_csv("weather_data.csv")

# Rata-rata suhu dari semua kota
average_temp = df["temperature"].mean()
print(f"Rata-rata suhu dari semua kota: {average_temp:.2f}°C")

# Kota dengan suhu tertinggi dan terendah
max_temp_city = df.loc[df["temperature"].idxmax()]["city"]
min_temp_city = df.loc[df["temperature"].idxmin()]["city"]

print(f"Kota dengan suhu tertinggi: {max_temp_city}")
print(f"Kota dengan suhu terendah: {min_temp_city}")

# Analisis cuaca yang paling sering muncul
most_common_weather = df["weather"].mode()[0]
print(f"Pola cuaca yang paling sering muncul: {most_common_weather}")

# terjemahan kondisi cuaca
weather_translation = {
    "clear sky": "langit cerah",
    "few clouds": "beberapa awan",
    "scattered clouds": "awan tersebar",
    "broken clouds": "awan pecah",
    "overcast clouds": "awan mendung",
    "shower rain": "hujan rintik",
    "rain": "hujan",
    "light rain": "hujan ringan",
    "heavy intensity rain": "hujan deras",
    "light intensity shower rain": "hujan rintik ringan",
    "thunderstorm": "badai petir",
    "snow": "salju",
    "mist": "kabut",
    "smoke": "asap",
    "haze": "kabut asap",
    "sand": "pasir",
    "dust": "debuan",
    "fog": "kabut tebal",
    "ash": "abu",
    "squall": "angin kencang",
    "tornado": "tornado"
}

# Ganti kondisi cuaca dengan bahasa Indonesia
df['weather'] = df['weather'].replace(weather_translation)

# Visualisasi
plt.figure(figsize=(14, 12))

# Subplot untuk distribusi suhu
plt.subplot(3, 1, 1)
sns.set_palette("husl")
sns.barplot(x="city", y="temperature", data=df, errorbar=None)  
plt.title("Laporan Perkiraan Cuaca: Distribusi Suhu di Berbagai Kota", fontsize=18, fontweight='bold', pad=15)
plt.xlabel("Kota", fontsize=10)
plt.ylabel("Suhu (°C)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menambah padding manual ke label sumbu x
labels = plt.gca().get_xticklabels()
for label in labels:
    label.set_y(-0.05) 

# Subplot untuk distribusi pola cuaca
plt.subplot(3, 1, 2)
sns.set_palette("pastel")
sns.countplot(x="weather", data=df, order=df["weather"].value_counts().index)
plt.title("Laporan Perkiraan Cuaca: Distribusi Pola Cuaca", fontsize=18, fontweight='bold', pad=15)
plt.xlabel("Kondisi Cuaca", fontsize=10)
plt.ylabel("Frekuensi", fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menambah padding manual ke label sumbu x
labels = plt.gca().get_xticklabels()
for label in labels:
    label.set_y(-0.05)  

# Subplot untuk kota dengan suhu tertinggi dan terendah
plt.subplot(3, 1, 3)
plt.bar([max_temp_city, min_temp_city], [df["temperature"].max(), df["temperature"].min()], color=['orange', 'blue'])
plt.title("Kota dengan Suhu Tertinggi dan Terendah", fontsize=18, fontweight='bold', pad=15)
plt.xlabel("Kota", fontsize=10)
plt.ylabel("Suhu (°C)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menambah padding manual ke label sumbu x
labels = plt.gca().get_xticklabels()
for label in labels:
    label.set_y(-0.05)  

# Menyesuaikan tata letak agar lebih rapi
plt.tight_layout(pad=5.0)
plt.show()
