from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question = self.canvas.create_text(150, 150,text="QUESTION", font=("Ariel", 24, "normal"), width=280)

        self.score = Label(text="Score: 0", font=("Arial", 12, "bold"), bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.score.grid(column=1, row=0)
        self.score.config(padx=20, pady=20)

        self.correct = PhotoImage(file="quiz_game/images/true.png")
        self.correct_button = Button(image=self.correct, highlightthickness=0, command=self.correct_q)
        self.correct_button.grid(column=0, row=2, pady=20)

        self.wrong = PhotoImage(file="quiz_game/images/false.png")
        self.wrong_button = Button(image=self.wrong, highlightthickness=0, command=self.false_q)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You completed the quiz!")
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")

    def false_q(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def correct_q(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_q)