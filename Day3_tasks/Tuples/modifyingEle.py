# Write a program to convert a tuple to a list and modify the element.
tu=(2,4,5,8,10)
lt=list(tu)
lt[2]=6
t=tuple(lt)
print("Modified tuple:",t)