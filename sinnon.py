from getpass import getpass

def display_credentials():
    website = input("Enter the name of the website:")
    password = getpass("Enter master password: ")
    print(website)
    print(password)

if __name__ == "__main__":
    display_credentials()
