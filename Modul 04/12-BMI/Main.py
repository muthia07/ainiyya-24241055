tinggi_badan = float(input("Masukkan tinggi badan :"))
berat_badan = float (input("Masukkan berat badan :"))

tinggi_badan = tinggi_badan / 100 
bmi = berat_badan / (tinggi_badan ** 2)

print(f"BMI adalah : {bmi:.1f}")