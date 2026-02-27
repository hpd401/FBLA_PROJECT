#Minigames for Snugbit 
import time
import random
from typing import Dict


def minigame_health(timeout: int = 3) -> Dict[str, int]:
    #Simple quick-time minigame for medicine.
    print("Get ready to give the medicine to your pet!")
    print("When you see 'NOW' press Enter as fast as you can.")
    time.sleep(random.uniform(1.0, 3.0))
    print("NOW")
    start = time.time()
    input()
    reaction_time = time.time() - start

    if reaction_time < 0.8:
        print("Great job! You gave the medicine on time.")
        return {'health': 20, 'dollars': 20}
    elif reaction_time < 1.6:
        print("Good effort! You gave the medicine a bit late.")
        return {'health': 10, 'dollars': 10}
    else:
        print("Too slow. The pet got the medicine late.")
        return {'health': -5, 'dollars': 5}


def minigame_happiness() -> Dict[str, int]:
    

    print("When you see 'NOW' press any button as fast as you can to perform a trick!")
    
    print("Trick Time! Get ready...")
    time.sleep(random.uniform(0.5, 2.0))
    print("NOW")
    start = time.time()
    input()
    reaction_time = time.time() - start

    if reaction_time < 0.8:
        print("Amazing trick! Happiness up a lot.")
        return {'happiness': 20}
    elif reaction_time < 1.6:
        print("Nice try! Happiness up a bit.")
        return {'happiness': 10}
    else:
        print("The trick was rough, but your pet liked the effort.")
        return {'happiness': 5}


def minigame_hunger(duration: int = 10) -> Dict[str, int]:

    print(f"Feeding Frenzy! Press Enter as many times as you can in {duration} seconds.")
    print("(Press Enter to start)")
    input()
    end_time = time.time() + duration
    presses = 0

    try:
        
        while time.time() < end_time:
            
            input_start = time.time()
           
            if time.time() >= end_time:
                break
            input()
            presses += 1
            
            if time.time() >= end_time:
                break
    except KeyboardInterrupt:
        print("Minigame interrupted.")

    score = presses
    print(f"You caught {score} treats!")

    
    hunger = min(10 + score * 6, 100)
    dollars = score * 2
    happiness = min(score * 3, 100)

    return {'hunger': hunger, 'dollars': dollars, 'happiness': happiness}