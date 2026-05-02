#============================================================================
#          Project Title:House Price Prediction (house_data.csv)
#          Analyze House prices dataset using NumPy, Pandas, Matplotlib
#=============================================================================

#=============================================================================
#                 Import Required Libraries
#=============================================================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_absolute_error,root_mean_squared_error

#reading a dataset
df=pd.read_csv("house_data.csv")
print(df.head())
print('-'*80)
print("Checking for null values")
print(df[["bedrooms","bathrooms","sqft_living","sqft_lot","floors",
      "condition","grade","sqft_basement","yr_built","yr_renovated","price"]].isnull().sum())

# Selecting features (X) and target (y)
X=df[["bedrooms","bathrooms","sqft_living","sqft_lot","floors",
      "condition","grade","sqft_basement","yr_built","yr_renovated"]].values

y=df["price"].values

#Shape of data
print(f"shape of X:{X.shape}\nShape of y:{y.shape}")

#splitting dataset into training data and testing data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

print('-'*80)
print(f"Length of X_train: {len(X_train)}\nLength of X_test: {len(X_test)}")
print(f"Length of y_train: {len(y_train)}\nLength of y_test: {len(y_test)}")

# -----------------------------
# Feature Scaling
# -----------------------------
sc=StandardScaler()
#Fit and transform on training data
X_train=sc.fit_transform(X_train)

#transform set data
X_test=sc.transform(X_test)

# function for model evaluation
def Model_eval(y_test,y_pred,Model):
    score=r2_score(y_test,y_pred)
    mae=mean_absolute_error(y_test,y_pred)
    rmse=root_mean_squared_error(y_test,y_pred)
    
    print(f"{Model} Score:")
    print(f"R2 Score: {score:.3f}")
    print(f"MAE: {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    
#============================================================
#               Linear Regression
#============================================================
from sklearn.linear_model import LinearRegression

LRmodel=LinearRegression()
print('-'*80)
print(LRmodel)
#training the model
LRmodel.fit(X_train,y_train)
y_pred=LRmodel.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Linear Regression")

#============================================================
#                Lasso Regression
#============================================================
from sklearn.linear_model import Lasso

lasso_model=Lasso()
print('-'*80)
print(lasso_model)
#training the model
lasso_model.fit(X_train,y_train)
y_pred=lasso_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Lasso Regression")

#============================================================
#                Ridge Regression
#============================================================
from sklearn.linear_model import Ridge
ridge_model=Ridge(alpha=1.0)
print('-'*80)
print(ridge_model)
#training the model
ridge_model.fit(X_train,y_train)
y_pred=ridge_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Ridge Regression")

#============================================================
#                Support Vector Machine
#============================================================
from sklearn.svm import SVR

svm_model=SVR()
print('-'*80)
print(svm_model)
#training the model
svm_model.fit(X_train,y_train)
y_pred=svm_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Support Vector Regression")

# ============================================================
#                Decision Tree
# ============================================================
from sklearn.tree import DecisionTreeRegressor

tree_model=DecisionTreeRegressor(random_state=42)
print('-'*80)
print(tree_model)
#training the model
tree_model.fit(X_train,y_train)
y_pred=tree_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Decision tree regressor")

# ============================================================
#               Random Forest Regressor
# ============================================================
from sklearn.ensemble import RandomForestRegressor

random_model=RandomForestRegressor()
print('-'*80)
print(random_model)
#training the model
random_model.fit(X_train,y_train)
y_pred=random_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Random Forest regressor")

# ============================================================
#               Gradient Boosting Regressor
# ============================================================
from sklearn.ensemble import GradientBoostingRegressor

grad_model=GradientBoostingRegressor()
print('-'*80)
print(grad_model)
#training the model
grad_model.fit(X_train,y_train)
y_pred=grad_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"Gradient Boosting Regressor")

# ============================================================
#               K-Nearest Neighbors Regressor
# ============================================================
from sklearn.neighbors import KNeighborsRegressor

KNN_model=KNeighborsRegressor()
print('-'*80)
print(KNN_model)
#training the model
KNN_model.fit(X_train,y_train)
y_pred=KNN_model.predict(X_test)
# To calculate algorithm score
Model_eval(y_test,y_pred,"K-Nearest Neighbors Regressor")

# ============================================================
#               Bagging Regressor
# ============================================================
from sklearn.ensemble import BaggingRegressor

bagging_model=BaggingRegressor()
print('-'*80)
print(bagging_model)
#training the model
bagging_model.fit(X_train,y_train)
y_pred=bagging_model.predict(X_test)
#To calculate algorithm score
Model_eval(y_test,y_pred,"Bagging Regressor")

# ============================================================
#               XGBoost Regressor
# ============================================================
from xgboost import XGBRegressor

XGB_model=XGBRegressor()
print('-'*80)
#print(XGB_model)
#training the model
XGB_model.fit(X_train,y_train)
y_pred=XGB_model.predict(X_test)
#To evaluate model 
Model_eval(y_test,y_pred,"XGBoost Regressor")

