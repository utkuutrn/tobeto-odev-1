sayi = input("Bir sayı giriniz :")
ters_sayi = sayi [::-1] 
if sayi == ters_sayi:
     print(f"{sayi} bir palindrom sayıdır.")       
else:
     print(f"{sayi} bir palindrom sayı değildir.")
        