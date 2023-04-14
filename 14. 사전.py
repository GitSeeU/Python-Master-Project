# cabinet = {3:"유재석", 100: "조세호"} # 키는 3 벨류는 유재석, 키는 100 벨류 조세호 입력(정수형)
# print(cabinet[3]) # 유재석 반환
# print(cabinet[100]) # 조세호 반환

# print(cabinet.get(3)) # get 함수를 사용하여 불러오려는 값을 반환
# print(cabinet[5]) # 5라는 키가 배정되지 않았으므로 오류 반환
# print(cabinet.get(5)) # 값이 없을시에 NONE 반환됨
# print(cabinet.get(5, "시용가능")) # 5라는 값에 대해서 없을시에 사용가능 반환
# print("hi") 

# print(3 in cabinet) # cabinet 3에 유재석이라는 값이 할당되어 있기때문에 True출력
# print(5 in cabinet) # cabinet 5에 값이 할당되있지않기때문에 False출력

cabinet = {"A-3" : "유재석", "B-100":"김태호"} # 문자열str로 값을 선언햇을시 A-3에 유재석 할당, B-100에 킴태호 할당
print(cabinet ["A-3"]) # 키에 해당하는 값인 유재석 반환
print(cabinet ["B-100"]) # 키에 해당하는값인 김태호 반환
# {'A-3': '유재석', 'B-100': '김태호'}

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 캐비넷에 A-30이라는 키를 만들고 그 키에 유재석이 빠지고 김종국라는 값을 넣음
cabinet["C-20"] = "조세호" # 캐비넷에 C-20이라는 키를 만들고 그 키에 조세호라는 값을 넣음
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호', 'A-30': '김종국', 'C-20': '조세호'} 반환 

# 간 손님
del cabinet["A-3"] # del함수를 이용하여 cabinet A-3에 할당된 값을 지워줌
print(cabinet) # {'B-100': '김태호', 'A-30': '김종국', 'C-20': '조세호'} 반환

# Key들만 줄력
print(cabinet.keys()) # dict_keys(['B-100', 'A-30', 'C-20'])반환, 현재 할당된 키(값) 을 반환

# Value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])반환, 키는 빠지고 안에 할당된 이름들만 나옴 

# Key, Value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])반환, 키와 벨류가 둘다 포함된 값을 반환

# 목욕탕 폐점
cabinet.clear() # .clear() 함수를 이용하여 할당된 값을 다 지워줌
print(cabinet) # 안에 값을 지웠으므로 {} 반환 
