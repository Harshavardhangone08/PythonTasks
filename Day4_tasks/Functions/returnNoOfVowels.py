# Write a function that takes a string as input and returns the number of vowels.

def vowel_count(string):
    vowels="aeiouAEIOU"
    count=0
    for ch in string:
        if ch in vowels:
            count+=1
    return count

s=input("Enter a string:")
c=vowel_count(s)
print("Count of vowels in the given string:",c)