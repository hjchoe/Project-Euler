
def palindromecheck(n):
    num = str(n)
    l = len(num)
    if l == 6:
        fpart = num[0:3]
        spart = num[3:6]
        if fpart == spart[::-1]:
            return True
        else:
            return False
    else:
        return False

mpalin = 0
for i in range(100, 1000):
    j = i
    while j > 100:
        num = i * j
        if palindromecheck(num) and num > mpalin:
            mpalin = num
            print(f"{i} * {j} = {mpalin}\n")
        j -= 1

print(mpalin)