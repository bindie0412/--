print("무슨 아이스크림을 드시고싶으신가요?")
print("1. 바닐라")
print("2. 초코")
print("3. 딸기")
print("4. 민트")
print("5. 커피")
answer = input("번호를 입력하세요: ")
if answer == "1":
    print("바닐라 아이스크림을 선택하셨습니다.")
elif answer == "2":
    print("초코 아이스크림을 선택하셨습니다.")
elif answer == "3":
    print("딸기 아이스크림을 선택하셨습니다.")
elif answer == "4":
    print("민트 아이스크림을 선택하셨습니다.")
elif answer == "5":
    print("커피 아이스크림을 선택하셨습니다.")
else:
    print("잘못된 선택입니다. 1부터 5까지의 번호를 입력해주세요.")