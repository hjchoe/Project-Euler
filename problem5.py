i = 20
while True:
    status = True
    for x in range(11, 21):
        if i % x == 0:
            pass
        else:
            status = False
    if status == True:
        break
    i += 20
print(i)