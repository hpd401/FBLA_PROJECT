print("Welcome to snugbit!")  # Opening title card and intro code so we get that pokemon style intro 
import minigames
import questionary
import economy
from personality_ai import pet_stats
class Pet:
    def __init__(self, pet_type, pet_name):
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.stats = pet_stats(pet_type)
        self.hunger = self.stats["Hunger"]
        self.health = self.stats["Health"]
        self.happiness = self.stats["Happiness"]
        self.energy = self.stats["Energy"]
def choose_option():# this can let users choose their pet and name it, As instucted in the guidlines
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
        return choose_option()

    pet_name = input(f"What would you like to name your {pet_type}? ")
    print(f"\nAwesome! You chose a {pet_type} named {pet_name}!")
    return pet_type, pet_name


pet_type, pet_name = choose_option()

# Stats setup & cap 
stats = pet_stats(pet_type)

Hunger = stats["Hunger"]
Health = stats["Health"]
Happiness = stats["Happiness"]
Energy = stats["Energy"]

Hunger_Max = 100
Health_Max = 100
Happiness_Max = 100
Energy_Max = 100
Happiness_Max= 100

if Health > Health_Max:
    Health = Health_Max

if Energy > Energy_Max:
    Energy = Energy_Max
    
if Hunger > Hunger_Max:
    Hunger = Hunger_Max

if Happiness > Happiness_Max:
    Happiness = Happiness_Max

def show_stats():# This function displays the current stats of the pet to the user
    print(f"\n{pet_name}'s Current Stats:")
    print(f"Hunger: {Hunger}") 
    print(f"Health: {Health}")
    print(f"Happiness: {Happiness}") 

def cap_stats():  3# This function ensures that all stats stay within their defined limits (0 to Max)
    global Hunger, Health, Happiness, Energy
    Hunger = min(max(0, Hunger), Hunger_Max)
    Health = min(max(0, Health), Health_Max)
    Happiness = min(max(0, Happiness), Happiness_Max)
    Energy = min(max(0, Energy), Energy_Max)

def feed_pet():  # this is the 1st action you can do
    global Hunger, Happiness, Energy
    Hunger += 10
    Happiness += 10
    Energy +=5
    cap_stats()


def play_with_pet():  # this is the second one we can do
    global Happiness, Health, Energy

    Happiness += 10
    Energy -= 10
    Health += 10

    print(f"\nYou played with {pet_name}! They seem more exited than usual.")
    cap_stats()
def rest():
    global Energy, Health
    Energy += 25
    Health += 10
    print(f"\n{pet_name} slept soundly. They look full of energy")
    cap_stats()

def play_minigame():# This is the minigame function, it allows the user to choose a minigame and then updates the pet's stats based on the results of the minigame.
    global Hunger, Health, Happiness, Energy
    
    minigame_choice = questionary.select(
        "Which minigame would you like to play?",
        choices=[
            "Medicine Rush",
            "Trick Performance",
            "Feeding Frenzy",
            "Back to main menu"
        ]
    ).ask()
    
    if minigame_choice == "Medicine Rush":
        result = minigames.minigame_health()
        if 'health' in result:
            Health += result['health']
        print(f"Health increased by {result.get('health', 0)}!")
        print(f"You also earned ${result.get('dollars', 0)}!")
        cap_stats()
        
    elif minigame_choice == "Trick Performance":
        result = minigames.minigame_happiness()
        Happiness += result.get('happiness', 0)
        print(f"Happiness increased by {result.get('happiness', 0)}!")
        cap_stats()
        
    elif minigame_choice == "Feeding Frenzy":
        result = minigames.minigame_hunger()
        Hunger = max(0, Hunger - result.get('hunger', 0))
        Happiness += result.get('happiness', 0)
        print(f"Hunger decreased by {result.get('hunger', 0)}, Happiness increased!")
        print(f"You also earned ${result.get('dollars', 0)}!")
        cap_stats()
        
    elif minigame_choice == "Back to main menu":
        return
        
    elif minigame_choice == "Trick Performance (Happiness)":
        result = minigames.minigame_happiness()
        Happiness += result.get('happiness', 0)
        print(f"Happiness increased by {result.get('happiness', 0)}!")
        
    elif minigame_choice == "Feeding Frenzy (Hunger)":
        result = minigames.minigame_hunger()
        Hunger = max(0, Hunger - result.get('hunger', 0))
        Happiness += result.get('happiness', 0)
        print(f"Hunger decreased by {result.get('hunger', 0)}, Happiness increased!")
        print(f"You also earned ${result.get('dollars', 0)}!")
        
    elif minigame_choice == "Back to main menu":
        return

def main():
    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                f"Feed {pet_name}",
                f"Play with {pet_name}",
                "Show stats",
                "Play a minigame",
                "rest",
                "Quit"
            ]
        ).ask()
        
        if choice == f"Feed {pet_name}":
            feed_pet()
        elif choice == f"Play with {pet_name}":
            play_with_pet()
        elif choice == "Show stats":
            show_stats()
        elif choice == "Play a minigame":
            play_minigame()
        elif choice == "rest":
            rest()
        elif choice == "Quit":
            print(f"Thanks for playing with {pet_name}! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":


    main()