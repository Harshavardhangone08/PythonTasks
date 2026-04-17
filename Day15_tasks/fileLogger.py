'''
Basic File Logger 
Scenario: 
A system logs user actions. 
Task: 
● Take user input 
● Store logs in a file 
● Use loop to allow multiple entries 
● Handle file errors using exception handling
'''

while True:
    try:
        log=input("Enter log(type exit to stop):")
        
        if log.strip()=="":
            raise ValueError
        
        if log.lower()=='exit':
            print("Logging stopped")
            break
        with open("log.txt",'a') as log_file:
            log_file.write(log+"\n")
            
        print("Log saved!")
    
    except ValueError:
        print("Empty log not allowed")
        
    except FileNotFoundError:
        print("Error! File not found")
    
        