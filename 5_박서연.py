#5번문제 

number = int(input('3보다 큰 홀수를 입력하시오? '))
n=3
sum=0

while n <= number :
    sum = sum + (n-2)/n
    n = n + 2
    
print(sum)