# Write a program to count the frequency of each character in a string

s=input("Enter a string:")
s=s.replace(" ","")

freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for k,val in freq.items():
    print(f"freqency of {k}:{val}")