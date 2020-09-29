"""Simple quiz| by Rajan Tamang"""
from time import sleep

import requests
import pyfiglet
ascii_banner =pyfiglet.figlet_format("Welcome! Be ready to test your knowledge")



quizAPI = ("https://opentdb.com/api.php?amount=50")
result = requests.get(quizAPI).json()
global balance
global lives
lives =3
global exit_prompt
# global answer
# global answer1
# global answer2

# function to show welcome message along with the instruction
def showInstruction():
    print(ascii_banner)
    sleep(1)
    print("Please read the rule carefully")
    sleep(1)
    exit_prompt = input("Do you want to quit and run away? Press 'q' to quit. Any key to continue")
    while exit_prompt !="q":
        startGame()
    game_over()
    print("You have option to choose, easy, medium or hard level")

# function to create easy level with questions that are easy from API alsong with the options and prompt user to answer
def easyLevel():
        for easy in result['results']:
            if easy['difficulty'] == "easy":
                print(easy['question'])
                rightanswer=(easy['correct_answer']).lower()
                answer1= []
                answer2=[]
                answer1.append(easy['correct_answer'])
                answer2.append(easy['incorrect_answers'])
                answer=[]
                answer = answer2.append(answer1)
                for numberlist in answer:

                    print(answer.index(numberlist)+1, end='')
                    print("",numberlist)


                userAnswer=input("Enter answer").lower()
                if userAnswer==rightanswer:
                    balance +=10
                    print(f"Correct Answer, Your balance is {balance}")
                else:
                    print("Wrong answer")
                    lives -=1


#function to create medium level with questions that are medium from API along with the options and prompt user to answer
def mediumLevel():
        for medium in result['results']:
            if medium['difficulty'] =="medium":
                print(medium['question'])
                rightanswer=(medium['correct_answer']).lower()
                answer=[]
                answer.append(medium['correct_answer'])
                answer.append(medium['incorrect_answers'])

                for numberlist in answer:

                    print(answer.index(numberlist)+1, end='')
                    print("",numberlist)
                userAnswer= input("Enter answer: ").lower()
                if userAnswer==rightanswer:
                    balance += 25
                    print(f"Correct answer! your total balance is {balance}")
                else:
                    print("wrong answer")
                    lives -=1


# function to execute game over
def game_over():
    if lives ==0 or exit_prompt=="q":
        print("Game over!")

        exit()


# function to create hard level with questions that are hard from API along with the options and prompt user to answer
def hardLevel():
        for hard in result['results']:
            if hard['difficulty']=="hard":
                print(hard['question'])
                answer=[]
                rightanswer=(hard['correct_answer']).lower()
                answer.append(hard['correct_answer'])
                answer.append(hard['incorrect_answers'])
                for numberlist in answer:

                    print(answer.index(numberlist)+1, end='')
                    print("",numberlist)
                userAnswer=input("enter answer: ").lower()
                if userAnswer==rightanswer:
                    balance += 50
                    print(f"Correct Answer, You have own {balance}")


                else:
                    print("Wrong answer!")
                    lives -=1




def startGame():
    try:
        selectLevel=input("Please select a level: easy, medium or hard: ").lower()

        if selectLevel=="easy":
            easyLevel()

        elif selectLevel=="medium":
            mediumLevel()
        elif selectLevel=="hard":
            hardLevel()
    except:
        print("Please select valid level")


def main():
    showInstruction()

if __name__ == '__main__':
    main()
