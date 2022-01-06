stu1_name=input("what is the name of 1st student ? ")

stu1_regno=input("what is the reg no of 1st student ? ")

stu1_sub_1=input("what are the marks of 1st subject ? ")

stu1_sub_2=input("what are the marks of 2nd subject ? ")

stu1_sub_3=input("what are the marks of 3rd subject ? ")

stu1_avgm= (float(stu1_sub_1)+float(stu1_sub_2)+float(stu1_sub_3)) / 3

stu2_name=input("what is the name of 2nd student ? ")

stu2_regno=input("what is the reg no of 2nd student ? ")

stu2_sub_1=input("what are the marks of 1st subject ? ")

stu2_sub_2=input("what are the marks of 2nd subject ? ")

stu2_sub_3=input("what are the marks of 3rd subject ? ")

stu2_avgm= (float(stu2_sub_1)+float(stu2_sub_2)+float(stu2_sub_3)) / 3


stu3_name=input("what is the name of 3rd student ? ")

stu3_regno=input("what is the reg no of 3rd student ? ")

stu3_sub_1=input("what are the marks of 1st subject ? ")

stu3_sub_2=input("what are the marks of 2nd subject ? ")

stu3_sub_3=input("what are the marks of 3rd subject ? ")

stu3_avgm= (float(stu3_sub_1)+float(stu3_sub_2)+float(stu3_sub_3)) / 3

avgm=[ str(stu1_avgm)+ " is the average of " + stu1_name + " with reg no " + str(stu1_regno),
str(stu2_avgm)+ " is the average of " + stu2_name + " with reg no " + str(stu2_regno),
str(stu3_avgm)+ " is the average of " + stu3_name + " with reg no " + str(stu3_regno)]
        
avgm.sort()
print( 'list in assending order : ', avgm)











