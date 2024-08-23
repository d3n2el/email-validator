import validators

def main():
    output= validators.email(input("What's your email address? "))
    if output == True:
        print("Valid")
    else:
        print("Invalid")

main()
