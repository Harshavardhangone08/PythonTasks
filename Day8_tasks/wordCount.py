'''
. Word Counter Program
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results.
'''
art=open("article.txt","w")
print("Enter your article (type 'END' on a new line to finish):")

while True:
    line = input()
    if line == "END":
        break
    art.write(line + "\n")

art.close()

file = open("article.txt", "r")

lines = 0
words = 0
characters = 0

for line in file:
    lines += 1
    words += len(line.split())
    characters += len(line)

file.close()

print("\nArticle Analysis:")
print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)