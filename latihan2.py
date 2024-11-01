# Program untuk menghitung total laba selama 8 bulan

# Inisialisasi variabel
modal = 100000000  # Modal awal 100 juta
laba = [0] * 8     # List untuk menyimpan laba tiap bulan
total_laba = 0     # Variabel untuk total laba

# Perhitungan laba per bulan
for i in range(8):
    if i < 2:  # Bulan 1 dan 2
        laba[i] = 0
    elif i < 4:  # Bulan 3 dan 4
        laba[i] = modal * 0.01  # Laba 1%
    elif i < 7:  # Bulan 5, 6, dan 7
        laba[i] = modal * 0.05  # Laba 5%
    else:  # Bulan 8
        laba[i] = modal * 0.03  # Laba 3%
    
    # Tampilkan laba per bulan
    print(f"laba bulan ke-{i+1} sebesar: {laba[i]}")
    
    # Tambahkan ke total laba
    total_laba += laba[i]

# Tampilkan total laba
print(f"Total laba adalah: {total_laba}")