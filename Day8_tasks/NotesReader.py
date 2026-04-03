'''
Notes Reader Program
A student stores daily notes in a file called notes.txt. Write a program that opens the
file, reads all the contents, and displays them on the screen.
'''

Notes=input("Enter Notes to be added:")

N_file=open("notes.txt","a")
N_file.write(f"{Notes} \n")

print("Daily Notes")
N_file=open("notes.txt","r")
print(N_file.read())
N_file.close()