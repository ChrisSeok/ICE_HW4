#8번문제 
word = input('문자열을 입력하시오? ')
reverse = ''

for x in word:
    reverse = x + reverse

print(reverse)