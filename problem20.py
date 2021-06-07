def factorial(n):
    i = n
    prod = 1
    while i >= 1:
        prod = prod * i
        i -= 1
    return prod

prod = factorial(100)

prod = str(prod)
sum = 0
for digit in prod:
    sum += int(digit)

print(sum)