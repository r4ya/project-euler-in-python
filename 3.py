"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
--------------------------------------------------------------
13195'in başlıca faktörleri 5, 7, 13 ve 29'dur.

600851475143 sayısının en büyük asal faktörü nedir ?
"""
largeprime = 600851475143
def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2, largeprime+1):
    if prime(i) and largeprime % i == 0:
        print(i)