print("\n\n\n\n\n\n")
# Function Arguments
''' 
Default Arguments
Keyword Arguments
Required Arguments
Variable-length Arguments
'''

# Default Arguments
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# Keyword Arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# Required Arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

# name("Peter", "Quill")    ''' This will give error '''

print("\n\n\n\n\n\n")


