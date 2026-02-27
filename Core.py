pip install questionary
pip install tkinter
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

def show_stats():
    print(f"\n{pet_name}'s Current Stats:")
    print(f"Hunger: {Hunger}") 
    print(f"Health: {Health}")
    print(f"Happiness: {Happiness}") 

def feed_pet():  # this is the 1st action you can do
    global Hunger, Happiness, Energy
    Hunger += 10
    Happiness += 10
    Energy +=5


def play_with_pet():  # this is the second one we can do
    global Happiness, Health, Energy

    Happiness += 10
    Energy -= 10
    Health += 10

    print(f"\nYou played with {pet_name}! They seem more exited than usual.")
def rest():
    global Energy, Health
    Energy += 25
    Health += 10
    print(f"\n{pet_name} slept soundly. They look full of energy"

def main():
    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                f"Feed {pet_name}",
                f"Play with {pet_name}",
                "Show stats",
                "Play a minigame",
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
            print("Minigame selection coming soon!")
        elif choice == "Quit":
            print(f"Thanks for playing with {pet_name}! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":


    main()