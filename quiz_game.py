# 1. 메뉴를 화면에 출력
# 2. 사용자 번호 입력받기
# 3. 번호에 따라 동작 (지금은 "선택됨" 메시지만 출력해도 OK)
# 4. 5번 입력 시 종료
# 5. 잘못된 입력 처리

# 1) 클래스는 맨 위에 한 번만 정의
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for i, c in enumerate(self.choices, start=1):
            print(f"{i}. {c}")   # "1. 1개" 형태로 출력

    def check(self):
        user = input("정답 번호를 입력하세요: ")
        try:
            number = int(user)        # 숫자 변환 시도
        except ValueError:            # 변환 실패하면 여기로!
            print("⚠️  숫자를 입력해주세요.")
            return False

        if number == self.answer:
            print("정답입니다! 🎉")
            return True
        else:
            print(f"틀렸어요. 정답은 {self.answer}번이에요. 😢")
            return False

# 2) 메뉴 함수
def show_menu():
    print("===== 자전거 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")

# 3) 퀴즈 데이터 준비 (루프 전에 미리)
q = Quiz("자전거 바퀴는 몇 개?", ["1개", "2개", "3개", "4개"], 2)

# 4) 메인 루프
while True:
    show_menu()
    choice = input("번호를 선택하세요: ")

    if choice == "5":
        print("게임을 종료합니다. 안녕히 가세요! 👋")
        break
    elif choice == "1":
        print("👉 퀴즈 풀기를 선택했습니다.")
        q.show()        # 문제 보여주고
        q.check()       # 답 확인하기
    elif choice == "2":
        print("👉 퀴즈 추가를 선택했습니다.")
    elif choice == "3":
        print("👉 퀴즈 목록을 선택했습니다.")
    elif choice == "4":
        print("👉 점수 확인을 선택했습니다.")
    else:
        print("⚠️  1~5 사이의 번호를 입력해주세요.")

# 데이터만 넣어서 문제를 여러 개 생성 (코드 중복 없음!)
# q2 = Quiz("대전광역시 공영자전거 이름은?", ["타슬라", "타슈", "어울링", "따릉이"], 2)


