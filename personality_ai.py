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
    cap_stats()  
    

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

def pet_response():

    pass

# Action tracking for personality assignment
action_counts = {"feed": 0, "play": 0, "clean": 0, "rest": 0}

def record_action(action):
    """
    Records a user action to track behavior patterns.
    """
    if action in action_counts:
        action_counts[action] += 1

def assign_personality():

    total_actions = sum(action_counts.values())
    if total_actions == 0:
        return "Neutral"  # No actions yet
    
    # Calculate percentages
    feed_ratio = action_counts["feed"] / total_actions
    play_ratio = action_counts["play"] / total_actions
    clean_ratio = action_counts["clean"] / total_actions
    rest_ratio = action_counts["rest"] / total_actions
    
    # Personality logic based on dominant actions
    if feed_ratio > 0.4:
        return "Nurturing"  # User focuses on feeding
    elif play_ratio > 0.4:
        return "Playful"  # User focuses on playing
    elif clean_ratio > 0.4:
        return "Responsible"  # User focuses on cleaning
    elif rest_ratio > 0.4:
        return "Relaxed"  # User focuses on resting
    elif feed_ratio > play_ratio and feed_ratio > clean_ratio:
        return "Caring"
    elif play_ratio > feed_ratio and play_ratio > clean_ratio:
        return "Energetic"
    else:
        return "Balanced"
