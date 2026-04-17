'''
Smart Data Processing Pipeline 
Scenario: 
A system processes numeric data from file. 
Task: 
● Read numbers from a file 
● Use NumPy for calculations (mean, std) 
● Convert results to Pandas DataFrame 
● Use exception handling for bad data 
● Use a generator to stream data 
● Apply decorator to measure execution time
'''
import numpy as np
import pandas as pd
import time

#decorator function
def timer(func):
    def wrapper(*a,**b):
        start=time.time()
        result=func(*a,**b)
        end=time.time()
        print(f"\nExecution Time:{end-start:.4f} seconds")
        return result
    return wrapper

#Generator to read data from the file
def read_num(NumData):
    try:
       with open(NumData,"r") as file:
          for num in file:
            try:
               yield float(num.strip())
            except ValueError:
                print("Unsupported Format! Skipping the data:",num.strip())         
    except FileNotFoundError:
        print("File Not found!") 

#Main function
@timer
def data_processing(NumData):
    numbers=[]
    for num in read_num(NumData):
        numbers.append(num)
        
    if not numbers:
        print("No data found!")
    
    arr=np.array(numbers)
    mean_arr=np.mean(arr)
    std_arr=np.std(arr)
    
    print("Array:",arr)
    
    #df=pd.DataFrame({"Metrics":["Mean","Standard Deviation"],"Value":[mean_arr,std_arr]})
    df=pd.DataFrame([mean_arr,std_arr],index=["Mean","Standard Deviation"],columns=["Value"])
    print("Results:")
    print(df)

data_processing("Numeric_data.txt")