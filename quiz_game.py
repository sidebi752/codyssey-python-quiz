# 1. 메뉴를 화면에 출력
# 2. 사용자 번호 입력받기
# 3. 번호에 따라 동작 (지금은 "선택됨" 메시지만 출력해도 OK)
# 4. 5번 입력 시 종료
# 5. 잘못된 입력 처리

def show_menu():
    print("===== 자전거 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")

while True:
    show_menu()
    choice = input("번호를 선택하세요: ")

    if choice == "5":
        print("게임을 종료합니다. 안녕히 가세요! 👋")
        break
    elif choice == "1":
        print("👉 퀴즈 풀기를 선택했습니다.")
    elif choice == "2":
        print("👉 퀴즈 추가를 선택했습니다.")
    elif choice == "3":
        print("👉 퀴즈 목록을 선택했습니다.")
    elif choice == "4":
        print("👉 점수 확인을 선택했습니다.")
    else:
        print("⚠️  1~5 사이의 번호를 입력해주세요.")