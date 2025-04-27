def simple_intrest(p, n, r):
    i = (p * r * n) / 100
    a = p + i
    return i, a


p = eval(input("Enter the principal amount: "))
n = eval(input("Enter the rate of interest: "))
r = eval(input("Enter the time in years: "))
i, a = simple_intrest(p, n, r)
print("The simple interest is: ", i)
