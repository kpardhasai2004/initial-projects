
def add(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
    return n*m
def div(n,m):
    return n/m
def sqroot(n):
    return n**0.5

def calculator():
    n=float(input("give the number 1: "))
    calc_obj={"+":add,
    "-":sub,
    "*":mul,
    "/":div,
    "√":sqroot
        }
    save_answer=True
    while save_answer:
        x=input("select on of these:\n+\n-\n*\n/\n√\n")
        if x!="√":
            m=float(input("give a number 2: "))
        if x=="+":
            y=add(n,m)
        elif x=="-":
            y=sub(n,m)
        elif x=="*":
            y=mul(n,m)
        elif x=="/":
            y=div(n,m)
        else:
            y=sqroot(n)
        answer=y
        print(answer)
        if input("do you want to save answer 'yes' or 'no' : ")=="yes":
            n=y
        else:
            save_answer=False
    print(answer)

shall_we_continue=True
while shall_we_continue:
    calculator()
    z=input("shall we continue 'yes' or 'no': ")
    if z=='no':
        shall_we_continue=False
        print("Thank you")