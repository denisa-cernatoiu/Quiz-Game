class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        currrent_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {currrent_question.text} (True/False):? -> ")
        self.check_answer(user_answer, currrent_question.answer )

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() != correct_answer.lower():
          print("You are wrong!")
        
        else:
          self.score += 1
          print("You got it right!")
        
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
