print("Welcome to Pet Pals!")  # Opening title card and intro code so we get that pokemon style intro 

def choose_option():
    print("\nPlease choose your pet:")
    print("1. Dog")   # charmander
    print("2. Cat")   # squirtle
    print("3. Bird")  # bulbasaur
    print("4. Robot") # pikachu

    choice = input("Enter your choice (1, 2, 3, or 4): ")
 
    if choice == '1':
        pet_type = "Dog"
    elif choice == '2':
        pet_type = "Cat"
    elif choice == '3':
        pet_type = "Bird"
    elif choice == '4':
        pet_type = "Robot"
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        return None, None
        continue 

    pet_name = input(f"What would you like to name your {pet_type}? ")
    print(f"\nAwesome! You chose a {pet_type} named {pet_name}!")
    return pet_type, pet_name



pet_type, pet_name = choose_option()

# Stats setup
Hunger = 75
Health = 75
Happiness = 75

def show_stats():
    print(f"\n{pet_name}'s Current Stats:")
    print(f"Hunger: {Hunger}") # jeremy has died of hunger
    print(f"Health: {Health}") # mary sue has died of dysentary
    print(f"Happiness: {Happiness}") # josh has volentarily consumed a 3x3 inch cube of sodium and died

def feed_pet():  # this is the 1st action you can do
    global Hunger, Happiness
    Hunger += 10
    if Hunger > 100:
        Hunger = 100
    Happiness += 10
    if Happiness > 100:
        Happiness = 100
    Dollars -= 5
    print(f"\nYou fed {pet_name}! They look happier already.")

def play_with_pet():  # this is the second one we can do
    global Happiness, Health
    Happiness += 10
    if Happiness > 100:
        Happiness = 100
    Health += 10
    if Health > 100:
        Health = 100
    Dollars -= 5
    print(f"\nYou played with {pet_name}! They seem full of energy now.")

def main():  
    while True:
        print("\nwhat would you like to do?")
        print(f"\n1.feed {pet_name}")
        print(f"\n2.play with {pet_name} ")
        print("3.show stats")
        print("4. Play a minigame")
        print("5.Quit")

        imp = input("Choose a number:")

        if imp == "1":
            feed_pet(pet_name)
        
        elif imp == "2":
            play_with_pet(pet_name)
        
        elif imp == "3":
            show_stats()
        
        elif imp == "4":
            print("choose a minigame!")
            print("1.Feeding Frenzy")
            print("2.Trick Time")
            print("3.Medical Mayhem")
            print("4.Return")

            if imp == "1":
                run minigame_hunger(pet_name)
            
            elif imp == "2":
                run minigame_happiness(pet_name)
            
            elif imp == "3":
                run minigame_health(pet_name)
            
            else imp == "4":
                return
        
        elif imp == "5":
            print("goodbye")
            break
        
        else:
            print("invalid choice,choose again")
            continue