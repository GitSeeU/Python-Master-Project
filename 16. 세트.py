# 집합 (set)
# 중복이 안돼고 순서가 없는 특징이 있음
my_set = {1,2,3,3,3} # my_set 이라는 변수에 {1,2,3,3,3} 를 지정
print( my_set) # 중복을 허용하지 않기 때문에 {1,2,3} 반환

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'} 반환, &기호를 사용하여 두 변수에 교집합을 구함
print(java.intersection(python)) # .intersection() 으로 교집합을 구함

# 합집합 (java를 할수있거나 python 할 수 있는 개발자)
print(java | python) # | = or 을 써서 java 와 python을 둘다 할수있는 개발자값{'양세형', '조세호', '박명수', '유재석'}을 반환
print(java.union(python)) #.union 함수를 써서 java 와 python을 둘다 할수있는 개발자값개발자값{'양세형', '조세호', '박명수', '유재석'}을 반환

# 차집합 (java는 할수있지만 python은 할줄 모르는 개발자)
print(java - python) # -기호를 이용해 java는 할수있지만 python은 할줄 모르는 개발자 값 {'조세호', '양세형'}을 반환
print(java.difference(python)) # .difference 함수를 사용해 java는 할수있지만 python은 할줄 모르는 개발자 값 {'조세호', '양세형'}을 반환

# python 할줄 아는 사람이 늘어남
python.add("김태호") # pyhton 함수에 "김태호" 를 추가
print(python) # {'박명수', '유재석', '김태호'} 반환

# java를 잊어버렸어요
java.remove("김태호") # .remove함수를 사용하여 "김태호"를 java 변수에서 삭제
print(java) # {'유재석', '양세형'} 반환 