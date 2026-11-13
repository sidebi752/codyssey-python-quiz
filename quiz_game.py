# 자전거 상식 퀴즈 게임 - Quiz(문제 1개), QuizGame(게임 진행) 클래스로 구성

# 1) 클래스는 맨 위에 한 번만 정의
import json
from pathlib import Path

STATE_FILE = Path(__file__).parent / "state.json" 

def get_text(prompt):
    """빈칸이 아닌 글자를 입력받을 때까지 반복해서 묻는다."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️  비어 있어요. 내용을 입력해주세요.")
            continue
        return text          # 통과하면 그 글자를 돌려주고 끝

def get_number(prompt, min_value, max_value):
    """min_value ~ max_value 사이의 정수를 받을 때까지 반복해서 묻는다."""
    while True:
        user = input(prompt).strip()

        if user == "":
            print("⚠️  입력이 비어 있어요. 번호를 입력해주세요.")
            continue

        try:
            number = int(user)
        except ValueError:
            print("⚠️  1~4 사이의 숫자를 입력해주세요.")
            continue

        if not min_value <= number <= max_value:
            print(f"⚠️  {min_value}~{max_value} 사이의 번호를 입력해주세요.")
            continue

        return number

def create_default_quizzes():
    """기본 퀴즈 목록을 만들어서 돌려준다."""
    return [
        Quiz("두발자전거의 바퀴는 몇 개?", ["1개", "2개", "3개", "4개"], 2),
        Quiz("대전광역시 공영자전거 이름은?", ["타슬라", "타슈", "어울링", "따릉이"], 2),
        Quiz("자전거 탈 때 사람이 착용하는 물건이 아닌 것은?", ["헬멧", "장갑", "우비", "타이어"], 4),
        Quiz("자전거의 주요 부품이 아닌 것은?", ["프레임", "바퀴", "핸들", "번호판"], 4),
        Quiz("다음 중 자전거 브랜드인 것은?", ["삼천리", "나이키", "칠곡", "코디세이"], 1),
    ]

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        """저장용: Quiz 객체 → 딕셔너리"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    def show(self):
        print(self.question)
        for i, c in enumerate(self.choices, start=1):
            print(f"{i}. {c}")   # "1. 1개" 형태로 출력

    def check(self):
        number = get_number("번호를 입력하세요: ", 1, len(self.choices))   # 1~4 사이의 숫자 입력

        if number == self.answer:
                print("정답입니다! 🎉")
                return True
        else:
                print(f"틀렸어요. 정답은 {self.answer}번이에요. 😢")
                return False
        
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()                     # 시작할 때 파일에서 불러오기

    def load(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.quizzes = []
            for item in data["quizzes"]:          # 딕셔너리 → Quiz 객체
                quiz = Quiz(item["question"], item["choices"], item["answer"])
                self.quizzes.append(quiz)
            self.best_score = data["best_score"]
            print(f"📂 저장된 데이터를 불러왔습니다. "
                  f"(퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")

        except FileNotFoundError:                 # ② 첫 실행
            print("📂 저장 파일이 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = create_default_quizzes()
            self.best_score = 0

        except (json.JSONDecodeError, KeyError, TypeError):   # ③ 손상
            print("⚠️  저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.quizzes = create_default_quizzes()
            self.best_score = 0

    def save(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],   # Quiz → 딕셔너리
            "best_score": self.best_score,
        }
        try:                                       # ④ 쓰기 오류 대비
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            print("⚠️  파일 저장에 실패했습니다.")                    # 최고 점수 (나중에 사용)

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
        print("📌 새로운 퀴즈를 추가합니다.")

        # ① 문제 (글자)
        question = get_text("문제를 입력하세요: ")

        # ② 선택지 4개 (글자 4번)
        choices = []
        for i in range(1, 5):
            choice = get_text(f"선택지 {i}: ")
            choices.append(choice)

        # ③ 정답 번호 (숫자 1~4)
        answer = get_number("정답 번호를 입력하세요 (1-4): ", 1, 4)

        # ④ Quiz 카드를 만들어서 묶음에 추가
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        # ⑤ 완료 메시지
        print(f"✅ 퀴즈가 추가되었습니다! (현재 총 {len(self.quizzes)}개)")
        
    def list_quizzes(self):
        if not self.quizzes:
            print("⚠️  등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return
        
        print(f"📋 등록된 퀴즈 목록: (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")
        print("-" * 40)

    def show_score(self):
        if self.best_score == 0:
            print("아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어보세요!")
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")

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

