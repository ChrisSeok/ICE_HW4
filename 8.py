#8번_B735042_김대겸

# 사용자로부터 문자열을 입력받고, 이를 user에 저장.
user = input("문자열을 입력하시오: ")
# 입력받은 문자열을 뒤집을 단어를 변수user_reverse로 선언하고, 그 안에 빈 문자열을 저장.
user_reverse = ""
# 입력받은 문자열 중 하나씩 문자를 꺼내 반복하도록 반복문시작.(마지막 문자가 끝나면 반복 종료) 
for ch in user:
    # 꺼낸 문자열을 user_reverse에 추가되도록 작성(다음 문자는 그 전의 문자 앞에 오도록)
    user_reverse = ch + user_reverse
# 뒤집은 문자열 출력.    
print(user_reverse)