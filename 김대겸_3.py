#3번_B735042_김대겸

#반복문 시작(무한루프로 시작)
while True:
    #정수의 합을 나타낼 변수total에 0을 저장.
    total = 0
    #사용자로부터 수를 입력받고 정수형태로 변환.
    int_user = int(input("정수를 입력하시오: "))
    #정수에 합에 사용자가 입력한 값을 더한다. 
    total += int_user
    #사용자가 0을 입력하면 total을 출력한 뒤 함수를 종료하고, 그렇지 않을 경우에는 다시 반복문을 반복한다.
    if (int_user == 0):
        print("합은", total, "입니다.")
        break
