import random
import time
import json

# Questions and answers
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

#pick up question from qa which is not already in askedQuestions
index = int
totalPoint = 0
totalCorrectAnswer = 0

for x in range(0, 10):
    while True:
        index = random.randint(0, questionsCount - 1)
        if index not in askedQuestions:
            break
    print(f"Question #{x+1}: {questionsAndAnswers[index]['question']}")
    askedQuestions.append(index)
    startTime = int(time.time())
    answer = input("Ditt svar: ").strip()
    finishTime = int(time.time())
    answerTime = finishTime - startTime
    if answer == questionsAndAnswers[index]['answer']:
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