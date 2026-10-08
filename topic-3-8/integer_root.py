n = int(input())
x = n
while x * x > n:
    x = (x + n // x) // 2
print(x)