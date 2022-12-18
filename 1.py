"""
Soru 1: 1000'den küçük, 3'e ya da 5'e bölünebilen tüm doğal sayıların toplamını
bulan fonksiyonu yazınız.
"""

numbers = []
for i in range(1,1000):
    if (i%3 == 0 or i%5 == 0):
        numbers.append(i)
print(numbers)      

#Sayılarımızı toplattırmak için:
  
result = 0
dividing = 0
for dividing in numbers:
    result += dividing
print("3'e ve 5'e bölünebilen 1000'den küçük sayıların toplamı: ", result)
