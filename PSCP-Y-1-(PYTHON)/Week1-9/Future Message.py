"""Future Message"""
def main():
    """Future Message"""
    n = input()
    if n.isnumeric():
        print("Number")
    elif n.isupper():
        print("Uppercase")
    elif n.islower():
        print("Lowercase")
    elif n.istitle():
        print("Title")
    elif n.isspace():
        print("Space")
    else:
        print( "Other" )
main()
