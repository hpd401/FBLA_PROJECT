# this is an algorithem that track actions and assigns a personality nicknamed P.AL for personality algorithem 
import time

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

def pet_response(action, pet_name="Pet"):
    personality = assign_personality()
    if personality == "Nurturing":
        if action == "feed":
            return " {name} eagerly accepts the food, showing deep appreciation for your nurturing care.".format(name=pet_name)
        elif action == "play":
            return " {name} plays gently, valuing the bond you're building.".format(name=pet_name)
        elif action == "clean":
            return " {name} stays still, trusting your careful cleaning.".format(name=pet_name)
        elif action == "rest":
            return "{name} rests peacefully, feeling secure in your presence.".format(name=pet_name)
        else:
            return "{name} appreciates your nurturing attention.".format(name=pet_name)
    elif personality == "Playful":
        if action == "feed":
            return " {name} bounces with excitement, loving the treat and asking for more playtime!".format(name=pet_name)
        elif action == "play":
            return "{name} moves energetically, loving the fun and games you share together!".format(name=pet_name)
        elif action == "clean":
            return "{name} squirms playfully, making cleaning a fun and silly experience!".format(name=pet_name)
        elif action == "rest":
            return "{name} reluctantly rests, but dreams of the next playful adventure!".format(name=pet_name)
        else:
            return "{name} is always ready for fun and games with you!".format(name=pet_name)
    elif personality == "Responsible":
        if action == "feed":
            return "{name} eats calmly, appreciating the care you take in providing for them.".format(name=pet_name)
        elif action == "play":
            return "{name} engages in play thoughtfully, enjoying the quality time together.".format(name=pet_name)
        elif action == "clean":
            return "{name} stays still and cooperative, understanding the importance of cleanliness.".format(name=pet_name)
        elif action == "rest":
            return "{name} rests quietly, valuing the routine and structure you provide.".format(name=pet_name)
        else:
            return "{name} appreciates your responsible care and attention.".format(name=pet_name)
    elif personality == "Relaxed":
        if action == "feed":
            return "{name} eats slowly, savoring the food and enjoying the moment.".format(name=pet_name)
        elif action == "play":
            return "{name} plays in a laid-back manner, enjoying the activity without any rush.".format(name=pet_name)
        elif action == "clean":
            return "{name} tolerates cleaning with a calm demeanor, not minding the process.".format(name=pet_name)
        elif action == "rest":
            return "{name} rests deeply, feeling completely at ease in your care.".format(name=pet_name)
        else:
            return "{name} enjoys a relaxed and easygoing relationship with you.".format(name=pet_name)
    elif personality == "Caring":
        if action == "feed":
            return "{name} eats with gratitude, showing a strong bond and appreciation for your care.".format(name=pet_name)
        elif action == "play":
            return "{name} plays with affection, cherishing the time spent together.".format(name=pet_name)
        elif action == "clean":
            return "{name} stays still and cooperative, trusting your care and attention.".format(name=pet_name)
        elif action == "rest":
            return "{name} rests peacefully, feeling loved and secure in your presence.".format(name=pet_name)
        else:
            return "{name} deeply values the caring relationship you share.".format(name=pet_name)
    elif personality == "Energetic":
        if action == "feed":
            return "{name} eats quickly, fueled by the energy and excitement you provide!".format(name=pet_name)
        elif action == "play":
            return "{name} plays with boundless energy, loving every moment of fun and activity!".format(name=pet_name)
        elif action == "clean":
            return "{name} fidgets during cleaning, eager to get back to playing and having fun!".format(name=pet_name)
        elif action == "rest":
            return "{name} struggles to rest, always buzzing with energy and ready for the next adventure!".format(name=pet_name)
        else:
            return "{name} is full of energy and always ready for fun with you!".format(name=pet_name)
    elif personality == "Balanced":
        if action == "feed":
            return "{name} eats with contentment, enjoying the balance of care and attention you provide.".format(name=pet_name)
        elif action == "play":
            return "{name} plays with enthusiasm, appreciating the fun and connection you share.".format(name=pet_name)
        elif action == "clean":
            return "{name} cooperates during cleaning, understanding the importance of care and hygiene.".format(name=pet_name)
        elif action == "rest":
            return "{name} rests comfortably, feeling secure and well-cared for in your presence.".format(name=pet_name)
        else:
            return "{name} enjoys a balanced and harmonious relationship with you.".format(name=pet_name)
    else:
        return "{name} responds in a unique way, reflecting its individual personality and the care you provide.".format(name=pet_name)

# Action tracking for personality assignment
action_counts = {"feed": 0, "play": 0, "clean": 0, "rest": 0}

def record_action(action):
  
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
