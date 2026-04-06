'''
Student Result Generator (Method Overloading Concept)
A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subjects.
'''
class Result:
    def calculate_result(self,s1,s2=0,s3=0):
        Marks=s1+s2+s3
        print("Student results:",Marks)
        
R=Result()
R.calculate_result(90,95)
R.calculate_result(95,86,90)
        
    