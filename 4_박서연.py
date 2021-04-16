#4번문제 

x = int(input('첫번째 정수: '))
y = int(input('두번째 정수: '))

for i in range(x+1 or y+1, 1, -1):
    if x%i == 0 and y%i == 0:
        print(i)
        break

