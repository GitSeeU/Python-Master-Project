python = "Python is Amazing"
print(python.lower()) # python is amazing 출력
print(python.upper()) # PYTHON IS AMAZING 출력
print(python[0].isupper()) # 0번째 자리에 글자가 대문자인가, True 출력
print(len(python)) # 몇 글자인가 17 출력
print(python.replace("Python", "Java")) # Java is Amazing 출력

index = python.index("n") #python에서 n이 몇번째 자리에 있나 
print(index) # 5 출력
index =python.index("n", index + 1) # 찾는값, 시작값이고 찾는값에 +1해서 시작 
print(index) # 15 출력

print(python.find("n")) # find는 원하는 걸 찾는함수 5출력
print(python.find("Java")) # 원하는 값이 변수에 없을때 -1 반환
#print(python.index("Java")) #원하는 값이 변수에 없을때 오류 및 프로그램 종료
print("hi")

print(python.count("n")) #python이란 변수에서 n이 총 몇번 등장하는지 센다, 2출력