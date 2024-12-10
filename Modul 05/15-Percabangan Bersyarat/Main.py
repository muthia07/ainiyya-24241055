# percabangan bersyarat / Nested if

# kalkulator
# +, -, *, /, %, **, //

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=")

angka_1 = float(input("Masukkan Bilangan 1 = "))
operator = input("operator (+, -, /, *, %, **, //) = ")
angka_2 = float(input("Masukkan Bilangan 2 = "))

# percabangan bersarang Elif statement

if operator == '+':
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '*':
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '%':
    hasil = angka_1 % angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '**':
    hasil = angka_1 ** angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '//':
    hasil = angka_1 // angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print(f"operator {operator} tidak dikenal")
print("Sekian Terima Kasih")    