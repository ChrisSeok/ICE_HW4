#1번, B835193 석채원
interest = float(input("이자율을 입력하시오:"))
target = float(input("목표배율을 입력하시오:"))
#initialize year
year =0 
initmoney=money=10 #any number is fine, since we deal with ratio
while 1:
    money=money+(money*interest)
    year+=1
    if(money>=initmoney*target):
        break;
print("이자율이 %g 일 때 원금의 %g배가 되기 위해 %d 년이 걸립니다."%(interest,target,year))
# use %g to eliminate 0s under digit
    
    
