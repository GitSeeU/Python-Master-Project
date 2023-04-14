print("백문이 불여일견\n백견이 불여일타.") # \n을 사용함으로써 줄을 바꿔줌, 백문이 불여일견 
                                                                      # 백견이 불여일타.

# 저는 "국제대 최재웅" 입니다.
print("저는 '국제대 최재웅' 입니다.") # 저는 '국제대 최재웅' 입니다. 반환   
print('저는 "국제대 최재웅" 입니다.') # 저는 "국제대 최재웅" 입니다. 반환
print("저는 \"국제대 최재웅\" 입니다.") # \" \" 를 써줌으로써 그 안에 문장에 "" 를 추가해줌, 저는 "국제대 최재웅" 입니다. 반환
print('저는 \'국제대 최재웅\" 입니다.') # \' \' 를 써줌으로써 그 안에 문장에 '' 를 추가해줌, 저는 '국제대 최재웅" 입니다. 반환

# \\ : 문장 내에서 \ 
# print("C:\Users\Administrator\Desktop\PythonWorkspace>")는 에러를 출력하므로 아래와 같이 \\ 로 수정해야함
print("C:\\Users\\Administrator\\Desktop\\PythonWorkspace>") # C:\Users\Administrator\Desktop\PythonWorkspace> 반환

# \r : 커서를 맨 앞으로 이동.
print("Red Apple\rPine") # \r뒤에있는 Pine(4자리)을 앞에있는 Red + 한자리를 리플레이스 해줌, PineApple 반환

# \b : 백스페이스 (앞에 한글자 삭제)
print("Redd\b Apple") # \b를 사용함으로써 앞에 한글자를 삭제해줌, Red Apple 반환

# \t : 탭
print("Red\tApple") # TAB키와 같은 역활, Redd    Apple 출력

# Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성
#예) http://naver.com
# 규칙1 : http:// 부분 제외 => naver.com
# 규칙2 : 처음만나는 점(.) 이후부분은 제외 => naver
# 규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#             (nav)                 (5)             (1)             (!)
#예) 생성된 비밀번호 :nav51!

url = "http://naver.com"
My_url = url.replace("http://", "") #규칙 1 
print(My_url)
My_url = My_url[:5]
print(My_url) #규칙 2
password = My_url[:3] + str(len(My_url)) + str(My_url.count("e")) + "!" # 규칙 3
print("{} 의 비밀번호는 {} 입니다.".format(url, password))



