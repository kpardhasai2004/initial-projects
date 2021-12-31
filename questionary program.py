def question():
    rules=input("You need to answer every question by yes or no Do you understand: ")
    if rules!="yes":
        return print("Try again")
    else:print("Next question")
    Quest1=input("Are you thirsty: ")
    if Quest1!="yes":
        return print("Then let's go for walk")
    else:print("Next question")
    Quest2=input("Do you want to drink at restaurant: ")
    if Quest2!="yes":
        return print("Come drink at my place")
    else:print("Next question")
    Quest3=input("Do you want to drink a cola: ")
    if Quest3!="yes":
        return print("let's go to drink milk then")
    else:print("let's go to drink cola")

question()