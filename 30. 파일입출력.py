# score_file = open("score.txt", "w", encoding = "utf8") # open 을 통해서 파일을 열어줌, "score.txt" = 파일이름, "w" 이 파일은 쓰기위한 목적정의, encoding = "utf8" -> 한글을 썻을때 에러방지
# print("수학 : 0", file = score_file) # 파일에 작성될 내용
# print("영어 : 50", file = score_file) # 파일에 작성될 내용
# score_file.close() # 작성한후 파일을 닫아라

# score_file = open("score.txt", "a", encoding = "utf8") # "a" = append 이미 있는파일에 내용을 추가
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8") # "r" = read 
# print(score_file.read()) # 파일에 잇는 모든 내용을 불러와서 출력해줌
# score_file.close()   

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline()) # 줄별로 읽기, 한줄을 읽고나서 커서를 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close() 
