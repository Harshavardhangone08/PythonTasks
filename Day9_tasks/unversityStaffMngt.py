'''
University Staff Management (Hierarchical Inheritance)
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information
'''
class Staff:
    def staff_details(self):
        print("Staff of ABC University!")
    def staff_prof(self):
        print("Professor of ABC University")
    def staff_labAsst(self):
        print("Lab Assistant of ABC University")
    def staff_admin(self):
        print("Administrator of ABC University") 
        
class Professor(Staff):
    def prof_details(self):
        print("A Professor should have the qualification of PhD"+"\n")
        
class LabAssistant(Staff):
    def labAsst_details(self):
        print("A lab Assistant should have good knowledge on the computer devices and Connectivity"+"\n")
    
class Administrator(Staff):
    def admin_details(self):
        print("An Administrator should have Strong Management skills and Strong leadership skills"+"\n")
    
P=Professor()
L=LabAssistant()
A=Administrator()

P.staff_prof()
P.prof_details()

L.staff_labAsst()
L.labAsst_details()

A.staff_admin()
A.admin_details()