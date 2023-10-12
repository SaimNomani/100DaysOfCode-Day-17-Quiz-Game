from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for n in range(0, len(question_data)):
    question_data[n] = Question(question_data[n]['text'], question_data[n]['answer'])
    question_bank.append(question_data[n])
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score is: {quiz.user_score}/{quiz.question_number}")
