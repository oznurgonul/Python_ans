",.?!:;" gibi noktalama işaretlerini kelime uzunluğuna dahil etmemeniz gerekiyor.
Örn: avg_len("Elma, Portakal, Armut") - 5.66 gibi.
"""


sentence = input("Bir cümle giriniz : ")
sonuc = 0
while sentence[sonuc:]:
    sonuc = sonuc+1
print("\nUzunluk =", sonuc/2)

#eksik :(
