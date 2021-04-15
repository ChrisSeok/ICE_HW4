# C111152 임종욱

a = int(input('정수를 입력하시오:'))
Sum = 0

#a != 0이면  정수를 입력받는다
while a != 0:
    Sum += a
    a = int(input('정수를 입력하시오:'))

print('합은',Sum,'입니다')