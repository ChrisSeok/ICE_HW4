# C111152 임종욱

rate = float(input('이자율 입력하시오? '))/100
goal = float(input('목표 배율을 입력하시요? '))

year = 0
now  = 1

while now <= goal :
    now *= rate+1
    
    year += 1

print('이자율이 ',round(rate,3),'일때 원금의 ',goal,'배가 되기위해 ',year,'년이 걸립니다')
