from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

game = QuizBrain(question_bank)
while game.still_has_question():
    game.next_question()
if not game.still_has_question():
    print("Congratulations! You've completed the quiz")
    print(f"Your final score is {game.score}/{len(game.question_list)}")