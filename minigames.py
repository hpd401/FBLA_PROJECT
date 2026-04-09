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

        pygame.quit()

        print(f"You caught {score} treats!")
        hunger = min(10 + score * 8, 100)
        dollars = score * 3
        happiness = min(score * 4, 100)
        return {'hunger': hunger, 'dollars': dollars, 'happiness': happiness}
    except Exception:
        if screen is not None:
            pygame.quit()
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
