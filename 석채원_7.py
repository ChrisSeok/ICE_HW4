#7번, B835193 석채원
 #이중for문 사용
for i in range(1,51): #from 1~50
    for j in range(1,5): #from 1~4
        print(i**j,"\t",end='') #use end='' to eliminate '\n'
    print() # print() ends with '\n'