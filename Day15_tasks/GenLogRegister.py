'''
Generator-based Log Reader 
Scenario: 
A large log file needs to be processed. 
Task: 
● Create a generator to read file line by line 
● Use loop to process logs 
● Use condition to filter errors 
● Count occurrences using a dictionary 
'''

def logFile(file):
  try:
     with open(file,"r") as fi:
        for line in fi:
            yield line.strip()  #reads file line by line
            
  except FileNotFoundError:
      print("File Not Found!")
      
Textfile=logFile("log_file.txt")

error_Occurrence={}
for log in Textfile:
    if log and "ERROR" in log:
        
        error=log.split()[-1]  #extracts Error message
        if error in error_Occurrence:
            error_Occurrence[error]+=1
        else:
            error_Occurrence[error]=1
        
print("Error Counts:")
for error,count in error_Occurrence.items():
    print(f"{error}:{count}")