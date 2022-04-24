from question_model import Question
from data import *
from quiz_brain import QuizBrain

from ui import UiQuiz

question_bank = []
for i in range(len(data["results"])):
    question_text = data["results"][i]["question"]
    question_answer = data["results"][i]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = UiQuiz(quiz)

