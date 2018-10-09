import database

def login():
    while(True):
        print("Please login\n")
        username = input("Username: ")
        password = input("Password: ")

        if username in database.Employees and database.Employees[username].password == password:
            print("Login succeeded!\n")
            return database.Employees[username]
        
        print("Login failed\n")


def main():    
    employee = login() # ask user to login

    # logged in, user interaction
    while(True):
        print("Your position is {}.".format(employee.position))

        print("Your available actions:")
        for priv in database.Privileges[employee.position]:
            print("\t{} = {}".format(priv, database.Actions[priv][0]))

        choice = input("\nWhat do you wanna do?")

        if choice not in database.Actions.keys():
            print("No such operation")
        elif choice not in database.Privileges[employee.position]:
            # the user is NOT allowed to invoke this function
            print("Insufficient privileges")
        else:

            # logout
            if choice == 'q':
                print("Logged out.\n")
                main()
            else:
                # invoke the method saved into Actions
                database.Actions[choice][1]()

if __name__ == "__main__":
    database.init() # initialize database
    main()