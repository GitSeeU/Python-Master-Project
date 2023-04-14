# 지역변수는 함수내에서만 사용가능 (함수가 호출될때 만들어졌다가, 함수가 끝나면 사라지는 변수)
# 전역변수는 모든 공간에서 사용가능한 변수
gun =  10

def checkpoint(soldiers): # 경계근무
   # gun = 20
    global gun # 전역변수인 gun 사용 
    # gun = gun - soldiers # 현재 총에서 군인에 수만큼 뺀수를 다시 gun에 넣어줌, gun - soldiersdptjdml gun은 지역변수
    gun = gun - soldiers # 현재 총에서 군인에 수만큼 뺀수를 다시 gun에 넣어줌
    print("[함수 내] 남은 총: {0}".format(gun)) # [함수 내] 남은 총: 18 지역변수에 영향을 받아 20자루에서 2를뺀 18 출력 / 전역변수 사용시 8 출력


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers 
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun # 합수값 리턴

print("전체 총: {0}".format(gun)) # 전체 총: 10 출력, 함수 밖에 있는 전역변수인 hun의 영향을 받음
#checkpoint(2) # 2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2) # 전역변수 gun을 받음
print("남은 총: {0}".format(gun)) # 남은 총: 8 출력, 지역변수 영향

# Quiz) 표준 체중을  구하는 프로그램을 작성하시오

# * 표준체중: 각 개인의 키에 적당한  체중

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도의  함수 내에서 계산
#             *함수명 : st_weight
#             *전달값 : 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점  둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의  표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자": 
        return height * height * 22
    else:
        return height * height * 21
height = 175
gender = "남자"
weight =round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의  표준 체중은 {2}kg 입니다.".format(height, gender, weight))