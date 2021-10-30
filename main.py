from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.questions_remaining():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}")



