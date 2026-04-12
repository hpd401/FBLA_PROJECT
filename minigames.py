
# Minigames for Snugbit
import time
import random
from typing import Dict

try:
    import pygame
    import sys
except ImportError:
    pygame = None
    sys = None


def minigame_health(timeout: int = 3, screen=None, is_fullscreen=False) -> Dict[str, int]:
    """Visual quick-time minigame for administering medicine."""
    if pygame is None:
        # Console fallback
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

    original_screen = screen
    try:
        pygame.init()
        if screen is None:
            screen_width, screen_height = 800, 600
            flag = pygame.FULLSCREEN if is_fullscreen else 0
            screen = pygame.display.set_mode((screen_width, screen_height), flag, vsync=1)
            pygame.display.set_caption("Snugbit Medicine Rush")
        else:
            screen_width = screen.get_width()
            screen_height = screen.get_height()
        font_large = pygame.font.Font(None, 60)
        font_medium = pygame.font.Font(None, 40)
        font_small = pygame.font.Font(None, 28)

        # Colors
        bg_color = (30, 60, 110)
        red = (200, 50, 50)
        green = (50, 200, 50)
        white = (255, 255, 255)
        yellow = (255, 255, 0)

        # Game state
        state = "waiting"  # waiting, counting, show_now, timeout
        wait_duration = random.uniform(1.5, 3.5)
        wait_start = pygame.time.get_ticks()
        now_shown_time = None
        reaction_time = None
        medicine_y = screen_height - 100
        medicine_drawn = False

        while True:
            now = pygame.time.get_ticks()
            elapsed_ms = now - wait_start

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if original_screen is None:
                        pygame.quit()
                        sys.exit()
                    return {'health': 10, 'dollars': 10}
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    if state == "show_now":
                        reaction_time = elapsed_ms / 1000.0 - wait_duration
                        state = "timeout"

            screen.fill(bg_color)

            # Draw title
            title = font_medium.render("💊 MEDICINE RUSH 💊", True, yellow)
            title_rect = title.get_rect(center=(screen_width // 2, 40))
            screen.blit(title, title_rect)

            # Draw instructions
            if state == "waiting":
                if elapsed_ms / 1000.0 < wait_duration:
                    instruction = font_small.render("GET READY...", True, white)
                    instruction_rect = instruction.get_rect(center=(screen_width // 2, 120))
                    screen.blit(instruction, instruction_rect)

                    # Countdown
                    remaining = wait_duration - (elapsed_ms / 1000.0)
                    countdown = font_large.render(f"{max(0, int(remaining) + 1)}", True, yellow)
                    countdown_rect = countdown.get_rect(center=(screen_width // 2, 200))
                    screen.blit(countdown, countdown_rect)
                else:
                    state = "show_now"
                    now_shown_time = pygame.time.get_ticks()

            elif state == "show_now":
                now_text = font_large.render("NOW!", True, red)
                now_rect = now_text.get_rect(center=(screen_width // 2, 150))
                screen.blit(now_text, now_rect)

                instruction = font_medium.render("Press any key or click!", True, yellow)
                instruction_rect = instruction.get_rect(center=(screen_width // 2, 280))
                screen.blit(instruction, instruction_rect)

                # Timeout after 3 seconds
                show_elapsed = (pygame.time.get_ticks() - now_shown_time) / 1000.0
                if show_elapsed > 3.0:
                    reaction_time = 3.0
                    state = "timeout"

            # Draw medicine bottle
            bottle_x = screen_width // 2 - 15
            bottle_y = 350
            pygame.draw.rect(screen, red, (bottle_x - 15, bottle_y, 30, 80))  # Bottle body
            pygame.draw.rect(screen, (255, 200, 0), (bottle_x - 5, bottle_y - 10, 10, 15))  # Cap
            pygame.draw.line(screen, white, (bottle_x - 15, bottle_y + 40), (bottle_x + 15, bottle_y + 40), 2)  # Fill line

            # Draw pet's mouth (simplified)
            pygame.draw.circle(screen, (200, 150, 100), (screen_width // 2, bottle_y + 100), 20)
            pygame.draw.line(screen, white, (screen_width // 2 - 15, bottle_y + 100), (screen_width // 2 + 15, bottle_y + 100), 3)

            # Show result
            if reaction_time is not None:
                if reaction_time < 0.8:
                    result = "🟢 PERFECT! Medicine given on time!"
                    result_color = green
                    health_reward = 40
                    dollars_reward = 40
                elif reaction_time < 1.6:
                    result = "🟡 GOOD! Medicine was a bit late."
                    result_color = yellow
                    health_reward = 20
                    dollars_reward = 20
                else:
                    result = "🔴 TOO SLOW! Pet was sick longer."
                    result_color = red
                    health_reward = 0
                    dollars_reward = 10

                result_text = font_medium.render(result, True, result_color)
                result_rect = result_text.get_rect(center=(screen_width // 2, 480))
                screen.blit(result_text, result_rect)

                time_text = font_small.render(f"Reaction time: {reaction_time:.2f}s", True, white)
                time_rect = time_text.get_rect(center=(screen_width // 2, 540))
                screen.blit(time_text, time_rect)

                # Wait 2 seconds then exit
                if state == "timeout":
                    if pygame.time.get_ticks() - (now_shown_time if now_shown_time else wait_start) > 5000:
                        # Clear input buffer before returning to hub
                        pygame.event.clear()
                        return {'health': health_reward, 'dollars': dollars_reward}

            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(f"Visual medicine minigame failed: {e}")
        if original_screen is None:
            pygame.quit()
        return {'health': 10, 'dollars': 10}




def minigame_happiness(screen=None, is_fullscreen=False) -> Dict[str, int]:
    """Simon Says minigame for happiness."""
    if pygame is None:
        # Console fallback
        print("Simon Says: Trick Time! Repeat the sequence of button presses.")
        print("Use: LEFT (A), RIGHT (D), UP (W), DOWN (S)")
        sequence = []
        correct_presses = 0
        
        while correct_presses < 5:
            next_move = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
            sequence.append(next_move)
            print(f"Sequence: {' -> '.join(sequence)}")
            
            player_seq = []
            for expected in sequence:
                move = input(f"Enter move ({expected}): ").upper()
                if move not in ['LEFT', 'RIGHT', 'UP', 'DOWN', 'A', 'D', 'W', 'S']:
                    print("Invalid move!")
                    return {'happiness': 5 + correct_presses * 2}
                player_seq.append(move)
            
            if player_seq[-1].lower() not in ['left', 'a', 'right', 'd', 'up', 'w', 'down', 's']:
                print("Wrong move! Game over.")
                return {'happiness': 5 + correct_presses * 3}
            correct_presses += 1
        
        return {'happiness': 40}

    original_screen = screen
    try:
        pygame.init()
        if screen is None:
            screen_width, screen_height = 800, 600
            flag = pygame.FULLSCREEN if is_fullscreen else 0
            screen = pygame.display.set_mode((screen_width, screen_height), flag, vsync=1)
        else:
            screen_width = screen.get_width()
            screen_height = screen.get_height()
        
        pygame.display.set_caption("Snugbit Simon Says")
        clock = pygame.time.Clock()
        font_large = pygame.font.Font(None, 60)
        font_medium = pygame.font.Font(None, 40)
        font_small = pygame.font.Font(None, 28)

        # Colors
        bg_color = (40, 80, 140)
        gold = (255, 215, 0)
        white = (255, 255, 255)
        green = (100, 200, 100)
        red = (200, 100, 100)
        blue = (100, 150, 255)

        # Simon Says game state
        sequence = []
        player_sequence = []
        level = 0
        showing_sequence = False
        show_index = 0
        show_time = 0
        game_over = False
        result_message = ""
        result_color = white

        # Direction buttons
        button_size = 80
        button_spacing = 20
        button_y = screen_height // 2 - button_size // 2
        
        buttons = [
            {'name': 'UP', 'color': (100, 200, 100), 'key': pygame.K_w, 'x': screen_width // 2 - button_size // 2},
            {'name': 'LEFT', 'color': (200, 150, 100), 'key': pygame.K_a, 'x': screen_width // 2 - button_size - button_spacing},
            {'name': 'RIGHT', 'color': (100, 150, 200), 'key': pygame.K_d, 'x': screen_width // 2 + button_spacing},
            {'name': 'DOWN', 'color': (200, 100, 150), 'key': pygame.K_s, 'x': screen_width // 2 - button_size // 2},
        ]

        while True:
            now = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if original_screen is None:
                        pygame.quit()
                    return {'happiness': 5 + level * 3}
                elif event.type == pygame.KEYDOWN:
                    if level == 0 and not showing_sequence and not game_over:
                        # Start game
                        sequence = [random.choice(['UP', 'LEFT', 'RIGHT', 'DOWN'])]
                        showing_sequence = True
                        show_index = 0
                        show_time = now
                    elif not showing_sequence and not game_over:
                        # Player input
                        move_found = False
                        for button in buttons:
                            if event.key == button['key']:
                                player_sequence.append(button['name'])
                                move_found = True
                                break
                        
                        if move_found:
                            # Check if correct
                            if player_sequence[-1] == sequence[len(player_sequence) - 1]:
                                # Correct move
                                if len(player_sequence) == len(sequence):
                                    # Level complete!
                                    level += 1
                                    if level >= 7:  # Win condition
                                        game_over = True
                                        result_message = f"🌟 AMAZING! You completed all {level} levels!"
                                        result_color = gold
                                    else:
                                        # Add next move to sequence
                                        sequence.append(random.choice(['UP', 'LEFT', 'RIGHT', 'DOWN']))
                                        player_sequence = []
                                        showing_sequence = True
                                        show_index = 0
                                        show_time = now
                            else:
                                # Wrong move
                                game_over = True
                                result_message = f"❌ You failed at level {level + 1}!"
                                result_color = red
                    elif game_over:
                        # Exit on any key after game over
                        if original_screen is None:
                            pygame.quit()
                        happiness = min(20, 5 + level * 3)
                        # Clear input buffer before returning to hub
                        pygame.event.clear()
                        return {'happiness': happiness}

            screen.fill(bg_color)

            # Draw title
            title = font_medium.render("🎮 SIMON SAYS 🎮", True, gold)
            title_rect = title.get_rect(center=(screen_width // 2, 40))
            screen.blit(title, title_rect)

            # Draw level
            level_text = font_medium.render(f"Level: {level}", True, white)
            level_rect = level_text.get_rect(center=(screen_width // 2, 100))
            screen.blit(level_text, level_rect)

            # Start game if first level
            if level == 0 and not showing_sequence and not game_over:
                instruction = font_small.render("Press any key to start!", True, white)
                instruction_rect = instruction.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
                screen.blit(instruction, instruction_rect)
                
                desc_text = font_small.render("Watch the pattern, then repeat it with arrow keys (W/A/S/D)", True, (200, 200, 255))
                desc_rect = desc_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
                screen.blit(desc_text, desc_rect)

            # Show sequence animation
            if showing_sequence:
                elapsed = now - show_time
                if elapsed > 500 and show_index < len(sequence):
                    show_index += 1
                    show_time = now
                
                if show_index >= len(sequence):
                    showing_sequence = False
                    player_sequence = []
                else:
                    # Highlight the current button in sequence
                    current_move = sequence[show_index]
                    for button in buttons:
                        if button['name'] == current_move:
                            color = tuple(min(c + 100, 255) for c in button['color'])
                            pygame.draw.rect(screen, color, (button['x'] - 10, button_y - 10, button_size + 20, button_size + 20))
                            break

            # Draw buttons
            for button in buttons:
                pygame.draw.rect(screen, button['color'], (button['x'], button_y, button_size, button_size))
                pygame.draw.rect(screen, white, (button['x'], button_y, button_size, button_size), 2)
                
                label = font_small.render(button['name'][:3], True, white)
                label_rect = label.get_rect(center=(button['x'] + button_size // 2, button_y + button_size // 2))
                screen.blit(label, label_rect)

            # Draw sequence progress
            if not game_over and level > 0:
                progress_text = font_small.render(f"Sequence: {' '.join(sequence)}", True, white)
                progress_rect = progress_text.get_rect(center=(screen_width // 2, screen_height - 100))
                screen.blit(progress_text, progress_rect)
                
                player_text = font_small.render(f"Your Input: {' '.join(player_sequence)}", True, blue)
                player_rect = player_text.get_rect(center=(screen_width // 2, screen_height - 50))
                screen.blit(player_text, player_rect)

            # Show result if game over
            if game_over:
                result_text = font_medium.render(result_message, True, result_color)
                result_rect = result_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
                screen.blit(result_text, result_rect)
                
                exit_text = font_small.render("Press any key to continue...", True, white)
                exit_rect = exit_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
                screen.blit(exit_text, exit_rect)

            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(f"Simon Says minigame failed: {e}")
        if original_screen is None:
            pygame.quit()
        return {'happiness': 10}




def minigame_hunger(duration: int = 15, screen=None, is_fullscreen=False) -> Dict[str, int]:
    """Top-down basket catching game where falling treats must be caught."""
    if pygame is None:
        print("Pygame not available. Using console fallback for hunger minigame.")
        return _minigame_hunger_fallback(duration)

    original_screen = screen
    try:
        pygame.init()
        if screen is None:
            screen_width, screen_height = 640, 480
            flag = pygame.FULLSCREEN if is_fullscreen else 0
            screen = pygame.display.set_mode((screen_width, screen_height), flag, vsync=1)
            pygame.display.set_caption("Snugbit Treat Catch")
        else:
            screen_width = screen.get_width()
            screen_height = screen.get_height()
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 32)

        basket = pygame.Rect(screen_width // 2 - 50, screen_height - 60, 100, 20)
        basket_speed = 8
        treats = []
        spawn_timer = 0
        spawn_interval = 700
        start_time = pygame.time.get_ticks()
        score = 0

        while True:
            now = pygame.time.get_ticks()
            elapsed = (now - start_time) / 1000.0
            if elapsed >= duration:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if original_screen is None:
                        pygame.quit()
                        sys.exit()
                    return {'hunger': 0, 'dollars': 0, 'happiness': 0}

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                basket.x -= basket_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                basket.x += basket_speed

            basket.x = max(0, min(basket.x, screen_width - basket.width))

            if now - spawn_timer > spawn_interval:
                spawn_timer = now
                treat_x = random.randint(20, screen_width - 20)
                treat_speed = random.uniform(3.0, 5.5)
                treats.append({'rect': pygame.Rect(treat_x, -20, 20, 20), 'speed': treat_speed})

            for treat in treats[:]:
                treat['rect'].y += treat['speed']
                if treat['rect'].colliderect(basket):
                    score += 1
                    treats.remove(treat)
                elif treat['rect'].top > screen_height:
                    treats.remove(treat)

            screen.fill((15, 60, 110))
            pygame.draw.rect(screen, (220, 180, 60), basket)
            for treat in treats:
                pygame.draw.ellipse(screen, (255, 220, 120), treat['rect'])

            title_text = font.render("Catch treats in the basket!", True, (255, 255, 255))
            timer_text = font.render(f"Time: {max(0, int(duration - elapsed))}", True, (255, 255, 255))
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(title_text, (20, 20))
            screen.blit(timer_text, (20, 60))
            screen.blit(score_text, (20, 100))

            pygame.display.flip()
            clock.tick(60)

        print(f"You caught {score} treats!")
        hunger = min(20 + score * 10, 100)
        dollars = score * 5
        happiness = min(score * 5, 100)
        # Clear input buffer before returning to hub
        pygame.event.clear()
        return {'hunger': hunger, 'dollars': dollars, 'happiness': happiness}
    except Exception:
        print("Graphical game failed, falling back to console hunger minigame.")
        if original_screen is None:
            pygame.quit()
        return _minigame_hunger_fallback(duration)


def _minigame_hunger_fallback(duration: int = 15) -> Dict[str, int]:
    print(f"Feeding Frenzy! Press Enter as many times as you can in {duration} seconds.")
    print("(Press Enter to start)")
    input()
    end_time = time.time() + duration
    presses = 0

    try:
        while time.time() < end_time:
            input()
            presses += 1
    except KeyboardInterrupt:
        print("Minigame interrupted.")

    score = presses
    print(f"You caught {score} treats!")
    hunger = min(10 + score * 6, 100)
    dollars = score * 2
    happiness = min(score * 3, 100)
    return {'hunger': hunger, 'dollars': dollars, 'happiness': happiness}
