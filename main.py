from database import Employees
from database import Privileges
from database import Actions

def login():
    while(True):
        print("Please login\n")
        username = input("Username: ")
        password = input("Password: ")

        if username in Employees and Employees[username].password == password:
            print("Login succeeded!\n")
            return Employees[username]
        
        print("Login failed\n")


def main():    
    employee = login() # ask user to login

    # logged in, user interaction
    while(True):
        print("Your position is {}.".format(employee.position))

        print("Your available actions:")
        for priv in Privileges[employee.position]:
            print("\t{} = {}".format(priv, Actions[priv][0]))

        choice = input("What do you wanna do?")


        if choice not in Privileges[employee.position]:
            # the user is NOT allowed to invoke this function
            print("Insufficient privileges")
        else:

            # logout
            if choice == 'q':
                print("Logged out.\n")
                main()
            else:
                # invoke the method saved into Actions
                Actions[choice][1]()

if __name__ == "__main__":
    main()