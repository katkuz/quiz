import random
import time
import json

# Read questions and answers from json with utf-8 encoding
questionsAndAnswers = json.load(open('data.json', 'r', encoding='utf-8'))

askedQuestions = list()  # list of already asked questions to avoid duplicate questions
questionsCount = len(questionsAndAnswers) # amount of questions and answers

# main program
print("Välkommen till quizen. Vi ska ställa 10 frågor om Python.\n"
        "Du får 5 poäng om du svarar korrekt inom 10 sekunder\n"
        "Du får 4 poäng om du svarar korrekt inom 20 sekunder\n"
        "Du får 3 poäng om du svarar korrekt inom 30 sekunder\n"
        "Du får 2 poäng om du svarar korrekt inom 40 sekunder\n"
        "Du får 1 poäng om du svarar korrekt efter 40 sekunder\n"
        "Nu kör vi!\n")

index = int             # index of question from json file
totalPoint = 0          # total points for the game
totalCorrectAnswer = 0  # total correct answers for the game

for x in range(0, 10):
    while True:
        index = random.randint(0, questionsCount - 1)
        if index not in askedQuestions:
            break
    print(f"Fråga #{x+1}: {questionsAndAnswers[index]['question']}")

    option_number = 1
    correct_options = list()
    shuffled_answers = questionsAndAnswers[index]['options']
    random.shuffle(shuffled_answers)
    for option in shuffled_answers:
        print(f"{option_number}: {option['text']}")
        if option['correct']:
            correct_options.append(option_number)
        option_number +=1

    askedQuestions.append(index)
    startTime = int(time.time())                    # get unix time before question

    try:
        answer = int(input("Ditt svar: ").strip()) # strip in order to avoid "space" problem
    except:
        answer = 0                                  #if not number set to 0 to simulate incorrect answer

    finishTime = int(time.time())                   # get unix time after question
    answerTime = finishTime - startTime
    if answer in correct_options:
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
        print(f"Rätt! Du svarade på {answerTime} sekunder och får {currentPoint} poäng!\nDu har {totalPoint} poäng totalt!")
    else:
        print(f"Fel! Du får 0 poäng.\nDu har {totalPoint} poäng totalt!")

print(f"\nGrattis!\nDu har svarat korrekt på {totalCorrectAnswer} frågor! Du har fått {totalPoint} poäng!")