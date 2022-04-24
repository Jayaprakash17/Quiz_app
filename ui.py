from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UiQuiz:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.label1 = Label(text="Score : 0", fg="White", bg=THEME_COLOR, highlightthickness=0)
        self.label1.grid(column=1, row=0)
        self.label1.configure(padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, width=250,
                                            text="TEXT", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct = PhotoImage(file="true.png")
        wrong = PhotoImage(file="false.png")
        self.button1 = Button(image=correct, highlightthickness=0, command=self.answer_check1)
        self.button1.grid(column=0, row=2)

        self.button2 = Button(image=wrong, highlightthickness=0, command=self.answer_check2)
        self.button2.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="White")
        if self.quiz_brain.still_has_questions():
            self.label1.configure(text=f"Score : {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the Quiz ")
            self.button2.configure(state='disabled')
            self.button1.configure(state='disabled')

    def answer_check1(self):
        user_answer = "true"
        is_ans = self.quiz_brain.check_answer(user_answer)
        self.screen_pause(is_ans)

    def answer_check2(self):
        user_answer = "false"
        is_ans = self.quiz_brain.check_answer(user_answer)
        self.screen_pause(is_ans)

    def screen_pause(self, is_right):
        if is_right:
            self.canvas.configure(bg="Green")
        else:
            self.canvas.configure(bg="Red")
        self.window.after(1000, self.get_next_question)

