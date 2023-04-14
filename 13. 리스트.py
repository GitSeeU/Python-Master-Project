# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10 # 변수에 값을 대입해 선언
subway2 = 20
subway3 = 30

subway = [10, 20, 30] # 리스트를 만들고 값을 넣어줌 
print(subway) # [10, 20 ,30] 출력

subway = ["유재석", "조세호", "박명수"] # 리스트 안에 문자일시 '....' 로 나옴
print(subway) # ['유재석', '조세호', '박명수'] 출력

# 조세호씨가 몇번째 칸에 타고있나?
print(subway.index("조세호")) # 1 출력

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append를 사용하여 기존에 있던 값에 값을 추가해줌(맨 뒤에)
print(subway) # ['유재석', '조세호', '박명수', '하하'] 출력

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # 값을 삽이위츠를 설정하고 넣을값을 적어줘야함. 
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하'] 삽입됨

# 지하철에 있는 사람을 뒤에서부터 한 명씩 꺼냄
print(subway.pop()) # pop은 뒤에서 부터 하나씩 꺼내는 함수
print(subway) # ['유재석', '정형돈', '조세호', '박명수'] 출력

# print(subway.pop()) 
# print(subway) # ['유재석', '정형돈', '조세호'] 출력

# print(subway.pop()) 
# print(subway) # ['유재석', '정형돈']

# 같은 이름에 사람이 몇명 있는지 확인
subway.append("유재석") # 리스트에 유재석을 하나더 추가해줌
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '유재석'] 출력
print(subway.count("유재석")) # 유재석이 몇번 들어갔는지 세줌

# 정렬도 가능
num_list = [5,2,4,3,1] # 변수에 리스트 생성 
num_list.sort() # 리스트 안에 값을 정렬해줌
print(num_list) # [1, 2, 3, 4, 5] 출력

# 순서 뒤집기   
num_list.reverse() # 순서를 반대로 해줌
print(num_list) # [5, 4, 3, 2, 1]

# 모두지우기
num_list.clear() # 리스트 안에 값을 다 지워줌
print(num_list) # []

# 다양한 자료형 함께 사용
num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

# 리스트 확장
num_list.extend(mix_list) # num_list 값에 mix_list 를 넣어줌 
print(num_list) # [5, 4, 3, 2, 1, '조세호', 20, True] 출력
 

 