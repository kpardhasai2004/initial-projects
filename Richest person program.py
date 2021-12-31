p1_n=input("what is your name: ")
p1_w=input("how much money do you have: ")

p2_n=input("what is your name: ")
p2_w=input("how much money do you have: ")

p3_n=input("what is your name: ")
p3_w=input("how much money do you have: ")

if float(p1_w)>float(p2_w) and float(p1_w)>float(p3_w):
    print( p1_n +" is the richest")

elif float(p2_w)>float(p1_w) and float(p2_w)>float(p3_w):
    print( p2_n +" is the richest")

elif float(p3_w)>float(p1_w) and float(p3_w)>float(p2_w):
    print( p3_n +" is the richest")