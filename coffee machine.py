
# penny=0.01
# dime=0.10
# nickel=0.05
# quarter=0.25
total=0
def totmoney():
    global total
    nfpenny=(input("No of pennies: "))
    nfdime=(input("No of dime: "))
    nfnickel=(input("No of nickel: "))
    nfquarter=(input("No of quarter: "))
    if nfpenny=="":
        nfpenny=0
    if nfdime=="":
        nfdime=0
    if nfnickel=="":
        nfnickel=0
    if nfquarter=="":
        nfquarter=0
    total+=((0.01*int(nfpenny))+(0.10*int(nfdime))+(0.05*int(nfnickel))+(0.25*int(nfquarter)))
    # print(total)
#print(resources["water"])
menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
        },"cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },"cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":24,
            "coffee":24
        },"cost":3.0
    }
}
resources={"water":300,"milk":200,"coffee":100}
needed=input("What do you want? (espresso/latte/cappuccino): ")
if needed=="report":
    print(*[str(k) + '=' + str(v) for k,v in resources.items()], sep='\n')
elif needed=="espresso":
    totmoney()
    if menu["espresso"]["cost"]==total or  menu["espresso"]["cost"]<=total:
        if menu["espresso"]["cost"]<total:
            print("Change is refunded successfully!")
        if menu["espresso"]["ingredients"]["water"] <= resources["water"] and menu["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            print("Here is your espresso.Thank you!")
            menu["espresso"]["ingredients"]["water"] - resources["water"]
            menu["espresso"]["ingredients"]["coffee"] - resources["coffee"]
        else: print("Insufficent resources.")
    if menu["espresso"]["cost"]>total:
        print("Insufficent money!\nMoney refunded succefully.")
elif needed=="latte":
    totmoney()
    if menu["latte"]["cost"]==total or menu["latte"]["cost"]<=total:
        if menu["latte"]["cost"]<total:
            print("Change is refunded successfully!")
        if menu["latte"]["ingredients"]["water"] <= resources["water"] and menu["latte"]["ingredients"]["coffee"] <= resources["coffee"] and menu["latte"]["ingredients"]["milk"] <= resources["milk"]:
            print("Here is your latte.Thank you!")
            menu["latte"]["ingredients"]["water"] - resources["water"]
            menu["latte"]["ingredients"]["coffee"] - resources["coffee"]
            menu["latte"]["ingredients"]["milk"] - resources["milk"]
    if menu["latte"]["cost"]>total:
        print("Insufficent money!\nMoney refunded succefully.")
    
elif needed=="cappuccino":
    totmoney()
    if menu["cappuccino"]["cost"]==total or menu["cappuccino"]["cost"]<=total:
        if menu["cappuccino"]["cost"]<total:
            print("Change is refunded successfully!")
        if menu["cappuccino"]["ingredients"]["water"] <= resources["water"] and menu["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"] and menu["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
            print("Here is your espresso.Thank you!")
            menu["cappuccino"]["ingredients"]["water"] - resources["water"]
            menu["cappuccino"]["ingredients"]["coffee"] - resources["coffee"]
            menu["cappuccino"]["ingredients"]["milk"] - resources["milk"]
    if menu["cappuccino"]["cost"]>total:
        print("Insufficent money!\nMoney refunded succefully.")
elif needed!="report" or needed!="espresso" or needed!="latte" or needed!="cappuccino":
    print("Please check the input!")


