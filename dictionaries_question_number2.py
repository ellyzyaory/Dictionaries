def accept_login(users, username, password):
    if username in users:
        if users[username] == password:
            return True
        else:
            return False
    else:
        return False

if __name__=="__main__":
    dictionary = {"Ellyz": "123456"}
    username_input = input("Username: ")
    password_input = input("Password: ")
    print(accept_login(dictionary, username_input, password_input))
