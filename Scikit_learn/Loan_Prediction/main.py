#=================================================================================
#        Project Title:Loan Prediction System (loan_Approval_Dataset.csv)
#        Analyze Loan Predication dataset using NumPy, Pandas, Matplotlib
#==================================================================================

#=============================================================================
#                 Import Required Libraries
#=============================================================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#reading a dataset
df=pd.read_csv(r"H:\Python_tasks\Scikit_learn\Loan_Prediction\loan_Approval_Dataset.csv")

#first five rows
print(df.head())
#print columns
print(df.columns)

print('-'*100)
print(df.shape)

print('-'*100)
print(df.describe())

print('-'*100)
print("Checking for null values")
print(df.isnull().sum())
df=df.dropna()
print("Null values after preprocessing")
print(df.isnull().sum())

print('-'*100)
print(df.Dependents.value_counts())
#To replace 3+ values to 4
df['Dependents']=df['Dependents'].replace('3+',4)
df['Dependents']=df['Dependents'].astype(int)
#df['Dependents']=pd.to_numeric(df['Dependents'])
print('-'*100)
print(df.Dependents.value_counts())

#=============================================================================
#               To Handle Categorical Data
#=============================================================================

df2=df.copy()  #Creating a deep copy of the original dataset

df2['Loan_Status']=df2['Loan_Status'].map({'Y':1, 'N':0})

df2['Married'] = df2['Married'].map({'Yes':1, 'No':0})
df2['Gender'] = df2['Gender'].map({'Male':1, 'Female':0})
df2['Self_Employed'] = df2['Self_Employed'].map({'Yes':1, 'No':0})
df2['Property_Area'] = df2['Property_Area'].map({'Rural':0, 'Semiurban':1, 'Urban':2})
df2['Education'] = df2['Education'].map({'Graduate':1, 'Not Graduate':0})
df2['Credit_History']=df2['Credit_History'].astype(int)

#splitting dataset into training data and testing data
X=df2.drop(["Loan_Status", "Loan_ID"], axis=1)
y=df2.Loan_Status

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42, stratify=y)

# -----------------------------
# Feature Scaling
# -----------------------------
sc=StandardScaler()
#Fit and transform on training data
X_train=sc.fit_transform(X_train)

#transform test data
X_test=sc.transform(X_test)

#============================================================
#               Logistic Regression
#============================================================

LR_Model=LogisticRegression(max_iter=2000)
print('-'*100)
print(LR_Model)
#training the model
LR_Model.fit(X_train,y_train)
#For prediction
y_pred=LR_Model.predict(X_test)

#To calculate accuracy
Acc=accuracy_score( y_test, y_pred)
print("Accuracy:",Acc)

#============================================================
#                Support Vector Machine
#============================================================
SVM_model=SVC(kernel='rbf', C=1, gamma='scale')
print('-'*100)
print(SVM_model)
#training the model
SVM_model.fit(X_train, y_train)
#For prediction
y_pred=SVM_model.predict(X_test)

#To calculate Accuracy
Acc=accuracy_score(y_test, y_pred)
print("Accuracy:",Acc)

# ============================================================
#               Random Forest Classifier
# ============================================================
RF_model=RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
print('-'*100)
print(RF_model)
#training the model
RF_model.fit(X_train, y_train)
#For prediction
y_pred=RF_model.predict(X_test)

#To calculate Accuracy
Acc=accuracy_score(y_test, y_pred)
print("Accuracy:",Acc)

# ============================================================
#                 Gradient Boosting
# ============================================================
from sklearn.ensemble import GradientBoostingClassifier

GB_model=GradientBoostingClassifier()
print('-'*100)
print(GB_model)
#train the model
GB_model.fit(X_train,y_train)
#For prediction
y_pred=GB_model.predict(X_test)
#To calculate accuracy 
Acc=accuracy_score(y_test,y_pred)

print("Accuracy:",Acc)
print('='*100)
