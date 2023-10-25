kilo = float(input("Kilonuzu kilogram üzerinden giriniz."))
boy = float(input("Boyunuzu metre üzerinden giriniz."))

#BMI Hesaplama 
bmi = kilo/(boy ** 2)
print ("Vücut Kitle İndeksiniz (BMI) :",round(bmi,2))
if bmi < 18.5 :
    print ("Zayıfsınız.")
elif 18.5 <= bmi < 24.9 : 
    print ("Normal kilodasınız.")
elif 25 <= bmi < 29.9 : 
    print ("Fazla kilolusunuz.")
else : 
    print ("Obezsiniz.")
