# C111152 임종욱

from random import randint

dice_1 = int(randint(1,6))
dice_2 = int(randint(1,6))
Sum = dice_1 + dice_2
user = int(input('원하는 두 주사위의 합을 입력하시오? '))

while Sum != user:
    print('첫번째 주사위=',dice_1,'두번째 주사위=',dice_2,'합 = ',Sum)
    dice_1 = int(randint(1,6))
    dice_2 = int(randint(1,6))
    Sum = dice_1 + dice_2

    
print('첫번째 주사위= ',dice_1,' 두번째 주사위= ', dice_2,'합 = ',Sum)
print('원하는 합이 나왔습니다. 합=',Sum)