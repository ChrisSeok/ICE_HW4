#6번, B835193 석채원
import random
sumdice = int(input("원하는 두 주사위의 합을 입력하시오?"))
while 1:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print("첫번째 주사위 =",d1,"두번째 주사위=",d2,"합=",d1+d2)
    
    #원하는 결과가 나왔을 때만 break from infinite loop
    if (d1+d2)== sumdice:
        print("원하는 합이 나왔습니다. 합=",sumdice)
        break


    