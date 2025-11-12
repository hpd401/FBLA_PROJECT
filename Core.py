print("Welcome to Pet Pals!")  # Opening title card and intro code. This reminds me of pokemon also google and my book came in clutch for showing me similar things.

def choose_option():
    print("\nPlease choose your pet:")
    print("1. Dog") # charmander
    print("2. Cat") # sqirtle
    print("3. Bird") # bulbasaur
    print("4. Robot") # pikachu

    choice = input("Enter your choice (1, 2, 3, or 4): ")  

    if choice == '1':
        print("You have chosen a Dog as your pet!")
    elif choice == '2':
        print("You have chosen a Cat as your pet!")
    elif choice == '3':
        print("You have chosen a Bird as your pet!")
    elif choice == '4':
        print("You have chosen a Robot as your pet!")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")


choose_option()

Hunger = 75
Health = 75
Happiness = 75
