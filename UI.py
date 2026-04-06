import pygame
import sys

class TitleScreen:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption("Snugbit - Virtual Pet Game")
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
            self.title_text = self.title_font.render("Snugbit", True, self.WHITE)
            self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4))

            # Subtitle
            self.subtitle_font = pygame.font.Font(None, 24)
            self.subtitle_text = self.subtitle_font.render("Virtual Pet Adventure", True, self.WHITE)
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
            print("No display available, skipping title screen.")
            return "start_game"
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        running = True
        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 5000:  # 5 seconds timeout
                running = False
                break

            self.screen.fill(self.BLACK)

            # Draw title
            self.screen.blit(self.title_text, self.title_rect)
            self.screen.blit(self.subtitle_text, self.subtitle_rect)

            # Draw buttons
            self.draw_button(self.start_button, "Start Game", self.GREEN)
            self.draw_button(self.quit_button, "Quit", self.BLUE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        running = False  # Proceed to game
                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        return "start_game"

class PetSelection:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption("Choose Your Pet")
            self.display_available = True

            # Colors
            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.BLUE = (0, 0, 255)
            self.GREEN = (0, 255, 0)
            self.RED = (255, 0, 0)
            self.YELLOW = (255, 255, 0)

            # Fonts
            self.title_font = pygame.font.Font(None, 48)
            self.button_font = pygame.font.Font(None, 24)

            # Title
            self.title_text = self.title_font.render("Choose Your Pet", True, self.WHITE)
            self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, 50))

            # Pet buttons
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
            print("No display available, defaulting to Dog.")
            return "Dog"
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        running = True
        selected_pet = None
        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 10000:  # 10 seconds timeout, default to Dog
                selected_pet = "Dog"
                running = False
                break
            self.screen.fill(self.BLACK)

            # Draw title
            self.screen.blit(self.title_text, self.title_rect)

            # Draw pet buttons
            self.draw_button(self.dog_button, "Dog", self.BLUE)
            self.draw_button(self.cat_button, "Cat", self.GREEN)
            self.draw_button(self.bird_button, "Bird", self.YELLOW)
            self.draw_button(self.robot_button, "Robot", self.RED)
            self.draw_button(self.back_button, "Back", self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dog_button.collidepoint(event.pos):
                        selected_pet = "Dog"
                        running = False
                    elif self.cat_button.collidepoint(event.pos):
                        selected_pet = "Cat"
                        running = False
                    elif self.bird_button.collidepoint(event.pos):
                        selected_pet = "Bird"
                        running = False
                    elif self.robot_button.collidepoint(event.pos):
                        selected_pet = "Robot"
                        running = False
                    elif self.back_button.collidepoint(event.pos):
                        selected_pet = "back"
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_pet = "Dog"
                        running = False
                    elif event.key == pygame.K_2:
                        selected_pet = "Cat"
                        running = False
                    elif event.key == pygame.K_3:
                        selected_pet = "Bird"
                        running = False
                    elif event.key == pygame.K_4:
                        selected_pet = "Robot"
                        running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        return selected_pet

if __name__ == "__main__":
    title = TitleScreen()
    result = title.run()
    print(result)  # For testing
