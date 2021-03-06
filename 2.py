"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
---------------------------------------
Fibonacci dizisindeki her yeni terim, önceki iki terimi ekleyerek oluşturulur.
1 ve 2 ile başlayarak, ilk 10 terim olacak:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Değerleri dört milyonu geçmeyen Fibonacci dizisindeki terimleri göz önüne alarak,
eşit değerli terimlerin toplamını bulun.
"""
def fibo():
    sonuc=0
    x=1
    y=2
    while x <= 4000000:
        if x % 2 == 0:
            sonuc += x
        x,y=y,x+y
    return sonuc

print(fibo())