a = [1, 2, 3, 17, 64, 1234, 4, 5, 7]
maxim = 0

for i in range(len(a)):
    if a[i] > maxim: maxim = a

print(maxim)
