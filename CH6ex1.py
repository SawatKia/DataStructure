def factorial(n):
    if n == 1:
        return 1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
n = input('Enter Number : ')
n = int(n)
print(f'{n}! = ',end='')
print(factorial(n))