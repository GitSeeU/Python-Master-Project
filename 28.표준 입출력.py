# print("Python", "Jave", "JavaScript", sep = " vs ") # Python vs Jave vs JavaScript 출력, sep을 사용하여 문장사이사이 "," 위치마다 vs를 출력해줌
# print("Python", "Jave", sep = " vs ", end = "?") # end를 사용함으로써 문장장 문장사이에에 "?" 출력, 또한 2줄출력되는 문장을 한문장으로 출력해줌
# print("무엇이 더 재미있까요?") # 무엇이 더 재미있까요? 출력

# import sys # sys라는 모델을 불러옴
# print("Python", "Jave", file = sys.stdout) # Python Jave 출력, stdout = standard out = 표준출력 / log처리를 할때 표준출력에 대해서는 잘 출력되므로 따로 신경 필요x
# print("Python", "Jave", file = sys.stderr) # Python Jave 출력, stderr = standard erro = 표준에러 / log처리를 할때 표준에러는 따로 에러처리를 해줘야함

# # 시험성적
# scores = {"수학": 0, "영어": 50, "코딩": 100} # scores 라는 dictionary 생성, 수학 = key 0 = value, 영어 = key 50 = value, 코딩 = 100, 100 = value
# for subject, score in scores.items():  # subject, score 라는 두개에 변수로 for문을 정의, itmes로 key 와 value 페어로 튜플로 값이 출력, 
#     print(subject.ljust(3), str(score).rjust(4), sep = ":") # .ljust = letf adjust = 왼쪽정렬, rjust = right adjust = 우측 정렬
#                                                             # .ljust(3)에 의미는 3만큼에 자리를 확보하고 왼쪽정렬해라 / .rjust(4) 4만큼에 자리를 확보하고 오른쪽 정렬해라 에 의미
#                                                             # sep = ":" 는 "," 사이에 : 삽입 

# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1, 21): 
#     print("대기번호 :", str(num).zfill(3)) # 대기번호 : 1 ~ 20 까지 출력, .zfill(3)은 3개의 공간을 확보하고 자리가 없는숫자는 0으로 채워넣음

answer = input("아무 값이나 입력하세요 : ") # 사용자에게 입력받는값이 answer값이됨
print(type(answer)) # input값은 무조건 str
# print("입력하신값은" + answer + "입니다.") # ㅑinput값을 받아 문장을 출력

    

