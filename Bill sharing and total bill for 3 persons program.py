name_1=input("name of the person 1  ")
name_2=input("name of the person 2  ")
name_3=input("name of the person 3  ")

total_price=input(" TOTAL PRICE OF MEAL ")

percentage_name_1=input("PERCENTAGE ATE BY " + name_1+" ")
percentage_name_2=input("PERCENTAGE ATE BY " + name_2+" ")
percentage_name_3=input("PERCENTAGE ATE BY " + name_3+" ")

price_of_name_1= float(total_price)*float(percentage_name_1)
price_of_name_2= float(total_price)*float(percentage_name_2)
price_of_name_3= float(total_price)*float(percentage_name_3)

print("price to be paid by " + name_1 + "is " +str (price_of_name_1))
print("price to be paid by " + name_2 + "is " +str (price_of_name_2))
print("price to be paid by " + name_3 + "is " +str (price_of_name_3))

result= float(price_of_name_1) + float(price_of_name_2) + float(price_of_name_3)

print("TOTAL AMOUNT TO BE PAID " + str(result))





