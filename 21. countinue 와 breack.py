absent = [2, 5] # 결석
No_book = [7] # 책을 깜빡함
for student in range(1, 11): # 1 ~ 10까지
    if student in absent: 
        continue # continue를 사용하여, absent 에 해당번호가 있을시에는 그 번호를 스킵하고 계속 for문 작동
    elif student in No_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break # break 를 사용함으로써 elif문이 작동되면 elif문 밑에 print를 출력하고 반복문을 종료허고 끝내는 것을 의미함
    print("{0}, 책을 읽어봐".format(student))  # 2 와 5를 제외한 1부터 10까지 , 책을 읽어봐 반환 