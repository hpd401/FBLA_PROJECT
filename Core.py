import os
import warnings

# Only use the dummy SDL driver when no display is available.
# This allows the visual title screen to appear on a normal desktop.
if "DISPLAY" not in os.environ and os.name != "nt":
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

warnings.filterwarnings("ignore", message=".*pkg_resources.*")
import UI
import minigames
import questionary
import economy
from personality_ai import pet_stats, pet_response, record_action
import time
import threading
import sys

class Pet:
    def __init__(self, pet_type, pet_name):
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.stats = pet_stats(pet_type)
        self.hunger = self.stats["Hunger"]
        self.health = self.stats["Health"]
        self.happiness = self.stats["Happiness"]
        self.energy = self.stats["Energy"]

title = UI.TitleScreen()
result = title.run()
if result == "start_game":
    pet_type = UI.PetSelection().run()
    if pet_type == "back":
        # Go back to title, but for simplicity, exit
        print("Going back to title.")
        sys.exit()
    else:
        pet_name = input(f"What would you like to name your {pet_type}? ")
        print(f"\nAwesome! You chose a {pet_type} named {pet_name}!")

        # Stats setup & cap as well as minimum 
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

        # Now create the pet
        my_pet = Pet(pet_type, pet_name)
        # ... continue with game loop or whatever
elif result == "quit":
    sys.exit()

if Happiness < 0:
    Happiness = 0

if Health < 0: 
    Health = 0
if Energy < 0:
    Energy = 0
if Hunger < 0:
    Hunger = 0

def show_stats():
    # display current stats along with wallet info and interest rate
    print(f"\n--- {pet_name}'s Current Stats ---")
    print(f"Balance: ${economy.get_balance()} (Interest: {economy.interest_rate*100:.1f}%)")
    print(f"Hunger: {Hunger}") 
    print(f"Health: {Health}")
    print(f"Happiness: {Happiness}") 

def cap_stats():  # This function ensures that all stats stay within their defined limits (0 to Max)
    global Hunger, Health, Happiness, Energy
    Hunger = min(max(0, Hunger), Hunger_Max)
    Health = min(max(0, Health), Health_Max)
    Happiness = min(max(0, Happiness), Happiness_Max)
    Energy = min(max(0, Energy), Energy_Max)

def stat_decay():
    global Hunger, Health, Happiness, Energy
    # stat decay works by applying a decay value to each stat every 5 minutes, simulating the passage of time and the need for care and attention from the player. This encourages regular interaction with the pet to maintain its well-being.
    Hunger_decay = 5
    Health_decay = 3
    Happiness_decay = 4  #social battery 
    Energy_decay = 2

    # Applies decay over time
    Hunger -= Hunger_decay
    Health -= Health_decay
    Happiness -= Happiness_decay
    Energy -= Energy_decay
    cap_stats()
    print(f"\n⏰ Time passes... {pet_name}'s stats have decayed slightly.")

def run_decay():
    while True:
        time.sleep(300)  # 5 minutes
        stat_decay()

def feed_pet():  # this is the 1st action you can do
    global Hunger, Happiness, Energy
    Shop_buff()
    Hunger += 10
    Happiness += 10
    Energy +=5
    record_action("feed")
    print(f"\nYou fed {pet_name}! {pet_response('feed')}")
    cap_stats()


def play_with_pet():  # this is the second one we can do
    global Happiness, Health, Energy
    Shop_buff()
    Happiness += 10
    Energy -= 10
    Health += 10
    record_action("play")
    print(f"\nYou played with {pet_name}! {pet_response('play')}")
    cap_stats()

def rest():
    global Energy, Health
    Energy += 25
    Health += 10
    record_action("rest")
    print(f"\n{pet_name} slept soundly. {pet_response('rest')}")
    cap_stats()

def Clean():
    global Health, Happiness
    Shop_buff()
    Health += 15
    Happiness -= 5
    record_action("clean")
    print(f"\nYou cleaned {pet_name}. {pet_response('clean')}")
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
        earned = result.get('dollars', 0)
        if earned:
            economy.add_dollars(earned, description="Medicine Rush reward")
        print(f"Health increased by {result.get('health', 0)}!")
        print(f"You also earned ${earned}!")
        cap_stats()
        
    elif minigame_choice == "Trick Performance":
        result = minigames.minigame_happiness()
        Happiness += result.get('happiness', 0)
        cap_stats()
        
    elif minigame_choice == "Feeding Frenzy":
        result = minigames.minigame_hunger()
        Hunger = max(0, Hunger - result.get('hunger', 0))
        Happiness += result.get('happiness', 0)
        earned = result.get('dollars', 0)
        if earned:
            economy.add_dollars(earned, description="Feeding Frenzy reward")
        print(f"Hunger decreased by {result.get('hunger', 0)}, Happiness increased!")
        print(f"You also earned ${earned}!")
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
    # Start the decay thread
    decay_thread = threading.Thread(target=run_decay)
    decay_thread.daemon = True
    decay_thread.start()
    
    while True:
        # automatically apply configured interest each turn
        gained = economy.apply_interest()  # uses economy.interest_rate
        if gained:
            print(f"\nPassive interest: +${gained} (new balance ${economy.get_balance()})")

        # header showing balance and rate (like top-right corner)
        print(f"\n[Balance: ${economy.get_balance()} | Interest rate: {economy.interest_rate*100:.1f}%]")

        choice = questionary.select(
            "What would you like to do?",
            choices=[
                f"Feed {pet_name}",
                f"Play with {pet_name}",
                f"Rest",
                "Show stats",
                "Show wallet",
                "Collect income",
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
        elif choice == "Show wallet":
            economy.print_economy_summary()
        elif choice == "Collect income":
            # a simple fixed paycheck, could be tied to time or events later
            amount = economy.give_income(50, description="fixed paycheck")
            print(f"\nYou received a paycheck of ${amount}!")
        elif choice == "Play a minigame":
            play_minigame()
        elif choice == "Rest":
            rest()
        elif choice == "Clean":
            Clean()
        elif choice == "Quit":
            print(f"Thanks for playing with {pet_name}! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":


    main()