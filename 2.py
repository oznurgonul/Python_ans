"""
Soru 2: 4 milyondan küçük 2'ye bölünebilen Fibonacci sayılarının toplamını
bulan fonksiyonu yazınız. 
"""


numbers = []
a = 1
b = 1
c = 1
while c<4000000: 
    c = a+b
    a = b
    b = c
    numbers.append(b)     
print(numbers)
# Fibonacci sayılarımız bunlardır.

# Çift olanları yazdıralım.

for fi in numbers:
    if fi > 0 and fi%2 == 0:
        print(fi)
        
#Toplamak için print(fi) komutunun çıktılarını liste haline getirdim.        

result = 0        
fibo_list = [2,8,34,144,610,2584,10946,46368,196418,832040,3524578 ]
for x in fibo_list:
    result += x
print("Çift Fibonacci Sayılarının Toplamı: ",result)  
