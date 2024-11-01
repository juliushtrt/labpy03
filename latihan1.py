from random import random

def tampilkan_bilangan_acak():
    try:
        # Input jumlah data yang diinginkan
        n = int(input("Masukkan nilai N: "))
        
        # Kombinasi while dan for
        i = 1
        while i <= n:
            nilai_acak = random()  # Menghasilkan bilangan acak antara 0 dan 1
            
            # Hanya tampilkan jika nilai kurang dari 0.5
            if nilai_acak < 0.5:
                print(f"data ke: {i} => {nilai_acak}")
            else:
                # Jika nilai >= 0.5, ulangi iterasi ini
                continue
            
            i += 1
            
        print("Selesai")
        
    except ValueError:
        print("Error: Masukkan angka bulat yang valid!")

# Jalankan program
tampilkan_bilangan_acak()