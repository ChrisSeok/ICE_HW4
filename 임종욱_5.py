# C111152 임종욱

N = int(input('3보다 큰 홀수를 입력하시오? '))
i = 0
Sum = 0

while (2 * i +1) < N  :
    
    An = (2*i +1) /(2*(i+1)+1)
    i += 1
    Sum += An

print(Sum)
