from data import question_data
from question_model import Question
import random
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    ii = question_data.index(i)
    new_q = Question(question_data[ii]["question"], question_data[ii]["correct_answer"])
    question_bank.append(new_q)

new_quiz_brain = QuizBrain(question_bank)

while new_quiz_brain.still_has_questions():
    new_quiz_brain.next_question()

print("You've completed the quiz.")    
print(f"Your final score is {new_quiz_brain.score}/{new_quiz_brain.question_number}")
