def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
        
    

readFile("1.py")
readFile("2.py")
readFile("3.py") 
readFile("4.py")
readFile("3.py") 