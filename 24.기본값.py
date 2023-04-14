def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t 주 사용언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬") # profile함수에 일일이 다른값을 넣어줌
profile("김태호", 20, "파이썬") # profile함수에 일일이 다른값을 넣어줌

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age = 17, main_lang = "파이썬"): # profile age 와 main_lang을 설정해서 프로필 함수가 호출될때 자동으로 해당값이 들어감
    print("이름 : {0}\t나이 : {1}\t 주 사용언어: {2}".format(name, age, main_lang)) 

profile("유재석")
profile("김태호")
