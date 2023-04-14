# 자료구조의 변경
menu = {"커피", "우유", "주스"} # menu라는 변수에 "커피", "우유", "주스" 지정
print(menu, type(menu)) # "커피", "우유", "주스" <class 'set'> 반환, 위에 변수값을 {} 중괄호로 묶어서 class type 이 set로 나옴

menu = list(menu) # list 함수를 써서 변수에 설정값을 list로 변환
print(menu, type(menu)) # ['우유', '커피', '주스'] <class 'list'> 반환

menu = tuple(menu) # tuple 함수를 써서  변수에 설정값을 tuple로 변환
print(menu, type(menu)) # ('커피', '주스', '우유') <class 'tuple'> 반환

menu = set(menu) # set 함수를 써서  변수에 설정값을 set 으로 변환
print(menu, type(menu)) # ('커피', '주스', '우유') <class 'set'> 반환

# Quiz 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 잰행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글내용과 상관 없이 무작위로 추첨하되 중복불가
# 조건3 : random 모듈과 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 -- 
# 치킨당첨자 : 1
# 커피당첨자 : [2, 3, 4]
# -- 축하합니다 -- 

# (활용예제)

# from random import*
# lst = [1,2,3,4,5]
# print(lst) # [1, 2, 3, 4, 5]
# shuffle(lst)
# print(lst) # random하게 변수안에 값을 섞어줌
# print(sample(lst), 1)

from random import*

users = range(1, 21) # 1 부터 20까지에 users라는 변수를 설정
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 -- ")
print("치킨당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 -- ")
