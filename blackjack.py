import random
ptotal=0
ctotal=0
Q=10
K=10
J=10
pcards=[]
ccards=[]
cards=[11,2,3,4,5,6,7,8,9,10,Q,K,J]
p=random.choice(cards)
c=random. randint(6,11)
print(f'your card is {p}.')
print(f'computer card is {c}.')
pcards.append(p)
ccards.append(c)
deal_continue=True
while deal_continue:
    deal=input("Do you want to make a deal? \nif yes enter 'y' for stop and sum enter 'n': ")
    if deal=='y':
        p1=random.choice(cards)
        c1=random.choice(cards)
        pcards.append(p1)
        ccards.append(c1)
        print(pcards)
    else:
        deal_continue=False
for pvalue in range(0,len(pcards)):
    ptotal=ptotal+pcards[pvalue]
for cvalue in range(0,len(ccards)):
    ctotal=ctotal+ccards[cvalue]

print(ptotal)
print(ctotal)

if 1>ctotal>21 or ctotal>ptotal:
    print("Better luck next time!")
if 1>ptotal>21 or ptotal>ctotal:
    print("You won!")
if ptotal>21:
    print ("You exceeded the value 21.")
if ptotal==ctotal:
    print("its a draw!")