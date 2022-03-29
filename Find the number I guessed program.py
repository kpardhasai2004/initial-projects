import random

def guessit():
    global attempts
    guess=int(input("Now guess the number: "))
    if guess==cn:
        print("You won!")
        game_complete=True
    elif guess>cn:
        print("Your guess is high!")
        attempts-=1
        print(f'left attempts: {attempts}')
    elif guess<cn:
        print("Your guess is low!")
        attempts-=1
        print(f'left attempts: {attempts}')

print("Welcome to the number guessing game!")
print("I am thinking a number between 1 to 100")
cn=random.randint(1,100)
# print(cn)
req_level=input("Choose the difficulty: \n'easy' or 'hard'\n")
if req_level=="easy":
    attempts=10
elif req_level=="hard":
    attempts=5
# print(attempts)
game_complete = False
while not game_complete:
    if attempts>0:
        guessit()
    elif attempts==0:
        print("You lost!")
        game_complete=True




