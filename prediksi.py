import pandas as pd
import numpy as np

# Mengambil data dari file Excel
file_path = "data enginer revisi1.xlsx"  # Ganti dengan path yang sesuai
df = pd.read_excel(file_path)

# Menampilkan data awal
print("Data Awal:")
print(df)

# Mengecek data yang hilang
missing_data = df.isnull().sum()
print("\nData yang Hilang:")
print(missing_data)

# Mengisi data hilang
df_cleaned = df.fillna(method='ffill')  # Mengisi data hilang dengan forward fill

# Mengelompokkan data
grouped_data = df_cleaned.groupby(['Commodity', 'Region'])['Price'].mean().reset_index()

# Menyimpan data yang telah dikelompokkan ke CSV
grouped_data.to_csv('data_kelompok.csv', index=False)
print("\nData setelah Pengelompokkan:")
print(grouped_data)

# Simulasi hasil prediksi (ganti dengan model yang sesungguhnya)
predicted_data = {
    'Index': np.arange(len(grouped_data)),
    'ActualPrice': grouped_data['Price'],
    'PredictedPrice': grouped_data['Price'] * np.random.uniform(0.9, 1.1, size=len(grouped_data))  # Simulasi prediksi
}

# Membuat DataFrame untuk hasil prediksi
predicted_df = pd.DataFrame(predicted_data)

# Menyimpan hasil prediksi ke file TXT
predicted_df.to_csv('prediksi_lstm.txt', index=False)

# Menampilkan hasil prediksi
print("\nHasil Prediksi:")
print(predicted_df)

# Menghitung Mean Squared Error sebagai contoh
mse = np.mean((predicted_df['ActualPrice'] - predicted_df['PredictedPrice']) ** 2)
print("\nMean Squared Error:", mse)
