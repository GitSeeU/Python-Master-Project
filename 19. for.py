# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0, 1, 2, 3, 4]: # list 안에 값이 순서대로 들어가서 밑에 print를 실행한후에 종료된다.
#     print("대기번호 : {0}".format(waiting_no)) # 대기번호 : 0 ~ 4 까지 반환


# for waiting_no in range(1,6): 1부터 시작하고 싶으면 range(1,6)
# for waiting_no in range(5): # range 0 ~ 5미만 안에 값이 순서대로 들어가서 밑에 print를 실행한후에 종료된다.
#     print("대기번호 : {0}".format(waiting_no)) # 대기번호 : 0 ~ 4 까지 반환

starbucks = ["아이언맨", "토르", "아이엠 그루트"] # starbucks 라는 변수안에 list로 " 아이언맨, 토르, 아이엠 그루트 " 를 설정
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    # 아이언맨, 커피가 준비되었습니다. 반환
    # 토르, 커피가 준비되었습니다. 반환
    # 아이엠 그루트, 커피가 준비되었습니다. 반환