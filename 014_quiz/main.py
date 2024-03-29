from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question = Questions(q_text, q_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is now completed.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
