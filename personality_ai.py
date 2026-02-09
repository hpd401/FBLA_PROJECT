# this is an aging system for AI personalities
def stat_decay
():
    global Hunger, Health, Happiness, Energy

    # Decay rates
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