"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-----------------------------------------
Palindromik bir sayı her iki yolu da okur.
İki 2 basamaklı sayının ürününden yapılan en büyük palindrom 9009 = 91 × 99'dur.

İki 3 basamaklı sayının ürününden yapılan en büyük palindromu bulun.
"""
palindromes = []
for x in range (100,1000):
    for i in range (100,1000):
        sayi=str(i*x).split()[0]
        if len(sayi) == 6:
            if sayi[0] == sayi [-1] and sayi[1] == sayi[-2] and sayi [2] == sayi [-3]:
                palindromes.append(i*x)
print ("Max Palindrome: ",max(palindromes))

"""for a in range (0,len(palindromes)):
    print (palindromes[a])"""