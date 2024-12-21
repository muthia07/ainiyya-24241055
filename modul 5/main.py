# Input: apakah pelanggan memiliki kartu member, dan total belanja
member = input("Apakah member (ya/tidak): ").strip().lower()
total_belanja = float(input("Masukkan total belanja RP: "))

# Menentukan diskon berdasarkan kondisi yang ada
if member == "ya":  # Jika pelanggan memiliki kartu member
    if total_belanja > 500000:
        diskon_persen = 20
        diskon_rp = total_belanja * (diskon_persen / 100)
    else:
        diskon_persen = 10
        diskon_rp = total_belanja * (diskon_persen / 100)
else:  # Jika pelanggan tidak memiliki kartu member
    if total_belanja > 500000:
        diskon_persen = 5
        diskon_rp = total_belanja * (diskon_persen / 100)
    else:
        diskon_persen = 0
        diskon_rp = 0

# Menghitung total bayar setelah diskon
total_bayar = total_belanja - diskon_rp

# Output hasil perhitungan
print(f"Total belanja :{total_belanja:,.0f}")
print(f"Diskon persen :{diskon_persen}%")
print(f"Diskon RP     :{diskon_rp:,.0f}")
print(f"Bayar RP      :{total_bayar:,.0f}")