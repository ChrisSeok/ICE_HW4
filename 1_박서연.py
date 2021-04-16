#1번문제 / C111061 박서연 
import math

interest = float(input('이자율을 입력하시오? '))
target = float(input('목표 배율을 입력하시오? '))
rate = interest*0.01

year = math.ceil(math.log(target, (1+rate)))

print('이자율이', rate, '일때 원금의', target, '배가 되기위해', year, '년이 걸립니다')