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


def minigame_health(timeout: int = 3) -> Dict[str, int]:
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

    screen = None
    try:
        pygame.init()
        screen_width, screen_height = 800, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Snugbit Medicine Rush")
        clock = pygame.time.Clock()
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
                    pygame.quit()
                    sys.exit()
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
                    health_reward = 20
                    dollars_reward = 20
                elif reaction_time < 1.6:
                    result = "🟡 GOOD! Medicine was a bit late."
                    result_color = yellow
                    health_reward = 10
                    dollars_reward = 10
                else:
                    result = "🔴 TOO SLOW! Pet was sick longer."
                    result_color = red
                    health_reward = -5
                    dollars_reward = 5

                result_text = font_medium.render(result, True, result_color)
                result_rect = result_text.get_rect(center=(screen_width // 2, 480))
                screen.blit(result_text, result_rect)

                time_text = font_small.render(f"Reaction time: {reaction_time:.2f}s", True, white)
                time_rect = time_text.get_rect(center=(screen_width // 2, 540))
                screen.blit(time_text, time_rect)

                # Wait 2 seconds then exit
                if state == "timeout":
                    if pygame.time.get_ticks() - (now_shown_time if now_shown_time else wait_start) > 5000:
                        return {'health': health_reward, 'dollars': dollars_reward}

            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(f"Visual medicine minigame failed: {e}")
        # Fallback (don't quit pygame, just return)
        return {'health': 10, 'dollars': 10}




def minigame_happiness() -> Dict[str, int]:
    """Visual trick-time minigame for happiness."""
    if pygame is None:
        # Console fallback
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

    screen = None
    try:
        pygame.init()
        screen_width, screen_height = 800, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Snugbit Trick Time")
        clock = pygame.time.Clock()
        font_large = pygame.font.Font(None, 60)
        font_medium = pygame.font.Font(None, 40)
        font_small = pygame.font.Font(None, 28)

        # Colors
        bg_color = (60, 120, 180)
        purple = (200, 100, 200)
        gold = (255, 215, 0)
        white = (255, 255, 255)
        green = (100, 200, 100)

        # Game state
        state = "waiting"  # waiting, counting, show_now, timeout
        wait_duration = random.uniform(0.8, 2.5)
        wait_start = pygame.time.get_ticks()
        now_shown_time = None
        reaction_time = None
        trick_counter = 0

        while True:
            now = pygame.time.get_ticks()
            elapsed_ms = now - wait_start

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    if state == "show_now":
                        reaction_time = elapsed_ms / 1000.0 - wait_duration
                        state = "timeout"

            screen.fill(bg_color)

            # Draw title with sparkles
            title = font_medium.render("✨ TRICK TIME ✨", True, gold)
            title_rect = title.get_rect(center=(screen_width // 2, 40))
            screen.blit(title, title_rect)

            # Draw instructions
            if state == "waiting":
                if elapsed_ms / 1000.0 < wait_duration:
                    instruction = font_small.render("GET READY FOR THE TRICK...", True, white)
                    instruction_rect = instruction.get_rect(center=(screen_width // 2, 120))
                    screen.blit(instruction, instruction_rect)

                    # Countdown
                    remaining = wait_duration - (elapsed_ms / 1000.0)
                    countdown = font_large.render(f"{max(0, int(remaining) + 1)}", True, gold)
                    countdown_rect = countdown.get_rect(center=(screen_width // 2, 200))
                    screen.blit(countdown, countdown_rect)
                else:
                    state = "show_now"
                    now_shown_time = pygame.time.get_ticks()

            elif state == "show_now":
                now_text = font_large.render("GO!", True, gold)
                now_rect = now_text.get_rect(center=(screen_width // 2, 100))
                screen.blit(now_text, now_rect)

                instruction = font_medium.render("Press any key or click!", True, white)
                instruction_rect = instruction.get_rect(center=(screen_width // 2, 200))
                screen.blit(instruction, instruction_rect)

                # Timeout after 3 seconds
                show_elapsed = (pygame.time.get_ticks() - now_shown_time) / 1000.0
                if show_elapsed > 3.0:
                    reaction_time = 3.0
                    state = "timeout"

            # Draw pet performing trick (animated)
            pet_x = screen_width // 2
            pet_y = 350
            animation_frame = (pygame.time.get_ticks() // 100) % 4

            # Pet body
            pygame.draw.circle(screen, purple, (pet_x, pet_y), 30)

            # Pet head
            pygame.draw.circle(screen, purple, (pet_x, pet_y - 35), 20)

            # Eyes
            pygame.draw.circle(screen, white, (pet_x - 8, pet_y - 38), 4)
            pygame.draw.circle(screen, white, (pet_x + 8, pet_y - 38), 4)

            # Trick animation - jumping
            jump_height = 20 * abs((animation_frame - 1.5) / 1.5) if state == "show_now" else 0
            pygame.draw.line(screen, gold, (pet_x - 20, pet_y + 5), (pet_x - 20, pet_y + 35 - jump_height), 3)
            pygame.draw.line(screen, gold, (pet_x + 20, pet_y + 5), (pet_x + 20, pet_y + 35 - jump_height), 3)

            # Draw action indicator
            if state == "show_now":
                action_text = font_small.render("Flip! Spin! Jump!", True, gold)
                action_rect = action_text.get_rect(center=(pet_x, pet_y + 70))
                screen.blit(action_text, action_rect)

            # Show result
            if reaction_time is not None:
                if reaction_time < 0.8:
                    result = "⭐ AMAZING TRICK! Pet loved it!"
                    result_color = gold
                    happiness_reward = 20
                elif reaction_time < 1.6:
                    result = "👍 NICE TRICK! Pet enjoyed it."
                    result_color = green
                    happiness_reward = 10
                else:
                    result = "✓ GOOD EFFORT! Pet appreciated it."
                    result_color = white
                    happiness_reward = 5

                result_text = font_medium.render(result, True, result_color)
                result_rect = result_text.get_rect(center=(screen_width // 2, 480))
                screen.blit(result_text, result_rect)

                time_text = font_small.render(f"Reaction time: {reaction_time:.2f}s", True, white)
                time_rect = time_text.get_rect(center=(screen_width // 2, 540))
                screen.blit(time_text, time_rect)

                # Wait 2 seconds then exit
                if state == "timeout":
                    if pygame.time.get_ticks() - (now_shown_time if now_shown_time else wait_start) > 5000:
                        return {'happiness': happiness_reward}

            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(f"Visual trick minigame failed: {e}")
        # Fallback (don't quit pygame, just return)
        return {'happiness': 10}




def minigame_hunger(duration: int = 15) -> Dict[str, int]:
    """Top-down basket catching game where falling treats must be caught."""
    if pygame is None:
        print("Pygame not available. Using console fallback for hunger minigame.")
        return _minigame_hunger_fallback(duration)

    screen = None
    try:
        pygame.init()
        screen_width, screen_height = 640, 480
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Snugbit Treat Catch")
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
                    pygame.quit()
                    sys.exit()

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
        hunger = min(10 + score * 8, 100)
        dollars = score * 3
        happiness = min(score * 4, 100)
        return {'hunger': hunger, 'dollars': dollars, 'happiness': happiness}
    except Exception:
        print("Graphical game failed, falling back to console hunger minigame.")
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
