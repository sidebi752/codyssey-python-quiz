# 자전거 상식 퀴즈 게임 - Quiz(문제 1개), QuizGame(게임 진행) 클래스로 구성

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
        while True:
            user = input("정답 번호를 입력하세요: ").strip()
             # ① 빈 입력
            if user == "":
                print("⚠️  입력이 비어 있어요. 번호를 입력해주세요.")
                continue
             # ② 숫자 변환 실패 (abc, 1.5 등)   
            try:
                number = int(user)        # 숫자 변환 시도
            except ValueError:            # 변환 실패하면 여기로!
                print("⚠️  1~4 사이의 숫자를 입력해주세요.")
                continue
            # ③ 범위 밖 (0, 7, -1 등)
            if not 1 <= number <= len(self.choices):
                print(f"⚠️  1~{len(self.choices)} 사이의 번호를 입력해주세요.")
                continue
            
            break   # 여기까지 오면 정상 입력이므로 반복문 탈출

        if number == self.answer:
                print("정답입니다! 🎉")
                return True
        else:
                print(f"틀렸어요. 정답은 {self.answer}번이에요. 😢")
                return False

def create_default_quizzes():
    """기본 퀴즈 목록을 만들어서 돌려준다."""
    return [
        Quiz("두발자전거의 바퀴는 몇 개?", ["1개", "2개", "3개", "4개"], 2),
        Quiz("대전광역시 공영자전거 이름은?", ["타슬라", "타슈", "어울링", "따릉이"], 2),
        Quiz("자전거 탈 때 사람이 착용하는 물건이 아닌 것은?", ["헬멧", "장갑", "우비", "타이어"], 4),
        Quiz("자전거의 주요 부품이 아닌 것은?", ["프레임", "바퀴", "핸들", "번호판"], 4),
        Quiz("다음 중 자전거 브랜드인 것은?", ["삼천리", "나이키", "칠곡", "코디세이"], 1),
    ]

class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()   # 문제 카드 묶음
        self.best_score = 0                       # 최고 점수 (나중에 사용)

    def show_menu(self):
        print("===== 자전거 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def play(self):
        print("👉 퀴즈 풀기를 선택했습니다.")

        # 3) 퀴즈가 없으면 안내하고 돌아가기
        if not self.quizzes:
            print("⚠️  등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct = 0                      # 이번 판에 맞힌 개수 (매번 0부터)

        # 1) 맞은 개수 세기
        for quiz in self.quizzes:
            quiz.show()
            if quiz.check():             # 입력은 여기서 딱 한 번
                correct += 1

        # 2) 결과 출력 (반복문이 끝난 뒤 한 번만)
        score = correct * 100 // total   # 100점 만점으로 환산
        print("=" * 40)
        print(f" 결과: {total}문제 중 {correct}문제 정답! ({score}점)")

        if correct == total:
            print("🎉 모든 문제를 맞췄습니다! 축하합니다! 🎉")

        # 최고 점수는 판이 끝난 뒤 비교해서 갱신
        if score > self.best_score:
            self.best_score = score
            print("✨ 새로운 최고 점수입니다!")
        print("=" * 40)

    def add_quiz(self):
        print("👉 퀴즈 추가는 준비 중입니다.")

    def list_quizzes(self):
        print("👉 퀴즈 목록은 준비 중입니다.")

    def show_score(self):
        print("👉 점수 확인은 준비 중입니다.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("번호를 선택하세요: ").strip()

            if choice == "5":
                print("게임을 종료합니다. 안녕히 가세요! 👋")
                break
            elif choice == "1":
                self.play()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                self.show_score()
            else:
                print("⚠️  1~5 사이의 번호를 입력해주세요.")

if __name__ == "__main__":
    game = QuizGame()   # 진행자(게임 객체) 만들기
    game.run()          # 게임 시작
