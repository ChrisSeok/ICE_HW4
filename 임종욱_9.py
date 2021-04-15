# C111152 임종욱

st = input('문자열을 입력하시오? ')
ch = input('문자를 입력하시오? ')
i =0
for c in st:
    if c == '$':
        break
    if c == ch:
        i += 1

print(i)