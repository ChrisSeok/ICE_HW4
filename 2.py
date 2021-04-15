#2번_B735042_김대겸
#난수 발생 코드 호출.
import random
#(0~100# 사이의 랜덤한 수를 변수x에 저장.
x = random.randint(0, 100)
#(0~100# 사이의 랜덤한 수를 변수x에 저장.
y = random.randint(0, 100)
# x와 y를 이용한 정답을 answer에 저장.
answer = x + y
#반복문 시작.(무한루프로 시작)
while True:
    #문제출력.
    print(x, "+", y, "의 값은?")
    #사용자로부터 답을 입력받고, user_ans에 저장.
    user_ans = int(input("정답을 입력하시오: "))
    #문제의 정답과 사용자가 입력한 답이 같으면, 맞았다고 출력하고 반복문 종료.
    if (user_ans == answer):
        print("맞았습니다.")
        break
    #문제의 정답과 사용자가 입력한 답이 다르면, 틀렸다고 출력하고 다시 반복.
    else:
        print("틀렸습니다.")