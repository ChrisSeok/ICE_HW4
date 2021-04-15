#9번, B835193 석채원
strin = input("문자열을 입력하시오:")
letter = input("문자를 입력하시오:")
#count indicates the number of letters within the string
count = 0
for i in strin:
    if(i==letter):
        count+=1
    if(i=='$'):
        break;

print(count)
    