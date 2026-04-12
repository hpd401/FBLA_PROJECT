# Visual Minigames Documentation

## Overview
All three minigames now feature visual Pygame interfaces with animations, timers, and feedback systems.

---

## 1. Treat Catch - Hunger Minigame 🎾

### Game Description
A top-down basket catching game where treats fall from the top of the screen and must be caught.

### Visual Elements
- **Playing Field**: Ocean blue background
- **Basket**: Yellow/brown rectangle at bottom, controlled by left/right arrows or A/D keys
- **Treats**: Falling orange/yellow circles with randomized spawn timing
- **Score Display**: Shows real-time score, time remaining, and title
- **Duration**: 15 seconds (customizable)

### Scoring System
- Each treat caught = 1 point
- **Rewards based on score**:
  - Hunger: min(10 + score × 8, 100)
  - Dollars: score × 3  
  - Happiness: min(score × 4, 100)

### Controls
- **Left Arrow** or **A Key**: Move basket left
- **Right Arrow** or **D Key**: Move basket right
- **Mouse Position** (optional): Can control with mouse

### Difficulty
Easy to Medium - depends on player reflexes

---

## 2. Medicine Rush - Health Minigame 💊

### Game Description
A quick-time reaction minigame where the player must respond to a "NOW!" prompt by pressing any key quickly.

### Visual Elements
- **Background**: Deep blue (medical theme)
- **Title**: "💊 MEDICINE RUSH 💊" in yellow
- **Countdown**: Animated number countdown during wait phase
- **Medicine Bottle**: Visual bottle graphic showing the medicine to be administered
- **Pet's Mouth**: Simplified graphic showing where medicine goes
- **Prompt**: Large red "NOW!" text when ready
- **Result Display**: Color-coded feedback with reaction time

### Game Flow
1. **Wait Phase**: Countdown displays 3-2-1
2. **Ready Phase**: "NOW!" appears on screen
3. **Reaction Window**: Player has 3 seconds to respond
4. **Result Phase**: Shows performance feedback

### Scoring System
- **< 0.8 seconds**: Perfect! Health +20, Dollars +20
- **0.8 - 1.6 seconds**: Good! Health +10, Dollars +10
- **> 1.6 seconds**: Too slow! Health -5, Dollars +5

### Visual Feedback
- 🟢 Green: Perfect timing
- 🟡 Yellow: Good timing
- 🔴 Red: Slow response

### Controls
- **Any Key** to respond
- **Mouse Click** to respond

---

## 3. Trick Time - Happiness Minigame ✨

### Game Description
A performance-based minigame where the pet performs tricks and the player responds quickly.

### Visual Elements
- **Background**: Medium blue with purple accent
- **Title**: "✨ TRICK TIME ✨" with sparkles
- **Pet Graphic**: 
  - Purple circle (body)
  - Purple circle (head)
  - White eyes
  - Animation: Jumping/spinning tricks
- **Gold Accents**: Sparkles and highlights
- **Action Text**: "Flip! Spin! Jump!" shows during trick performance
- **Result Display**: Emoji-based feedback

### Game Flow
1. **Setup Phase**: Countdown (GET READY FOR THE TRICK...)
2. **Trick Phase**: Pet animates performing tricks with "GO!" prompt
3. **Reaction Window**: Player has 3 seconds to respond
4. **Result Phase**: Shows performance and happiness reward

### Scoring System
- **< 0.8 seconds**: Amazing Trick! Happiness +20
- **0.8 - 1.6 seconds**: Nice Trick! Happiness +10
- **> 1.6 seconds**: Good Effort! Happiness +5

### Visual Feedback
- ⭐ Gold: Amazing trick
- 👍 Green: Nice trick
- ✓ White: Good effort

### Controls
- **Any Key** to respond
- **Mouse Click** to respond

### Animation
- Pet jumping animation loops when trick is performing
- Animated countdown during wait phase
- Smooth transitions between game states

---

## Technical Implementation

### File: minigames.py

#### Function Signatures
```python
def minigame_hunger(duration: int = 15) -> Dict[str, int]:
    """Returns {'hunger', 'dollars', 'happiness'}"""

def minigame_health() -> Dict[str, int]:
    """Returns {'health', 'dollars'}"""

def minigame_happiness() -> Dict[str, int]:
    """Returns {'happiness'}"""
```

#### Error Handling
All minigames include:
- Try/except error handling
- Graceful fallback to console versions if Pygame fails
- Proper pygame.quit() calls on exit
- Safe handling of user interruption

#### Fallback Modes
If Pygame visual mode fails:
- **Hunger**: Text-based button pressing challenge
- **Health**: Console reaction time test
- **Happiness**: Console trick performance test

### Performance
- 60 FPS render loop
- Efficient sprite/shape rendering
- Minimal memory overhead
- Timeout handling prevents infinite loops

---

## Integration with Game Core

### Calling Minigames from Core.py
```python
from minigames import minigame_hunger, minigame_health, minigame_happiness

# Run hunger minigame
result = minigame_hunger()  # Returns {'hunger': value, 'dollars': value, 'happiness': value}

# Run health minigame  
result = minigame_health()  # Returns {'health': value, 'dollars': value}

# Run happiness minigame
result = minigame_happiness()  # Returns {'happiness': value}
```

### Updating Pet Stats
```python
def play_minigame(state):
    """Update pet stats based on minigame result"""
    result = minigame_happiness()
    
    state.happiness += result.get('happiness', 0)
    if 'hunger' in result:
        state.hunger += result['hunger']
    if 'health' in result:
        state.health += result['health']
    if 'dollars' in result:
        economy.add_currency(result['dollars'])
    
    state.cap_stats()
```

---

## Color Reference

### Minigame Colors
- Medicine Rush: Red (200, 50, 50), Dark Blue (30, 60, 110)
- Trick Time: Purple (200, 100, 200), Gold (255, 215, 0)
- Treat Catch: Ocean Blue (15, 60, 110), Yellow (255, 220, 120)

### Feedback Colors
- Success: Green (50, 200, 50)
- Warning: Yellow (255, 255, 0)
- Alert: Red (200, 50, 50)
- Neutral: White (255, 255, 255)

---

## Future Enhancements

Potential improvements for minigames:
1. Sound effects and background music
2. Progressive difficulty levels
3. Achievement badges for perfect plays
4. Leaderboard integration
5. Pet-specific minigame variations
6. Power-up items during games
7. Combo multipliers for quick succession
8. Visual preferences/themes

---

## Testing Recommendations

1. **Test without Pygame**: Verify console fallbacks work
2. **Test timeout scenarios**: Ensure 3-second timeouts work
3. **Test edge cases**: Perfect timing, no response, etc.
4. **Test exit handling**: Proper cleanup on ESC/quit
5. **Test reward calculations**: Verify stat updates
6. **Test with different screen sizes**: Scaling performance
