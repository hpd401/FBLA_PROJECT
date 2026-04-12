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

def pet_response(action):
    personality = assign_personality()
    if personality == "Nurturing":
        if action == "feed":
            return " {pet_name} eagerly accepts the food, showing deep appreciation for your nurturing care."
        elif action == "play":
            return " {pet_name} plays gently, valuing the bond you're building."
        elif action == "clean":
            return " {pet_name} stays still, trusting your careful cleaning."
        elif action == "rest":
            return "{pet_name} rests peacefully, feeling secure in your presence."
        else:
            return "{pet_name} appreciates your nurturing attention."
    elif personality == "Playful":
        if action == "feed":
            return " {pet_name} bounces with excitement, loving the treat and asking for more playtime!"
        elif action == "play":
            return "{pet_name} moves energetically, loving the fun and games you share together!"
        elif action == "clean":
            return "{pet_name} squirms playfully, making cleaning a fun and silly experience!"
        elif action == "rest":
            return "{pet_name} reluctantly rests, but dream of the next playful adventure!"
        else:
            return "{pet_name} is always ready for fun and games with you!"
    elif personality == "Responsible":
        if action == "feed":
            return "{pet_name} eats calmly, appreciating the care you take in providing for them."
        elif action == "play":
            return "{pet_name} engages in play thoughtfully, enjoying the quality time together."
        elif action == "clean":
            return "{pet_name} stays still and cooperative, understanding the importance of cleanliness."
        elif action == "rest":
            return "{pet_name} rests quietly, valuing the routine and structure you provide."
        else:
            return "{pet_name} appreciates your responsible care and attention."
    elif personality == "Relaxed":
        if action == "feed":
            return "{pet_name} eats slowly, savoring the food and enjoying the moment."
        elif action == "play":
            return "{pet_name} plays in a laid-back manner, enjoying the activity without any rush."
        elif action == "clean":
            return "{pet_name} tolerates cleaning with a calm demeanor, not minding the process."
        elif action == "rest":
            return "{pet_name} rests deeply, feeling completely at ease in your care."
        else:
            return "{pet_name} enjoys a relaxed and easygoing relationship with you."
    elif personality == "Caring":
        if action == "feed":
            return "{pet_name} eats with gratitude, showing a strong bond and appreciation for your care."
        elif action == "play":
            return "{pet_name} plays with affection, cherishing the time spent together."
        elif action == "clean":
            return "{pet_name} stays still and cooperative, trusting your care and attention."
        elif action == "rest":
            return "{pet_name} rests peacefully, feeling loved and secure in your presence."
        else:
            return "{pet_name} deeply values the caring relationship you share."
    elif personality == "Energetic":
        if action == "feed":
            return "{pet_name} eats quickly, fueled by the energy and excitement you provide!"
        elif action == "play":
            return "{pet_name} plays with boundless energy, loving every moment of fun and activity!"
        elif action == "clean":
            return "{pet_name} fidgets during cleaning, eager to get back to playing and having fun!"
        elif action == "rest":
            return "{pet_name} struggles to rest, always buzzing with energy and ready for the next adventure!"
        else:
            return "{pet_name} is full of energy and always ready for fun with you!"
    elif personality == "Balanced":
        if action == "feed":
            return "{pet_name} eats with contentment, enjoying the balance of care and attention you provide."
        elif action == "play":
            return "{pet_name} plays with enthusiasm, appreciating the fun and connection you share."
        elif action == "clean":
            return "{pet_name} cooperates during cleaning, understanding the importance of care and hygiene."
        elif action == "rest":
            return "{pet_name} rests comfortably, feeling secure and well-cared for in your presence."
        else:
            return "{pet_name} enjoys a balanced and harmonious relationship with you."
    else:        return "{pet_name} responds in a unique way, reflecting its individual personality and the care you provide."

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
