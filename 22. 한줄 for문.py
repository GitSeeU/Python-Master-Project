# 출석번호 1, 2, 3, 4, 앞에 100을 붙이기로함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5] # students 라는 변수에 list로 1, 2, 3, 4, 5 라는 값을 지정
print(students) # [1, 2, 3, 4, 5] 반환
students = [i + 100 for i in students] # i 라는 값에 항상 100을 대해주라는 for문 을 작성
print(students) # [101, 102, 103, 104, 105] 반환

# # 학생이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"] # student 라는 변수에 "Iron man", "Thor", "I am groot" 이라는 string 형식에 값을 지정
students = [len(i) for i in students] # len는 string의 길이를 숫자로 변환해줌, students 라는 list의 변수를 길이로 변환
print(students) # [8, 4, 10] 반환

# 학생이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"] # student 라는 변수에 "Iron man", "Thor", "I am groot" 이라는 string 형식에 값을 지정
students = [i.upper() for i in students] # upper는 대문자로 뵨환해주는 함수, students안에 값을 하나씩 나져와서 대문자로 변환
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT'] 반환

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명에 승객솨 매칭 기회가 있을떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [o] 1번쨰 손님 (소요시간:15분)
# []  2번쨰 손님 (소요시간:50분)
# [o] 3번쨰 손님 (소요시간:5분)
# ...
# []  50번쨰 손님 (소요시간:16분)

# 총 탑승 승객 : 2 명 

from random import*

cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~50이라는 수(승객)
    time = randrange(5, 51) # 5 ~ 50분 사이에 소요시간
    if 5 <= time <= 15: # 5분에서 15분 이내의 손님(매칭 성공), 탑승 승객수 증가처리
        print("[o] {0}번쨰 손님 (소요시간:{1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번쨰 손님 (소요시간:{1}분)".format(i, time))
print("총 탑승 승객 수 : {0}". format(cnt)) # EX) 총 탑승 승객 수 : 13 반환

