print(""""""*********
Hesap Makinesi Programı

İşlemler

1.Toplama İşlemi

2.ÇIıkarma işlemi

3.Çarpma İşlemi

4.Bölme İşlemi
*********






"""""")


a = int(input("Birinci Sayı:"))
b = int(input("İkinci sayı:"))

işlem = input("İşlem Giriniz:")

if işlem == "1":
    print("{}ile {} in toplamı {} dır.".format(a,b,a+b))
elif işlem == "2":
    print("{}ile {} in toplamı {} dır.".format(a, b, a - b))
elif işlem == "3":
    print("{}ile {} in toplamı {} dır.".format(a, b, a * b))
elif işlem == "4":
  print("{}ile {} in toplamı {} dır.".format(a, b, a / b))


else:
    print("Geçersiz İşlem")





