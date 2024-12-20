#!/opt/anaconda3/bin/python

'''Basic script that takes a number as input and prints whether it's even or odd'''

num = int(input('Enter a number: '))

if num % 2 == 0:
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')