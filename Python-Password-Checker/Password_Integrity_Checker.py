def check_password(password):
    password_list = str(password)

    has_capital = False
    has_special = False
    has_number = False
    has_length = True

    #Checks that password length is at least 8
    if len(password_list) >= 8:
        has_length = True
    
    special_chars = set("!@#$%^&*()<>?:{}[]")

    #checks if the characters in the given password fit the requirements
    for char in password_list:
        if char.isupper():
            has_capital = True
        if char.isdigit():
            has_number = True
        if char in special_chars:
            has_special = True
    
    is_valid = has_capital and has_length and has_special and has_number

    #Prints the error or success message
    if is_valid:
        return True, ("Password is valid!")
    elif not has_length:
        return False, ("Password is too short.")
    elif not has_capital:
        return False, ("Password needs a capital letter.")
    elif not has_special:
        return False, ("Password needs a special character.")
    elif not has_number:
        return False, ("Password needs a number.")

while True:   #Sets an infinite loop
    password = input("Enter a password: ")
    is_valid, errors = check_password(password) #Sets the two values from check_password, boolean and errors, to is_valid and errors
    
    #if password is valid, infinite loop breaks
    if is_valid:
        print("Password is valid!")
        break
    #otherwise, it repeats
    else:
        print("Password is invalid!")
        print(errors)
