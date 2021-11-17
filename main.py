import time
from api import get_questions
from printing import welcome, print_question, final
from getting import get_user_answers
from logic import get_next_question_index, \
    get_answers, answers_check, correct_answers

questions_and_answers = get_questions()
asked_questions = list()
# list of already asked questions to avoid duplicate questions
given_answers = list()
# list of given answers
total_points = 0
# total points for the game
total_correct_answers = 0
# total correct answers for the game
wrong_answered_questions = list()
# list of wrong answered questions

welcome()

for current_question in range(0, 10):
    current_question_index = get_next_question_index(
        questions_and_answers, asked_questions)
    print_question(
        current_question, questions_and_answers, current_question_index)
    shuffled_answers = get_answers(
        questions_and_answers, current_question_index)
    correct_answers_list = correct_answers(shuffled_answers)
    start_time = int(time.time())  # get unix time before question
    given_answers = get_user_answers()
    finish_time = int(time.time())  # get unix time after question
    total_points, total_correct_answers = answers_check(
        correct_answers_list, finish_time - start_time,
        total_points, total_correct_answers, given_answers,
        shuffled_answers, questions_and_answers, current_question_index,
        wrong_answered_questions)

final(questions_and_answers, wrong_answered_questions,
      total_correct_answers, total_points)
