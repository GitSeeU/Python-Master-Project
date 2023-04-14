# while - 조건이 맞을때 지속적으로 반복
# customer = "토르" # customer라는 변수에 토르라는 값을 지정
# index = 5
# while index >= 1: # index가 1보다 크거나 같을때 아래 문장을 출력
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index)) # 토르, 커피가 준비되었습니다. 5 ~ 1 번 남았어요 반환
#     index -= 1 # index = 5 값에서 while문을 실행시킬때마다 한번씩 빼줌
#     if index == 0: # if문을 써서 index 값이 0이 되었을떄 아래 문장을 출력
#         print("커피는 패기처분되었습니다.") # if문에 조건을 충족시 "커피는 패기처분되었습니다." 반환

# customer = "아이언맨" # customer라는 변수에 아이언맨이라는 값을 지정
# index = 1 
# while True: # 계속 호출하기 위해 True를 써줌
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index)) # 아이언맨, 커피가 준비되었습니다. 호출 1~9999....회 반환
#     index += 1 # 횟수를 보기위해 while함수가 실행되는 동안 index값에 1을 계속 더해줌

    # ctrl + c 강제종료


customer = "토르" 
person = "Unknown"

while person != customer: # while 토르가 아닐시 아래 문장을 계속 반복
    print("{0}, 커피가 준비되었습니다.".format(customer)) # 토르, 커피가 준비되었습니다.
    person = input("이름이 어떻게 되세요") # 사용자가 토르라고 입력하지않으면 다시 처음부터 while문 반복