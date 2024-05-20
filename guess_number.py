# ----------------------------------------------------Guess the number(project)----------------------------------------------
import random

print("let me think of a number between 1 to 50'\n")

random_no = random.randint(1,50)
# print(random_no)

game_level = input("Choose level of difficulty....Type 'easy' or 'hard': ")
def easy_level():
        no_of_attempts=10
        end_loop = True
        while(end_loop):
                      print(f"You have {no_of_attempts} attempts remaining to guess the number!")
                      guess_no = int(input("Make a guess: "))
                      if(guess_no == random_no):
                          print(f"You guess correct no. The answer is {random_no}\nYou Win")
                          break
                      else:
                            if(guess_no < random_no):
                                print("Your Guess is Too Low\nGuess again!")
                                no_of_attempts =  no_of_attempts-1
                                if(no_of_attempts==0):
                                           print(f"You are out of guesses..........You lose!\ncorrect answer is {random_no}")
                                           
                                           end_loop=False
                            else:
                                print("Your Guess is too High\nGuess again!")
                                no_of_attempts =  no_of_attempts-1
                                if(no_of_attempts==0):
                                           print(f"You are out of guesses..........You lose!\ncorrect answer is {random_no}")
                                           end_loop=False
                                                                               
                                           
def hard_level():
    no_of_attempts=5
    end_loop = True
    while(end_loop):
                      print(f"You have {no_of_attempts} attempts remaining to guess the number!")
                      guess_no = int(input("Make a guess: "))
                      if(guess_no == random_no):
                          print(f"You guess correct no.The answer is {random_no}\nYou Win")
                          break
                      else:
                            if(guess_no < random_no):
                                print("Your Guess is too Low\nGuess again!")
                                no_of_attempts =  no_of_attempts-1
                                if(no_of_attempts==0):
                                           print(f"You are out of guesses..........You lose!\ncorrect no:{random_no}")
                                           end_loop=False
                            else:
                                print("Your Guess is too High\nGuess again!")
                                no_of_attempts =  no_of_attempts-1
                                if(no_of_attempts==0):
                                           print(f"You are out of guesses..........You lose!\ncorrect no:{random_no}")
                                           end_loop=False


                                           
if(game_level=="easy"):
    easy_level()
else:
    hard_level()
                       
