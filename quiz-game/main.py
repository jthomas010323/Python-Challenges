from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in range(len(question_data)):
    question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.retrieve()

print(f"Quiz is over, score is {quiz.score}/{quiz.question_number}")