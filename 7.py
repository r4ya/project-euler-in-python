""""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
------------------------------------
İlk altı asal sayıları listeleyerek: 2, 3, 5, 7, 11, ve 13
6. nın 13 olduğunu görebiliriz.

10 001. asal sayı nedir?
"""
def prime():
    last=10001
    x=2
    primelist=[]
    while(len(primelist)<last):
        if all(x % primenumber for primenumber in primelist):
            primelist.append(x)
        x+=1
        print(primelist[-1])
    print("\n\n10 001st prime number is ",primelist[10000])
prime()