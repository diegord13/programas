n = 10
a, b = 1, 1
print(a, b, end = '')
for i in range(2, n+1):
    a, b = b, a+b
    print(' ', b, end='')