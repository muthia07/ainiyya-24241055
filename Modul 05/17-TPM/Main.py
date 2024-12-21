# TPM Tugas 
member = input("Apakah Member? : ")
total_belanja = float(input("Masukkan Total Belanja = Rp. "))


if member == 'ya' and total_belanja > 500.000:
    diskon_persen = 20
elif member == 'ya' and total_belanja <= 500.000:
    diskon_persen = 10
elif member == 'tidak' and total_belanja > 500.000:
    diskon_persen = 5
elif member == 'tidak' and total_belanja <= 500.000:
    diskon_persen = 0
    
diskon_rp = total_belanja * (diskon_persen / 100)
total_bayar = total_belanja - diskon_rp

print(f"Total Belanja: Rp. {total_belanja:.3f}")
print(f"Diskon persen: {diskon_persen}%")   
print(f"Diskon Rp: Rp. {diskon_rp:.3f}") 
print(f"Bayar Rp: Rp. {total_bayar:.3f}")