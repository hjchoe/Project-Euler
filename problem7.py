
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

numofprimes = 1
prime = 2
while numofprimes < 10001:
    prime = nextprime(prime)
    numofprimes += 1
print(f"{numofprimes}: {prime}")