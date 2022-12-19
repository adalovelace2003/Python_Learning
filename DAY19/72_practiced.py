with open(("DAY19/donkey.py")) as f:
    content=f.read()

content= content.replace("donkey","$%^@$^#")

with open("DAY19/donkey.py","w") as f:
    f.write(content)
