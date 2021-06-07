def checkifprime(n):
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
 
    if (n % 2 == 0 or n % 3 == 0): 
        return False
 
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
 
    return True

def nextprime(n):
    n += 1
    while checkifprime(n) == False:
        n += 1
    return n

n = 2
sum = 0
while n < 2000000:
    sum += n
    n = nextprime(n)

print(sum)