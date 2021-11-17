from logic import calculate_correct_percent


def welcome():
    """ Print rules of the quiz """
    print("Välkommen till quizen! \n\n"
          "--------------Regler--------------\n"
          "Vi ska ställa 10 frågor om Python.\n"
          "Du få svara med ett eller flera alternativ för varje fråga.\n"
          "Flera alternativ skriver du separerat med komma. \n"
          "Alla korrekta svar ska vara valda för att räkna "
          "svar som korrekt. \n"
          "Du får 5 poäng om du svarar korrekt inom 10 sekunder\n"
          "Du får 4 poäng om du svarar korrekt inom 20 sekunder\n"
          "Du får 3 poäng om du svarar korrekt inom 30 sekunder\n"
          "Du får 2 poäng om du svarar korrekt inom 40 sekunder\n"
          "Du får 1 poäng om du svarar korrekt efter 40 sekunder\n"
          "----------------------------------\n\n"
          "Nu kör vi!\n")


def print_question(current_question, questions_and_answers,
                   current_question_index):
    """ Print current question with statistics if available """
    correct_percent = calculate_correct_percent(
        int(questions_and_answers[current_question_index]['times_correct']),
        int(questions_and_answers[current_question_index]['times_asked'])
    )
    if correct_percent < 0:
        # Print without correct percentage cause we can not calculate it
        print(
            f"Fråga #{current_question + 1} "
            f"[id: {questions_and_answers[current_question_index]['id']}]:"
            f" {questions_and_answers[current_question_index]['prompt']}")
    else:
        print(
            f"Fråga #{current_question + 1} "
            f"[id: {questions_and_answers[current_question_index]['id']}; "
            f"{correct_percent}% har svarat rätt]:"
            f" {questions_and_answers[current_question_index]['prompt']}")


def print_answers(answer_number, answer):
    """ Print selected option with option number """
    print(f"{answer_number}: {answer['answer']}")


def correct_answer(answer_time, current_point, total_points):
    """ Print time elapsed, current and total points if user answer correct"""
    print(
        f"Rätt! Du svarade på {answer_time} sekunder och får "
        f"{current_point} poäng!\nDu har {total_points} poäng totalt!\n")


def incorrect_answer(shuffled_answers, total_points):
    """ Print total points and correct answer if user answer incorrect"""
    correct_answer_found = False
    print("Fel! ", end='')
    print("Rätt svar: ", end='')
    i = 1
    for answer in shuffled_answers:
        if answer['correct']:
            if correct_answer_found:
                print("; ", end='')
            print(str(i) + ") " + answer['answer'], end='')
            correct_answer_found = True
        i = i + 1
    print("")
    print(f"Du får 0 poäng.\nDu har {total_points} poäng totalt!\n")


def final(questions_and_answers, wrong_answered_questions,
          total_correct_answers, total_points):
    """ Print final info: total points and all
    incorrect answered questions with correct answers """
    print(f"\nGrattis!\nDu har svarat korrekt på "
          f"{total_correct_answers} frågor! Du har fått {total_points} poäng!")
    if len(wrong_answered_questions) > 0:
        print("\nDu svarade fel på dessa frågor:")
        for index in wrong_answered_questions:
            print(f"- {questions_and_answers[index]['prompt']}")
            print("Rätt svar: ", end='')
            correct_answer_found = False
            for answer in questions_and_answers[index]['answers']:
                if answer['correct']:
                    if correct_answer_found:
                        print("; ", end='')
                    print(answer['answer'], end='')
                    correct_answer_found = True
            print("")
    else:
        print("\nDu svarade rätt på alla frågor. Vilken klippa du är!")
