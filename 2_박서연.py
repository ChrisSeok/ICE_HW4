#2번문제 
import random

x = random.randint(0, 100)
y = random.randint(0, 100)
z = x + y 

print(x, '+', y, '의 값은?', end='')
calculation = int(input())

while z != calculation:
    print('틀렸습니다.')
    print(x, '+', y, '의 값은?', end='')
    calculation = int(input())

else:
    print('맞았습니다.')
    
    



