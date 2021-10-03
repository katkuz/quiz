import random

# Questions and answers
questionsAndAnswers = [
      ("Vilken funktion används för att skriva ut saker på skärmen?", "print"),
      ("Vad heter nyckelordet för att göra en loop i Python?", "for"),
      ("Hur tar man fram längden på listan i variabeln \"fruits\"?", "list(fruits)"),
      ("fråga4", "svar4"),
      ("fråga5", "svar5"),
      ("fråga6", "svar6"),
      ("fråga7", "svar7"),
      ("fråga8", "svar8"),
      ("fråga9", "svar9"),
      ("fråga10", "svar10"),
      ("fråga11", "svar11"),
      ("fråga12", "svar12"),
      ("fråga13", "svar13"),
      ("fråga14", "svar14"),
      ("fråga15", "svar15"),
      ("fråga16", "svar16"),
      ("fråga17", "svar17"),
      ("fråga18", "svar18"),
      ("fråga19", "svar19"),
      ("fråga20", "svar20")
      ]

askedQuestions = list()  # list of already asked questions to avoid duplicate questions
questionsCount = len(questionsAndAnswers) # amount of questions and answers

# main program
print("Välkommen till quizen. Vi ska ställa 5 frågor om Python.\nNu kör vi!\n")

#pick up question from qa which is not already in askedQuestions
index = int

for x in range(0, 5):
      while True:
            index = random.randint(0, questionsCount - 1)
            if index not in askedQuestions:
                  break
      print(f"Question #{x+1}: {questionsAndAnswers[index][0]}")
      askedQuestions.append(index)
      answer = input("Ditt svar: ").strip()
      if answer == questionsAndAnswers[index][1]:
            print("Rätt!")
      else:
            print("Fel!")

print("done")