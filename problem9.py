

for m in range(1, 100):
    for n in range(1, m):
        a = m**2 - n**2
        b = 2 * n * m
        c = n**2 + m**2
        print(a, b, c)
        if a + b + c == 1000:
            answer = a * b * c

print(f"\n{answer}")
