"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
------------------------------------------------------
1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.
"""
def summary():
    sonuc = sum( sayi for sayi in range(0,1000) if (sayi % 3 == 0 or sayi % 5 == 0) )
    return sonuc

print(summary())
