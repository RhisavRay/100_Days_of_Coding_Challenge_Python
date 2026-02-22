class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q{self.question_no} {question.question}?(True/False): ").capitalize()
        self.check_answer(answer, question.answer)

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_no}\n\n")