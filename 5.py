"""
Soru 5 : Verilen listedeki None değerleri, kendinden önceki None olmayan değerle
yer değiştirip yeni bir liste oluşturan fonksiyonu yazınız. Örn: İnput[3,None,2,
None,None,1,False,None,10] Output: [3,3,2,2,2,1,False,False,10] .Listenin None ile
başlamayacağını varsayabilirsiniz.
"""

liste = [3,None,2,1,5,None,6,False,None,7]
print(liste)

liste[1] = 3
liste[5] = 5
liste[8] = False
print(liste)
