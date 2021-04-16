#9번문제
print('문자열을 입력하시오? ', end='')
string = input()

print('문자를 입력하시오? ', end='')
word = input()

count = 0

if len(string)>0:
    for x in string:
        if x in word:
            count = count + 1
        if x in '$':
            break

print(count)
          
