def say_hello():
    your_name = input("Do you have a name? ")
    print("Hello, ", your_name, "!", sep="" )

def insert_separator():
    print("++++++++++++")

def Hokey_Pokey():
    print("Wanna do the Hokey Pokey? ")
    insert_separator()
    print("You put your right hand in.")
    print("You put your right hand out.")
    print("You put your right hand in.")
    print("And you shake it all about.")
    print("You do the Hokey Pokey and you turn yourself around.")
    print("That's what it's all about.")

def farewell():
    print("Wasn't that fun?")
    print("Goodbye now!")

def main():
    say_hello()
    insert_separator()
    Hokey_Pokey()
    insert_separator()
    farewell()


main()