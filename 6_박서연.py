#6번문제
import random

x = random.randint(1, 6)
y = random.randint(1, 6)

wanted = int(input('원하는 두 주사위의 합을 입력하시오? '))

while x + y != wanted :
    print('첫번째 주사위=', x, '두번째 주사위=', y, '합=', x+y)
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    
else:
    print('원하는 합이 나왔습니다. 합 =', x+y)
    

