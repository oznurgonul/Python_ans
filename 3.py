
"""
Soru 3:Baştan ve sondan yazıldığında değişmeyen sayılara palindrom sayılar denir.
Ör: 1001,23432. 2 haneli sayıların çarpımından elde edilen en büyük palindrom 
sayısı 91*99=9009'dur.3 haneli sayıların çarpımından elde edilen en büyük
palindrom sayısını bulan fonksiyonu yazınız.
"""


from itertools import combinations_with_replacement
def is_palindrom(number):
    num_str = str(number)
    return num_str == num_str[::-1]
print(max(x for x in
    (a*b for (a,b) in combinations_with_replacement(range(100,1000),2))
    if is_palindrom(x)))
