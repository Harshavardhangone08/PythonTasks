'''
Decorator-based Access Control 
Scenario: 
Restrict access to certain functions. 
Task: 
● Create a decorator to check user role 
● Use condition inside decorator 
● Apply decorator to multiple functions 
● Store roles in a dictionary 
'''
users={"Harsha":"admin","Anshu":"manager","Abhi":"user"}
print(users,"\n")

def required_role(role):
    def decorator(func):
        def wrapper(username,*a,**b):
            if username in users and users[username]==role:
                return func(username,*a,**b)
            else:
                print(f"Access denied for {username}! Required role:{role}")
        return wrapper
    return decorator


@required_role("admin")
def modify_data(username):
    print(f"{username} modified data")

@required_role("manager")
def access_reports(username):
    print(f"{username} can access reports")

@required_role("user")
def user_profile(username):
    print(f"{username} is viewing profile")
    
modify_data("Harsha")
modify_data("Abhi")
access_reports("Harsha")
access_reports("Anshu")
user_profile("Abhi")