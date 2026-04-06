'''
Secure Login System (Decorators)
A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function.
'''
def SecureloginSys(func):
    def login_details():
       id='Harsha'
       ps='H@123'
       while True:
          a=input("Enter Your Id:")
          b=input("Enter Password:")
          if a==id and b==ps:
             print("Authentication Successful")
             func()
             break
          else:
             print("Authentication Failed")
             break
    return login_details           

@SecureloginSys
def info():
     print("You Can Access " \
            "--> Sensitive Information")
info()           