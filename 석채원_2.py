#2번, B835193 석채원
import random
x = random.randint(0,100)
y = random.randint(0,100)
#무한루프 
while 1:
    print(x,'+',y,"의 값은?")
    answer = int(input())
    #원하는 값을 얻으면 while문에서 break
    if(answer == x+y):
        print("맞았습니다.")
        break
    #원하는 값이 아닐경우 계속 while loop 돌기
    else :
        print("틀렸습니다.")
        
    