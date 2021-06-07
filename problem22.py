import string

f = open("/Users/hjcho/Dropbox/programming/T2 python/Project Euler/problem22.txt", "r")
namefromtxt = f.readlines()

x = namefromtxt[0]

x = x.replace('"', '')

names = []
name = ''
for char in x:
    if char != ',':
        name += char
    else:
        name = name.lower()
        names.append(name)
        name = ''

names.sort()

def charTOpos(letter):
    return string.ascii_lowercase.index(letter) + 1

def namescore(name, pos):
    sum = 0
    for char in name:
        p = charTOpos(char)
        sum += p
    return sum * pos

sum = 0
for name in names:
    pos = names.index(name)
    score = namescore(name, pos)
    print(f"{name} ({pos}): {score}")
    sum += score

print(sum)