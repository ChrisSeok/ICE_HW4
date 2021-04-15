# C111152 임종욱

x = int(input('첫번째 정수: '))
y = int(input('두번째 정수: '))
i = 1

while i <= min(x,y):
    if (x % i == 0) and (y % i == 0):
        divisor = i
    i += 1

print(divisor)