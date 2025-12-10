print("Welcome to snugbit!")  # Opening title card and intro code so we get that pokemon style intro 

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
      
        continue 

    pet_name = input(f"What would you like to name your {pet_type}? ")
    print(f"\nAwesome! You chose a {pet_type} named {pet_name}!")
    return pet_type, pet_name


pet_type, pet_name = choose_option()

# Stats setup & cap 
stats = get_pet_stats(pet_type)

Hunger = stats["Hunger"]
Health = stats["Health"]
Happiness = stats["Happiness"]
Energy = stats["Energy"]

Hunger_Max = 100
Health_Max = 100
Happiness_Max = 100
Energy_Max = 100 # I spent four hours coding this, the minigames and the Ageing system then exited and forgot to save so it was all lost ... bruh

if Happiness > Happiness_Max:
    Happiness = Happiness_Max

if Health > Health_Max:
    Health = Health_Max

if Energy > Energy_Max:
    Energy = Energy_Max
    
if Hunger > Hunger_Max:
    Hunger = Hunger_Max

def show_stats():
    print(f"\n{pet_name}'s Current Stats:")
    print(f"Hunger: {Hunger}") # jeremy has died of hunger
    print(f"Health: {Health}") # mary sue has died of dysentary
    print(f"Happiness: {Happiness}") # josh has volentarily consumed a 3x3 inch cube of sodium and died

def feed_pet():  # this is the 1st action you can do
    global Hunger, Happiness
    if Dollars < 5:
        print("sorry,you don't have enough dollars")
        return
    Hunger += 10
    Happiness += 10
    Energy +=5
    Dollars -= 5
    print(f"\nYou fed {pet_name}! They look happier already.")

def play_with_pet():  # this is the second one we can do
    global Happiness, Health
    if Dollars < 5:
        print ("Sorry, you dont have enough dollars")
        return
    Happiness += 10
    Energy -= 10
    Health += 10
    Dollars -= 5
    print(f"\nYou played with {pet_name}! They seem more exited than usual.")
def rest():
    global Energy, Health
    Energy += 25
    Health += 10
    print(f"\n{pet_name} slept soundly. They look full of energy")

def main():  #dev log3: i accdentaly deleted the 1st devlog but thats ok. this code should fix the problem of the function happening without input so thanks book and google
    while True:
        print("\nwhat would you like to do?")
        print(f"\n1.feed {pet_name}")
        print(f"\n2.play with {pet_name} ")
        print("3.show stats")
        print("4. Play a minigame")
        print("5.Quit")

        imp = input("Choose a number:") # if chedder = cheese elif nachos elif tacos else nacho, taco

        if imp == "1":
            feed_pet()
        
        elif imp == "2":
            play_with_pet()
        
        elif imp == "3":
            show_stats()
        
        elif imp == "4":
            print("choose a minigame!")
            print("1.Feeding Frenzy")
            print("2.Trick Time")
            print("3.Medical Mayhem")
            print("4.Return")
            fun_choice = input("choose_a_minigame: ")

            if fun_choice == "1":
                minigame_hunger()

            elif fun_choice == "2":
                minigame_happiness()

            elif fun_choice == "3":
                minigame_health()
            
            elif fun_choice == "4":
                pass
            
            else:
                print("invalid choice")
                continue

        
        elif imp == "5":
            print("goodbye")
            break
        
        else:
            print("invalid choice,choose again")
            continue
main()