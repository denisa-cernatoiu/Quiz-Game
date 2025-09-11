class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.currrent_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q. {self.question_number}: {self.currrent_question.text}"

    def check_answer(self, user_answer):
        correct_answer = self.currrent_question.answer
        if user_answer.lower() != correct_answer.lower():
          return False
        else:
          self.score += 1
          return True
        