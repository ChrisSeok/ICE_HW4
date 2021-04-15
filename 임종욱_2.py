# C111152 임종욱

from random import randint

x = int(randint(0,100))
y = int(randint(0,100))


z = int(input('%d + %d의 값은?'%(x,y)))
# 답이 틀리면 반복문을 이용해 다시 물어본다
while z != x+y :
    print('틀렸습니다')
    z = int(input('%d + %d의 값은?'%(x,y)))

print('맞았습니다.')