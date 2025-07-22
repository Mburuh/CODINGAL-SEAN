def fibonacci(n):
    if n <=0:
       return n
    elif n==1:
        return n+recur_factorial(n+1)
    num=int (input ('enter a number:'))
    if num<=0:
        print('fibonnanci doesn`t exist for negative number')
    elif num==1:
        print("fibonacci exists")
        print('fibonacci of', num, 'is', fibonacci(num))