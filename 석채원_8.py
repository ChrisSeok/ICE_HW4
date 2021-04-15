#8번, B835193 석채원
strin = input("문자열을 입력하시오:")
slength = len(strin)-1  #문자열 길이-1 == 마지막 원소의 index
# slength는 마지막 원소의 index 부터 index 0까지 
while slength >= 0:
    print(strin[slength],end='')
    slength-=1
    
