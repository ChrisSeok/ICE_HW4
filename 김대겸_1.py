#1번_B735042_김대겸

#사용자로부터 년 이자율을 입력받고 interest에 저장.
interest = float(input("이자율을 입력하시오? "))
#사용자로부터 목표 배율을 입력받고 goal에 저장.
goal = float(input("목표 배율을 입력하시오? "))
#year에 0을 저장
year = 0
#반복문 시작(무한루프로 시작)
while True:
    #위의 interest변수를 이용해 year_interest변수 선언
    year_interest = (1 + (interest/100)) ** year
    #반복문을 한 번 돌때마다  year의 값이 1씩 증가하도록 설정.
    year += 1
    #복리 이자율이 누적된 값과 목표 배율이 같아질 때 반복문을 종료하도록 설정.
    if year_interest >= goal:
        break
#같아지는 년도를 year을 이용하여 문제의 출력문을 출력.
print("이자율이", (interest/100), "일 때 원금의", goal, "배가 되기위해", (year-1), "년이 걸립니다.")
    
