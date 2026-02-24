# this is an aging system for AI personalities
import time

def stat_decay():
    global Hunger, Health, Happiness, Energy
    # stat decay works by check time then applying a decay value to each stat every 10 seconds, simulating the passage of time and the need for care and attention from the player. This encourages regular interaction with the pet to maintain its well-being.
    Hunger_decay = 5
    Health_decay = 3
    Happiness_decay = 4  #social battery 
    Energy_decay = 2

    # Applies decay over time with each action
    Hunger -= Hunger_decay
    Health -= Health_decay
    Happiness -= Happiness_decay
    Energy -= Energy_decay

    # Ensures stats do not go below zero
    if Hunger < 0:
        Hunger = 0
    if Health < 0:
        Health = 0
    if Happiness < 0:
        Happiness = 0
    if Energy < 0:
        Energy = 0

def pet_stats(pet_type):
    if pet_type == "Dog":
        return {"Hunger": 100, "Health": 100, "Happiness": 100, "Energy": 100}
    elif pet_type == "Cat":
        return {"Hunger": 90, "Health": 120, "Happiness": 90, "Energy": 80}
    elif pet_type == "Bird":
        return {"Hunger": 80, "Health": 85, "Happiness": 110, "Energy": 95}
    elif pet_type == "Robot":
        return {"Hunger": 0, "Health": 100, "Happiness": 100, "Energy": 100}
    else:
        return {"Hunger": 100, "Health": 100, "Happiness": 100, "Energy": 100}