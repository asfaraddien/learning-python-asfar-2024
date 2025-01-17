from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.masih_lanjut():
    quiz.next_question()

print(f"Skor akhirmu adalah: {quiz.score}/{quiz.question_number}")
