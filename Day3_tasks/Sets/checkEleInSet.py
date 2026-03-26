# Write a program to check if an element exists in a set

'''
num=input("Enter elements seperated by space to form a set:")
s=set(map(int,num.split()))
'''
s=set(map(int,input("Enter elements:").split()))
#print("Set:",s)

check=int(input("Enter to check whether it exits in the set:"))

if check in s:
    print(f"{check} exists in the set")
else :
    print(f"{check} does not exits in the set")