"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
---------------------------------------
İlk on doğal sayının karelerinin toplamı,

1^2 + 2^2+... + 10^2 = 385
İlk on doğal sayının toplamının karesi,

(1 + 2+... + 10)^2 = 552 = 3025
Bu nedenle, ilk on doğal sayının karelerinin toplamı ile toplamın karesi arasındaki fark 3025-385 = 2640'dır.

İlk yüz doğal sayıların karelerinin toplamı ile toplamın karesi arasındaki farkı bulun.
"""
x=0
for i in range(1,101):
        x += i*i
y=0
for i in range(1,101):
    y += i
y=y*y
print("Result is ",(y-x))