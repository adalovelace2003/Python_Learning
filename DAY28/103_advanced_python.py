#  Exception Handling

while (True):
    a = input("Enter a number : ")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)

        if a > 6:
            print("You entered a number greater than 6 ")
    except Exception as e:
        print(f"Your input resulted an error \n{e}")


print("Thanks for playing this game")
