# Basic Email Validator
''' 
Conditions to validate email:
1. It can contain . _ on any count. 
( it's not necessary to have .com at last to be a valid mail. So we are not checking for .com at last.)
( Example: test@test.au test@test.technology || Both of these are valid mail.)
2. It should only contain one @ 
'''
def wrong():
    print("\n\tInvalid E-mail Address.")
    exit(0)

def validate(email):
    # Verifying if email address have only one @ and at least one dot.
    at = 0
    dot = 0
    for i in email:
        if i == "@":
            at += 1
        elif i == ".":
            dot += 1
    if at != 1 or dot == 0:
        wrong()

    for i in email:
        if i.isalnum() or i == "." or i == "_" or i == "@":
            pass
        elif  i == " ":
            wrong()
        else:
            wrong()
    print("\n\tValid E-mail Address.")


if __name__ == "__main__":
    email = input("Enter E-mail : ")
    validate(email)


