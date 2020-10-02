"""Simple quiz| by Rajan Tamang"""
import sys
import time
from time import sleep

import requests
import pyfiglet
ascii_banner =pyfiglet.figlet_format("Welcome! Be ready to test your knowledge")

quizAPI = ("https://opentdb.com/api.php?amount=50&category=18&type=multiple")
result = requests.get(quizAPI).json()

global balance
global lives

global exit_prompt
global question_bank
question_bank=[]
# function to show welcome message along with the instruction
def showInstruction():
    print(ascii_banner)
    sleep(1)
    print("Please read the rule carefully")
    sleep(1)
    print("Quiz have three different level: easy, medium and hard")
    sleep(1)
    print("Points are earned based on question difficulty.")
    sleep(1)
    print("Points for getting easy questions' correct answer: 10")
    sleep(1)
    print("Points for getting medium questions' correct answer: 25")
    sleep(1)
    print("Points for getting hard questions' correct answer: 50")
    sleep(1)
    exit_prompt = input("Do you want to quit and run away? Press 'q' to quit. Any key to continue...: ")
    animation = "|/-\\"

    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print ("Are you Ready!")
    if exit_prompt != 'q':
        startGame()




# function to create easy level with questions that are easy from API alsong with the options and prompt user to answer
def easyLevel(balance,lives, question_bank, level):
            for easy in result['results']:
                game_over(lives)
                if easy['difficulty'] == level:
                    question_easy=easy['question']

                    if question_easy not in question_bank:
                        print(question_easy)
                        question_bank.append(question_easy)
                        rightanswer=str(easy['correct_answer']).lower()

                        answer=[]
                        answer.append(rightanswer)
                        wronganswer=(easy['incorrect_answers'])

                        for options in wronganswer: # iterate in wronganswer list and add each element to answer
                            answer.append(options)
                        for numberlist in answer:
                            print(answer.index(numberlist) + 1, end='')
                            print("", numberlist)
                        userAnswer=str(input("Enter answer: ")).lower()

                        if userAnswer.strip()==rightanswer.strip():
                            balance +=10
                            print(f"Correct Answer!, Your balance is {balance}")
                        else:
                            print("Wrong answer!")
                            lives -=1
                            print("Remaining lives:", lives)

                        break

#function to create medium level with questions that are medium from API along with the options and prompt user to answer
def mediumLevel(balance, lives,question_bank, level):
        for medium in result['results']:
            # if lives == 0:
            #     sys.exit()
            game_over(lives)
            if medium['difficulty']==level:
                question_medium = medium['question']
                if question_medium not in question_bank:
                    print(question_medium)
                    question_bank.append(question_medium)
                    rightanswer=str(medium['correct_answer']).lower()
                    answer=[]
                    answer.append(medium['correct_answer'])
                    wronganswer=(medium['incorrect_answers'])

                    for option in wronganswer: # iterates over each element in wronganswer list and add to answer
                        answer.append(option)

                    for numberlist in answer:
                        print(answer.index(numberlist)+1, end='')
                        print("",numberlist)

                        # prompt user to answer
                    userAnswer= input("Enter answer: ").lower()
                    if userAnswer==rightanswer: # check if the user input is equal to the correct answer
                        balance += 25
                        print(f"Correct answer! your total balance is {balance}")
                    else:
                        print("wrong answer")
                        lives -=1
                        print(lives)
                    break

# function to execute game over
def game_over(lives):
    if lives ==0:
        print("Game over!")
        sys.exit()


# function to create hard level with questions that are hard from API along with the options and prompt user to answer
def hardLevel(balance, lives, question_bank, level):
        for hard in result['results']:
            # if lives == 0:
            #     sys.exit()
            game_over(lives)
            if hard['difficulty']== level:
                question_hard = hard['question']
                if question_hard not in question_bank:
                    print(question_hard)
                    question_bank.append(question_hard)
                    answer=[]
                    rightanswer=str(hard['correct_answer']).lower()
                    answer.append(hard['correct_answer'])
                    wronganswer=(hard['incorrect_answers'])
                    for option in wronganswer: # iterates over each element in wronganswer list and add to answer
                        answer.append(option)

                    for numberlist in answer:
                        print(answer.index(numberlist)+1, end='')
                        print("",numberlist)

                        #prompt user to input answer
                    userAnswer = input("Enter answer: ").lower()
                    if userAnswer==rightanswer:
                        balance +=50
                        print(f"Correct Answer! your total balance is {balance}")
                    else:
                        print("Wrong Answer")
                        lives -= 1
                        print("Remaining lives: ", lives)


                    break

def startGame():
    lives =3
    while lives!=0:
        balance=0
        game_over(lives)

        try:
            selectLevel=input("Please select a level: easy, medium or hard or 'q' to quit: ").lower()
            if selectLevel =="easy":
                easyLevel(balance,lives,question_bank,selectLevel)
            if selectLevel == "medium":
                mediumLevel(balance,lives,question_bank,selectLevel)
            if selectLevel == "hard":
                hardLevel(balance,lives,question_bank,selectLevel)
            if selectLevel=="q".lower():
                sys.exit()
        except Exception as e:
            print(e)


def main():
    showInstruction()

if __name__ == '__main__':
    main()
