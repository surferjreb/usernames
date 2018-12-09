usernames = {"john":"iceman13","james":"surferjreb"}

quit = True

while quit:

    name = input("Welcome, Please enter your name: ")
    if name == "quit":
        quit = False
        print("Have a nice day!")
        break
    else:
        
        if name in usernames:
            duplicate_name = input("Name already exists is your username " + usernames[name] + " y or n?: ").strip().lower()
            if duplicate_name == "y":
                print("Thanks for visiting, your login already exisits.")
                break
            else:
                name = input("Enter your name plus last initial: ").strip().lower()
                user_name = input("Enter your user name: ").strip().lower()
                usernames[name] = user_name
                print("You have been added")

        else:
            user_name = input("What is your user name?: ")
        
            for key,val in usernames.items():
            
                if user_name in val:
                    user_name = input("User name already exists, Please enter a different one: ")
                    usernames[name] = user_name
                    print("You have been added")
                    break

    print(usernames)
