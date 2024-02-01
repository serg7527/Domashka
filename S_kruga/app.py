number = 25
n = 1
x = 2
while n <= 25:
    x_n = (1/n)*((n-1)*x+number/x**(n-1))
    n += 1
    print (str(x_n)[:9])