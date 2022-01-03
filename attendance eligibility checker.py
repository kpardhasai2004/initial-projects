name=input("enter name of the student: ")
reg=input("enter reg number: ")

sub1_name=input("Name of sub1: ")

sub2_name=input("Name of sub2: ")

sub3_name=input("Name of sub3: ")

sub4_name=input("Name of sub4: ")

sub5_name=input("Name of sub5: ")

sub1_attendance=input("attendance of " + sub1_name + " : ")

sub2_attendance=input("attendance of " + sub2_name + " : ")

sub3_attendance=input("attendance of " + sub3_name + " : ")

sub4_attendance=input("attendance of " + sub4_name + " : ")

sub5_attendance=input("attendance of " + sub5_name + " : ")

minimum_attendance=60

if float(sub1_attendance)>float(minimum_attendance) and float(sub2_attendance)>float(minimum_attendance) and float(sub3_attendance)>float(minimum_attendance) and float(sub4_attendance)>float(minimum_attendance) and float(sub5_attendance)>float(minimum_attendance):
    print("studet name : "+ name)
    print("student Reg_no : " + reg)
    print("status: eligible to attend exam ")  


else :
    print("studet name : "+ name)
    print("student Reg_no : " + reg)
    print("status: not eligible to attend exam")
