#7번_B735042_김대겸

# 반복문 시작 (1, 50)의 범위까지 i를 1씩 증가시키며 반복하도록 설정.
for i in range(1, 51):
    # 2제곱값을 i를 이용해 표현하고 이를 변수 sec에 저장.
    sec = i * i
    # 3제곱값을 i를 이용해 표현하고 이를 변수 sec에 저장.
    thi = i * i * i
    # 4제곱값을 i를 이용해 표현하고 이를 변수 sec에 저장.
    fou = i * i * i * i
    # 제곱값들을 출력하고, i는 1증가되어 반복한다. 
    print(i, "\t", sec, "\t", thi, "\t", fou)    
