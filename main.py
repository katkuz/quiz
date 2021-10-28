import random
import sys
import time
import requests
import json

questionsAndAnswers = list()
# questionsAndAnswers = json.load(open('data.json', 'r', encoding='utf-8'))['questions'] #keeping it for local debugging

try:
    response_API = requests.get('https://bjornkjellgren.se/quiz/v1/questions')
    questionsAndAnswers = json.loads(response_API.text)['questions']

except:
    print("Can't get questions and answers. Quitting")
    sys.exit()

askedQuestions = list()  # list of already asked questions to avoid duplicate questions
wrongAnsweredQuestions = list()  # list of wrong answered questions
questionsCount = len(questionsAndAnswers)  # amount of questions and answers

# main program
print("Välkommen till quizen! \n\n"
      "--------------Regler--------------\n"
      "Vi ska ställa 10 frågor om Python.\n"
      "Du få svara med ett eller flera alternativ för varje fråga.\n"
      "Flera alternativ skriver du separerat med komma. \n"
      "Alla korrekta svar ska vara valda för att räkna svar som korrekt. \n"
      "Du får 5 poäng om du svarar korrekt inom 10 sekunder\n"
      "Du får 4 poäng om du svarar korrekt inom 20 sekunder\n"
      "Du får 3 poäng om du svarar korrekt inom 30 sekunder\n"
      "Du får 2 poäng om du svarar korrekt inom 40 sekunder\n"
      "Du får 1 poäng om du svarar korrekt efter 40 sekunder\n"
      "----------------------------------\n\n"
      "Nu kör vi!\n")

index = int  # index of question from json file
totalPoint = 0  # total points for the game
totalCorrectAnswer = 0  # total correct answers for the game

for x in range(0, 10):
    while True:
        index = random.randint(0, questionsCount - 1)
        if index not in askedQuestions:
            break
    print(f"Fråga #{x + 1} (id: {questionsAndAnswers[index]['id']}): {questionsAndAnswers[index]['prompt']}")

    answer_number = 1
    correct_answers = list()
    shuffled_answers = questionsAndAnswers[index]['answers']
    random.shuffle(shuffled_answers)
    for answer in shuffled_answers:
        print(f"{answer_number}: {answer['answer']}")
        if answer['correct']:
            correct_answers.append(answer_number)
        answer_number += 1

    askedQuestions.append(index)
    startTime = int(time.time())  # get unix time before question
    given_answers = list()

    try:
        given_answer_txt = input("Ditt svar: ").strip()  # strip in order to avoid "space" problem
        if "," in given_answer_txt:
            given_answers = [int(x.strip()) for x in
                             given_answer_txt.split(',')]  # strip in order to avoid "space" problem
        else:
            given_answers.append(int(given_answer_txt))
    except:
        pass

    finishTime = int(time.time())  # get unix time after question
    answerTime = finishTime - startTime
    is_all_answers_correct = True

    for correct_answer in correct_answers:
        if correct_answer not in given_answers:
            is_all_answers_correct = False
            break

    if is_all_answers_correct and len(correct_answers) != len(given_answers):
        is_all_answers_correct = False

    if is_all_answers_correct:
        currentPoint = int
        totalCorrectAnswer += 1
        if answerTime <= 10:
            currentPoint = 5
        elif answerTime <= 20:
            currentPoint = 4
        elif answerTime <= 30:
            currentPoint = 3
        elif answerTime <= 40:
            currentPoint = 2
        else:
            currentPoint = 1
        totalPoint += currentPoint
        print(
            f"Rätt! Du svarade på {answerTime} sekunder och får {currentPoint} poäng!\nDu har {totalPoint} poäng totalt!\n")
    else:
        wrongAnsweredQuestions.append(index)
        print(f"Fel! ", end='')
        print("Rätt svar: ", end='')
        correctAnswerFound = False
        i = 1
        for answer in shuffled_answers:
            if answer['correct']:
                if correctAnswerFound:
                    print("; ", end='')
                print(str(i) + ") " + answer['answer'], end='')
                correctAnswerFound = True
            i = i + 1
        print("")
        print(f"Du får 0 poäng.\nDu har {totalPoint} poäng totalt!\n")

print(f"\nGrattis!\nDu har svarat korrekt på {totalCorrectAnswer} frågor! Du har fått {totalPoint} poäng!")