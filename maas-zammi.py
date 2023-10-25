maas = float(input("Mevcut maaşı girin."))
zam_orani = float(input("Zam oranını yüzde olarak girin: "))
zam_miktari = (zam_orani / 100) * maas
yeni_maas = maas+zam_miktari
print("Zam Miktarı :" , zam_miktari)
print("Zamlı Maaş :" , yeni_maas)