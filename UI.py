import pygame
import sys


class TitleScreen:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption('Snugbit - Virtual Pet Game')
            self.display_available = True

            # Colors
            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.BLUE = (0, 0, 255)
            self.GREEN = (0, 255, 0)

            # Fonts
            self.title_font = pygame.font.Font(None, 72)
            self.button_font = pygame.font.Font(None, 36)

            # Title text
            self.title_text = self.title_font.render('Snugbit', True, self.WHITE)
            self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4))

            # Subtitle
            self.subtitle_font = pygame.font.Font(None, 24)
            self.subtitle_text = self.subtitle_font.render('Virtual Pet Adventure', True, self.WHITE)
            self.subtitle_rect = self.subtitle_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4 + 80))

            # Buttons
            self.start_button = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2, 200, 50)
            self.quit_button = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2 + 70, 200, 50)
        except Exception:
            self.display_available = False

    def draw_button(self, rect, text, color):
        pygame.draw.rect(self.screen, color, rect)
        text_surf = self.button_font.render(text, True, self.BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def run(self):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, skipping title screen.')
            return 'start_game'
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        running = True
        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 5000:  # 5 seconds timeout
                running = False
                break

            self.screen.fill(self.BLACK)
            self.screen.blit(self.title_text, self.title_rect)
            self.screen.blit(self.subtitle_text, self.subtitle_rect)
            self.draw_button(self.start_button, 'Start Game', self.GREEN)
            self.draw_button(self.quit_button, 'Quit', self.BLUE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        running = False
                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        return 'start_game'


class PetSelection:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption('Choose Your Pet')
            self.display_available = True

            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.BLUE = (0, 0, 255)
            self.GREEN = (0, 255, 0)
            self.RED = (255, 0, 0)
            self.YELLOW = (255, 255, 0)

            self.title_font = pygame.font.Font(None, 48)
            self.button_font = pygame.font.Font(None, 24)

            self.title_text = self.title_font.render('Choose Your Pet', True, self.WHITE)
            self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, 50))

            self.dog_button = pygame.Rect(100, 150, 150, 100)
            self.cat_button = pygame.Rect(300, 150, 150, 100)
            self.bird_button = pygame.Rect(500, 150, 150, 100)
            self.robot_button = pygame.Rect(200, 300, 150, 100)
            self.back_button = pygame.Rect(450, 300, 150, 100)
        except Exception:
            self.display_available = False

    def draw_button(self, rect, text, color):
        pygame.draw.rect(self.screen, color, rect)
        text_surf = self.button_font.render(text, True, self.BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def run(self):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, defaulting to Dog.')
            return 'Dog'
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        running = True
        selected_pet = None
        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 10000:
                selected_pet = 'Dog'
                running = False
                break

            self.screen.fill(self.BLACK)
            self.screen.blit(self.title_text, self.title_rect)
            self.draw_button(self.dog_button, 'Dog', self.BLUE)
            self.draw_button(self.cat_button, 'Cat', self.GREEN)
            self.draw_button(self.bird_button, 'Bird', self.YELLOW)
            self.draw_button(self.robot_button, 'Robot', self.RED)
            self.draw_button(self.back_button, 'Back', self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dog_button.collidepoint(event.pos):
                        selected_pet = 'Dog'
                        running = False
                    elif self.cat_button.collidepoint(event.pos):
                        selected_pet = 'Cat'
                        running = False
                    elif self.bird_button.collidepoint(event.pos):
                        selected_pet = 'Bird'
                        running = False
                    elif self.robot_button.collidepoint(event.pos):
                        selected_pet = 'Robot'
                        running = False
                    elif self.back_button.collidepoint(event.pos):
                        selected_pet = 'back'
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_pet = 'Dog'
                        running = False
                    elif event.key == pygame.K_2:
                        selected_pet = 'Cat'
                        running = False
                    elif event.key == pygame.K_3:
                        selected_pet = 'Bird'
                        running = False
                    elif event.key == pygame.K_4:
                        selected_pet = 'Robot'
                        running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        return selected_pet


class TutorialScreen:
    def __init__(self, screen, steps):
        self.screen = screen
        self.steps = steps
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 48)

    def draw_step(self, text, step_index):
        self.screen.fill((30, 30, 40))
        overlay = pygame.Surface((self.width - 120, self.height - 120), pygame.SRCALPHA)
        overlay.fill((10, 10, 10, 220))
        self.screen.blit(overlay, (60, 60))

        title = self.title_font.render('Tutorial', True, (255, 255, 255))
        self.screen.blit(title, title.get_rect(center=(self.width // 2, 120)))

        lines = self.wrap_text(text, self.font, self.width - 160)
        y = 180
        for line in lines:
            rendered = self.font.render(line, True, (230, 230, 230))
            self.screen.blit(rendered, (80, y))
            y += 36

        hint = self.font.render('Press any key to continue...', True, (180, 180, 180))
        self.screen.blit(hint, hint.get_rect(center=(self.width // 2, self.height - 100)))

        step_label = self.font.render(f'Step {step_index + 1} of {len(self.steps)}', True, (200, 200, 200))
        self.screen.blit(step_label, (80, self.height - 100))

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current = ''
        for word in words:
            test = f'{current} {word}'.strip()
            if font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines

    def run(self):
        clock = pygame.time.Clock()
        for index, step in enumerate(self.steps):
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.KEYDOWN:
                        waiting = False
                self.draw_step(step, index)
                pygame.display.flip()
                clock.tick(60)
        return True


class HubScreen:
    def __init__(self, screen, pet_name, pet_type, animations):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.animations = animations
        self.pet_x = 120
        self.pet_y = self.height - 160
        self.speed = 4
        self.direction = 'right'
        self.walking = False
        self.frame_timer = 0
        self.current_frame = 0
        self.message = 'Use arrow keys to move. Press E to interact.'
        self.font = pygame.font.Font(None, 28)
        self.title_font = pygame.font.Font(None, 40)

        self.action_spots = [
            {'name': 'Feed', 'rect': pygame.Rect(100, 420, 120, 120), 'color': (230, 180, 90), 'label': 'Food Bowl'},
            {'name': 'Play', 'rect': pygame.Rect(300, 360, 140, 140), 'color': (160, 220, 180), 'label': 'Play Area'},
            {'name': 'Rest', 'rect': pygame.Rect(520, 420, 120, 120), 'color': (140, 170, 240), 'label': 'Bed'},
            {'name': 'Clean', 'rect': pygame.Rect(620, 180, 120, 120), 'color': (220, 200, 220), 'label': 'Bath'},
            {'name': 'Mini Game', 'rect': pygame.Rect(100, 180, 140, 120), 'color': (255, 140, 140), 'label': 'Mini Game'},
        ]

    def get_pet_rect(self):
        sprite = self.get_current_sprite()
        return pygame.Rect(self.pet_x, self.pet_y, sprite.get_width(), sprite.get_height())

    def get_animation_frames(self):
        if self.walking:
            if self.direction == 'right':
                return self.animations.get('walk_right', self.animations.get('idle', []))
            elif self.direction == 'left':
                return self.animations.get('walk_left', self.animations.get('idle', []))
            elif self.direction == 'up':
                return self.animations.get('walk_up', self.animations.get('idle', []))
            elif self.direction == 'down':
                return self.animations.get('walk_down', self.animations.get('idle', []))
        return self.animations.get('idle', [])

    def get_current_sprite(self):
        frames = self.get_animation_frames()
        if not frames:
            return pygame.Surface((64, 64), pygame.SRCALPHA)
        return frames[self.current_frame % len(frames)]

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.walking = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pet_x -= self.speed
            self.direction = 'left'
            self.walking = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pet_x += self.speed
            self.direction = 'right'
            self.walking = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pet_y -= self.speed
            self.direction = 'up'
            self.walking = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pet_y += self.speed
            self.direction = 'down'
            self.walking = True

        sprite = self.get_current_sprite()
        self.pet_x = max(0, min(self.pet_x, self.width - sprite.get_width()))
        self.pet_y = max(0, min(self.pet_y, self.height - sprite.get_height()))

    def update(self, dt):
        if self.walking:
            self.frame_timer += dt
            frames = self.get_animation_frames()
            if self.frame_timer > 120 and frames:
                self.frame_timer = 0
                self.current_frame = (self.current_frame + 1) % len(frames)

    def get_current_spot(self):
        pet_rect = self.get_pet_rect()
        for spot in self.action_spots:
            if spot['rect'].colliderect(pet_rect):
                return spot
        return None

    def draw(self):
        self.screen.fill((90, 180, 210))
        pygame.draw.rect(self.screen, (100, 180, 100), (0, self.height - 160, self.width, 160))
        pygame.draw.rect(self.screen, (70, 130, 180), (0, 0, self.width, 100))

        title = self.title_font.render(f"{self.pet_name}'s Home", True, (255, 255, 255))
        self.screen.blit(title, (28, 20))
        hint = self.font.render('Walk to a spot and press E to interact', True, (240, 240, 240))
        self.screen.blit(hint, (28, 68))

        for spot in self.action_spots:
            pygame.draw.rect(self.screen, spot['color'], spot['rect'])
            label = self.font.render(spot['label'], True, (20, 20, 20))
            self.screen.blit(label, label.get_rect(center=spot['rect'].center))

        pet_sprite = self.get_current_sprite()
        self.screen.blit(pet_sprite, (self.pet_x, self.pet_y))

        spot = self.get_current_spot()
        if spot:
            prompt = self.font.render(f"Press E to {spot['name']}", True, (255, 255, 255))
            self.screen.blit(prompt, (28, self.height - 120))

        message = self.font.render(self.message, True, (255, 255, 255))
        self.screen.blit(message, (28, self.height - 90))

    def run(self, on_action):
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_e:
                        spot = self.get_current_spot()
                        if spot:
                            result = on_action(spot['name'])
                            self.message = result or self.message
            self.handle_input()
            self.update(dt)
            self.draw()
            pygame.display.flip()
        return


if __name__ == '__main__':
    title = TitleScreen()
    result = title.run()
    print(result)
