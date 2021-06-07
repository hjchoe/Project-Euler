sum = 0

f = open("/Users/hjcho/Dropbox/programming/T2 python/Project Euler/problem13.txt", 'r')

for line in f:
    sum += int(line)
sum = str(sum)
print(sum[0:10])
