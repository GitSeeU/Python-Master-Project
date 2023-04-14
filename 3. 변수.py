# 애완동물을 소개해 주세요.
animal = "강아지" # animal 이란 변수에 "강아지" 로 지정
name = "우주" # name 이란 변수에 "우주" 로 지정
age = 4 # age란 변수에 4 로 지정
hobby = "산책" # hobby란 변수에 "산책" 으로 지정
is_adult = age >= 3 # is_adult 란 변수에 age >= 3 을 지정
print("우리집 강아지 이름은 우주에요") # print 는 출력을 위한 명령문이고 "우리집 강아지 이름은 우주에요" 를 출력
print("우주는 4살이며, 산책을 아주 좋아해요") # print 는 출력을 위한 명령문이고 "우주는 4살이며, 산책을 아주 좋아해요" 를 출력
print("우주는 어른일까요? True") # print 는 출력을 위한 명령문이고 "우주는 어른일까요? True" 를 출력

print("우리집" + animal + "이름은" + name + "에요") # print 는 출력을 위한 명령문이고 "우리집 강아지 이름은 우주에요" 를 출력
print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요") # print 는 출력을 위한 명령문이고 "우주는 4살이며, 산책을 아주 좋아해요" 를 출력
print(name + "는 어른일까요?" + str(is_adult)) # print 는 출력을 위한 명령문이고 "우주는 어른일까요? True" 를 출력

animal = "고양이" # animal 이란 변수에 "고양이" 로 지정
name = "보리" # name 이란 변수에 "보리" 로 지정
age = 2 # age란 변수에 2 로 지정
hobby = "터그놀이" # hobby란 변수에 "터크" 으로 지정
is_adult = age >= 3 # is_adult 란 변수에 age >= 3 을 지정


print("우리집" + animal + "이름은" + name + "에요") # print 는 출력을 위한 명령문이고 "우리집 고양이 이름은 보리에요" 를 출력
print(name + "는" + str(age) + "살이며," + hobby + "룰 아주 좋아해요") # print 는 출력을 위한 명령문이고 "보리는 2살이며, 터그놀이를 아주 좋아해요" 를 출력
print(name + "는 어른일까요?" + str(is_adult)) # print 는 출력을 위한 명령문이고 "보리는 어른일까요? False" 를 출력


# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명: station
# 변수값: "사당", "신도림", "인천공항" 순으로 입력

# 출력문장: xx행 열차가 들어오고 있습니다.

station = "사당" # 변수 station에 "사당"을 지정
print(station + "행 열차가 들어오고 있습니다.") # print는 출력을 위한 명령문이고 "사당행 열차가 들어오고 있습니다"
station = "신도림" # 변수 station에 "신도림"을 지정
print(station + "행 열차가 들어오고 있습니다.") # print는 출력을 위한 명령문이고 "사당행 열차가 들어오고 있습니다"
station = "인천공항" # 변수 station에 "인천공항"을 지정
print(station + "행 열차가 들어오고 있습니다.") # print는 출력을 위한 명령문이고 "사당행 열차가 들어오고 있습니다"
