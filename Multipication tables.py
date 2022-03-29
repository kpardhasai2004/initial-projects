n=int(input("Multiplication table you want: "))
z=int(input("The largest number that has to be multiplied: "))
for x in range (1,z+1):
    y=n*x
    print(f'{n}*{x}={y}')