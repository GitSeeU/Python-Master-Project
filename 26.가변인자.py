# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " "를 사용함으로써 문장이 출력된후 이어서 밑에 문장을 출력함
#     print(lang1, lang2, lang3, lang4, lang5) # profile에 해당되는 값을 출력


def profile(name, age, *language): # 가변인자를 사용하기 위해 *language을 써서 lang1~6을 생략하고 언어 이름들을 넣어줌
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " "를 사용함으로써 문장이 출력된후 이어서 밑에 문장을 출력함
    for lang in language: # for문을 써서 lang이라는 변수를 만들어 language안에 포함된 것들을 하나씩 출력
        print(lang, end =" ") # 줄바꿈을 하지 않기위해 end =" " 추가
    print() # 줄바꿈을 위해 넣어줌

profile("유재석", 20, "python", "java", "C", "C++", "C#", "javascript")
profile("유재석", 25, "kotlin", "swift", "", "", "")