#5번, B835193 석채원
oddnum = int(input("3보다 큰 홀수를 입력하시오:"))
sum=0;
i = 3
# i goes up from 3 to oddnum
while i<=oddnum:
    sum += (i-2)/i
    i+=2
    
print(sum)