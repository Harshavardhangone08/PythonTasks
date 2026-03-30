'''
Develop a Python program to manage student marks for three subjects. Store the subject
names in a tuple, maintain unique student names in a set, and store each student's marks
in a list inside a dictionary where the key is the student name. Create user-defined
functions to add a student with marks, display all student records, and calculate the average
marks of a student. Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu. Also include
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
student name entered does not exist in the dictionary).
'''

def addStudent():
    try:
        Name=input("Enter student name:")
        if Name in students:
            print("Student already exists")
            return
        
        students.add(Name)
            
        M1=int(input(f"Enter marks for {sub[0]}:"))
        M2=int(input(f"Enter marks for {sub[1]}:"))
        M3=int(input(f"Enter marks for {sub[2]}:"))
          
        marks_li=[M1,M2,M3]
        Stu_di[Name]=marks_li
        
    except ValueError:
         print("Marks should be an integer value!")
    except TypeError:
        print("Invalid data type entered!")
    
def displayStudents():
    if not Stu_di:
        print("No Student data available!")
    else:
        print("Student Records:")
        for k,val in Stu_di.items():
            print(k,":",val)

#Recursive function
def marks_total(li):
    if len(li)==0:
        return 0
    else:
        return li[0]+marks_total(li[1:])
    
def calculateAvg():
    try:
        s=input("Enter student name to calculate average:")
        if s not in Stu_di:
            raise NameError  #("Student not found")
        
        li=Stu_di[s]
        total=marks_total(li)
        
        avg=total/len(li)
        print(f"Average marks of {s}={avg:.2f}")
        
    except NameError:
       print("Student Not found!")
    except TypeError:
        print("Invalid data type!")
    except ZeroDivisionError:
        print("Number cannot be divided by zero!")
  
Stu_di={}   
students=set()
sub=('Maths','Science','English')
#Menu
while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Calculate Average")
    print("4.Exit")
    try:
      choice=int(input("Enter choice(1-4):"))
    except ValueError:
        print("Enter integer value!")
        continue
        
    if choice==1:
        addStudent()
    elif choice==2:
        displayStudents()
    elif choice==3:
        calculateAvg()
    elif choice==4:
        print("Exit!")
        break
    else:
        print("Invalid choice!")
   
   