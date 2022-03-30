from game_data import data
import random
print("Wellcome!\n The game name is Higher or Lower. \nThis game is all about the followers of some social media accounts. \nlet's start the game! ")
q1=random.choice(data)
q2=random.choice(data)
answer_is_correct=True
score=0
while answer_is_correct:
    q1equalq2=True
    while q1equalq2:
        if q1==q2:
            q2=random.choice(data)
        else:
            q1equalq2=False
    
    print(f'{q1["name"]},a {q1["desription"]},from {q1["country"]}')
    print("vs")
    print(f'{q2["name"]},a {q2["desription"]},from {q2["country"]}')
    ans=input("The followers of first addressed account is 'Higher' or 'Lower' than the second account:\n").lower()
    if ans=="higher" and q1["followers"]>q2["followers"]:
        score+=1
        print(f"Your guess is right! \nyour score is {score}")
        q1=q2
    if ans=="lower" and q1["followers"]<q2["followers"]:
        score+=1
        print(f"Your guess is right! \nyour score is {score}")
        q1=q2
    if ans!="higher" and q1["followers"]>q2["followers"]:
        print(f"Your guess is wrong!")
        answer_is_correct=False
    if ans!="lower" and q1["followers"]<q2["followers"]:
        print(f"Your guess is wrong!")
        answer_is_correct=False
print(f'your total score: {score}')
        



