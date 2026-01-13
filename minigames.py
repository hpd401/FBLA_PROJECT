import time
import random 
def minigame_health():
    print("get ready to give {pet_name} medicine")
    print(" when the screen says 'NOW' press any button as fast as you can")
    time.sleep(random.randint(2,5))
    print("NOW")
    start_time = time.time()
    input()
    reaction_time = time.time() - start_time
    if reaction_time < 1:
        print("Great job! You gave the medicine on time.")
        +20 health, +20 dollars
    elif reaction_time < 2:
        print("Good effort! You gave the medicine a bit late.")
        +10 health, +10 dollars
    else:
        print("Oof, you were too slow! {pet_name} got the medicine a bit late.")
        -5 health, +5 dollars

def minigame_happiness():
    