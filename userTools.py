#Used to seperate my functions into modules and clean up my code
import usernames

def check_continue(value):
    if value == "quit":
        print("Have a nice day!")
        return False
    else:
        check_name(value)
        return True

def check_name(name):
    if name in usernames.usernames:
        duplicate(name)
    else:
        user_name = input("Enter your user name: ").strip().lower()
        check_username(name, user_name)
        

def check_username(name, user_name):
    
    for key,val in usernames.usernames.items():
        if user_name in val:
            user_name = input("User name already exists, Please enter a different one: ")
            add_user(name, user_name)
            break
    
    add_user(name, user_name)
        
def duplicate(name):
    duplicate_name = input("Name already exists is your username "+ usernames.usernames[name] + " y or n?: ").strip().lower()
    if duplicate_name == "y":
        print("Thanks for visiting, your login already exisits.")
    else:
        name = input("Enter your name plus last initial: ").strip().lower()
        check_name(name)

    
def add_user(name, user_name):
    
    usernames.usernames[name] = user_name
    print("You have been added.")
    

def print_usernames():
    print(usernames.usernames)
