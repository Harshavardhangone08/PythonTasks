#importing libraries
from random import randint
from sklearn.linear_model import LinearRegression

# Create a range limit for random numbers in the training set, and a count of the 
#number of rows in the training set 
TRAIN_SET_COUNT=1000
TRAIN_SET_LIMIT=100

#Create an empty list of the input training set 'X' and create an empty list of the 
#output for each training set 'y' 
TRAIN_INPUT=list()
TRAIN_OUTPUT=list()

#Create and append a randomly generated data set to the input and output 
for i in range(TRAIN_SET_LIMIT):
    a=randint(0,TRAIN_SET_COUNT)
    b=randint(0,TRAIN_SET_COUNT)
    c=randint(0,TRAIN_SET_COUNT)
    d=randint(0,TRAIN_SET_COUNT)
    #Create a linear function for the output dataset 'y'
    Result= 7*a + 3*b + 4*c + 9*d
    TRAIN_INPUT.append([a,b,c,d])
    TRAIN_OUTPUT.append(Result)

#Create a linear regression object  
#n_jobs = the number of jobs to use for computation, -1 means use all processors 
model=LinearRegression(n_jobs=-1)
#training the model
model.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)  #(approximate a target function)

#X_TEST=[list(map(int,input("Enter 4 values seperated by space:").split()))]  #taking input from user
X_TEST=[[2,6,4,8]]  #Create our testing data set, the ouput should be 
#7*2 + 3*6 + 4*4 + 9*8= 120

Output=model.predict(X=X_TEST)  # Predict the ouput of the test data using the linear model

coefficients=model.coef_   ##The estimated coefficients for the linear regression problem.

print(f"Result:{Output}\nCoefficients:{coefficients}")           


