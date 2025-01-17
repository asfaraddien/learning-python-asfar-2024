
class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def masih_lanjut(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").title()
        self.cek(user_answer, current_question.answer)

    def cek(self, user_answer, jawaban_benar):
        if user_answer == jawaban_benar:
            print("Benar!")
            self.score += 1
        else:
            print("Salah!")
        print(f"yang benar ialah {jawaban_benar}\nSkor kamu {self.score}/{self.question_number}\n")






