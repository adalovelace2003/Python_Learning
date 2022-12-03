letter= ''' Dear < | NAME |>,
Greetings from ABC companyy, I am happy to tell about your selection
You are selected!
Have a great day Ahead
Date : <| DATE |> 
'''
name= input("Enter your name! : ")
date = input("Enter date : ")
letter = letter.replace("NAME", name)
letter = letter.replace("DATE", date)

print(letter)