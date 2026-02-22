from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    Q = Question(question["text"],question["answer"])
    question_bank.append(Q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Your quiz is complete!")
print(f"Your score is {quiz.score}/{quiz.question_no}")