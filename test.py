import os, sys, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#array1 = np.array([[1, 2, 3, 4]])
#print(array1.shape)

#program to calculate the factorial of a number
def fact(n):
    prod = 1
    if n == 0:
        return 0
    else:
        while n > 0:
            prod = prod * n
            n = n-1
    return prod

x = int(input("Enter the number whose factorial is to be calculated: "))
assert fact(x) == math.factorial(x)

print(f'Factorial of {x}: {fact(x)}')

#function that checks whether a string is a palindrome
word = input("Enter the word that needs to be assessed whether it is a palindrome: ")
def palindrome_check(word): 
    lst = []
    lst1= []

    for l in word.lower():
        lst.append(l)

    i=len(lst)-1
    while i > -1:
        lst1.append(lst[i])
        i-=1

    if lst == lst1:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')

palindrome_check(word)


