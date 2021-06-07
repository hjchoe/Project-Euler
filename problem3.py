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

num = 600851475143
sprime = 2
fprime = 0

while True:
    if checkifprime(num) == True:
        fprime = num
        break
    if num % sprime == 0:
        num = num / sprime
    else:
        sprime = nextprime(sprime)



print(fprime)