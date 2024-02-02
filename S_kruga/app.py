number = 25
n = 5
x = 3
while n <= 15:
    x_n = (1/n)*((n-1)*x+number/x**(n-1))
    n += 1
    print (str(x_n)[:9])