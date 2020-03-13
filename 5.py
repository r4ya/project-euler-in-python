"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
------------------------------------------------
2520, herhangi bir geri kalan olmadan 1'den 10'a kadar olan sayıların her birine bölünebilen en küçük sayıdır.

1'den 20'ye kadar olan tüm sayılarla eşit olarak bölünebilen en küçük pozitif sayı nedir?
"""
"""
def bolunen():
    for i in range (20,0,-1):
        for j in range (19,0,-1):
            if i % j == 0:
                print(j)
    print("\n")

bolunen()
"""

def division(number):
    for i in range (2,21):
        if number % i != 0:
            return False
    return True
number=20
while True:
    if division(number):
        break
    number += 20

print(number)
