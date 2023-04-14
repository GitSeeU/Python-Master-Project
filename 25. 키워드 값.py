def profile(name, age, main_lang): # 함수를 정의
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20) # 유재석 20 파이썬 출력, 함수를 정의할때에 순서에 맞추어 재정리됨
profile(main_lang = "파이썬", age = 20, name = "조세호") # 조세호 20 파이썬 출력, 함수를 정의할때에 순서에 맞추어 재정리됨