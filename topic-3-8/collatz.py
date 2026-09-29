a = int(input())
steps = 0
peakval = 0
while a > 1:
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
    steps = steps + 1
    if a > peakval:
        peakval = a
print(peakval)
print(steps)