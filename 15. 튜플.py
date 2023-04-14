# 리스트와는 다르게 내용에 변경이나 추가가 안됨, 단 속도가 리스트 보다 빠름.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 값을 추가할수 없기때문에 에러반환

# name = "김종국" # name 이란 변수에 "김종국" 지정
# age = 20 # age 란 변수에 20 지정
# hobby = "코딩" # hobby 란 변수에 "코딩" 지정
# print(name, age, hobby) # 김종국 20 코딩 반환

(name, age, hobby) = ("김종국", 20, "코딩") # 튜플을 이용해 변수값들을 한번에 선언
print(name, age, hobby) # 김종국 20 코딩 반환