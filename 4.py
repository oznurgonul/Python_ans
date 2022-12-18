"""
Soru 4: Pozitif tam sayılar kendisinden ve 1'den başka böleni olmayan sayılara
asal sayılar denir. ilk on asal sayı 2,3,5,7,11,13,17,19,23,29 biçiminde sıralanır.
1.asal sayı 2, 10. asal sayı 29'dur.10001. asal sayıyı bulan fonksiyonu yazınız.
"""


prime=[2]

def numberof_prime(sayi):
    for a in range(2,56161846123184318543):
        for b in prime:
            if a%b==0:
                break
            if a%b!=0 and b==prime[-1]:
                prime.append(a)
                break
        if len(prime)==sayi:
            return(prime[-1])
            break
print(numberof_prime(10001))
