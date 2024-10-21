# Program Kalkulator Sederhana
x = float(input("masukan bilangan pertama: " ))
y = float(input("masukan bilangan kedua: " ))
operasi = input("pilih operasi bilangan (+, -, *, /): ")
if operasi == '+':
    hasil = x + y
elif operasi == '-':
    hasil = x - y
elif operasi == '*':
    hasil = x * y
elif operasi == '/':
    hasil = x / y
print("Hasil: ", hasil)