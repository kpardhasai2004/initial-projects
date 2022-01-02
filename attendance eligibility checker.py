name=input("enter name of the student: ")
reg=input("enter reg number: ")
sub1_attendance=input("attendance of sub1: ")
sub2_attendance=input("attendance of sub2: ")
sub3_attendance=input("attendance of sub3: ")
sub4_attendance=input("attendance of sub4: ")
sub5_attendance=input("attendance of sub5: ")
minimum_attendance=60

if float(sub1_attendance)>float(minimum_attendance) and float(sub2_attendance)>float(minimum_attendance) and float(sub3_attendance)>float(minimum_attendance) and float(sub4_attendance)>float(minimum_attendance) and float(sub5_attendance)>float(minimum_attendance):
    print("studet name : "+ name)
    print("student Reg_no : " + reg)
    print("status: eligible to attend exam")  


else :
    print("studet name : "+ name)
    print("student Reg_no : " + reg)
    print("status: not eligible to attend exam")
