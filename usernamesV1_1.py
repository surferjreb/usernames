import userTools

quit = True

while quit:

    name = input("Welcome, Please enter your name: ").strip().lower()
    
    

    userTools.print_usernames()
    quit = userTools.check_continue(name)
