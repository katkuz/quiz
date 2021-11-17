import random
from api import send_statistics


def is_all_answers_correct(correct_answers_list, given_answers):
    """ Return true if all selected options are correct, otherwise false """
    for correct_answer in correct_answers_list:
        if correct_answer not in given_answers:
            return False
    if len(correct_answers_list) != len(given_answers):
        return False
    return True


def correct_answers(shuffled_answers):
    """ Return correct options in list from all possible options """
    answer_number = 1
    correct_answers_list = list()
    for answer in shuffled_answers:
        from printing import print_answers
        print_answers(answer_number, answer)
        if answer['correct']:
            correct_answers_list.append(answer_number)
        answer_number += 1
    return correct_answers_list


def calculate_correct_percent(times_correct, times_asked):
    """ Return percent of whom answered correct for the question """
    try:
        if times_correct <= times_asked:
            return int((times_correct / times_asked) * 100)
    except ZeroDivisionError:
        pass
    return -1


def count_points(answer_time):
    """ Return awarded points based on how much time elapsed """
    if answer_time < 0:
        return 0
    elif answer_time <= 10:
        return 5
    elif answer_time <= 20:
        return 4
    elif answer_time <= 30:
        return 3
    elif answer_time <= 40:
        return 2
    else:
        return 1


def get_next_question_index(questions_and_answers, asked_questions):
    """ Get index of next question to work with which is not asked yet """
    amount_of_questions = len(questions_and_answers)
    while True:
        index = random.randint(0, amount_of_questions - 1)
        if index not in asked_questions:
            break
    asked_questions.append(index)
    return index


def answers_check(
        correct_answers_list, answer_time, total_points,
        total_correct_answers, given_answers,
        shuffled_answers, questions_and_answers,
        current_question_index, wrong_answered_questions):
    """ Check if given answer(s) are correct, send statistics,
    print info and calculate total points for the user """
    from printing import correct_answer, incorrect_answer
    if is_all_answers_correct(correct_answers_list, given_answers):
        total_correct_answers += 1
        current_point = count_points(answer_time)
        total_points += current_point
        send_statistics(
            questions_and_answers[current_question_index]['id'], True)
        correct_answer(answer_time, current_point, total_points)
    else:
        wrong_answered_questions.append(current_question_index)
        send_statistics(
            questions_and_answers[current_question_index]['id'], False)
        incorrect_answer(shuffled_answers, total_points)
    return total_points, total_correct_answers


def get_answers(questions_and_answers, current_question_index):
    """ Return shuffled options for selected question """
    answers = questions_and_answers[current_question_index]['answers']
    random.shuffle(answers)
    return answers
