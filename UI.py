import pygame
import sys
import visual_reactions
from visual_reactions import ReactionAnimator, ReactionType


class TitleScreen:
    def __init__(self, screen_width=1280, screen_height=720, start_fullscreen=False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            flag = pygame.FULLSCREEN if start_fullscreen else 0
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flag, vsync=1)
            pygame.display.set_caption('Snugbit - Virtual Pet Game')
            self.display_available = True
            self.is_fullscreen = start_fullscreen

            # Colors
            self.BLACK = (0, 0, 0)
            self.DARK_BLUE = (25, 50, 100)
            self.LIGHT_BLUE = (100, 180, 255)
            self.WHITE = (255, 255, 255)
            self.GOLD = (255, 215, 0)
            self.GREEN = (100, 255, 100)

            # Fonts
            self.title_font = pygame.font.Font(None, 120)
            self.subtitle_font = pygame.font.Font(None, 48)
            self.button_font = pygame.font.Font(None, 48)
            self.hint_font = pygame.font.Font(None, 32)

            # Title text
            self.title_text = self.title_font.render('🐾 Snugbit 🐾', True, self.GOLD)
            self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4))

            # Subtitle
            self.subtitle_text = self.subtitle_font.render('Virtual Pet Adventure', True, self.LIGHT_BLUE)
            self.subtitle_rect = self.subtitle_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4 + 100))

            # Tagline
            self.tagline_text = self.hint_font.render('Care for your digital companion!', True, self.WHITE)
            self.tagline_rect = self.tagline_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4 + 180))

            # Buttons
            btn_width, btn_height = 250, 70
            self.start_button = pygame.Rect(self.screen_width // 2 - btn_width // 2, self.screen_height // 2 + 50, btn_width, btn_height)
            self.quit_button = pygame.Rect(self.screen_width // 2 - btn_width // 2, self.screen_height // 2 + 160, btn_width, btn_height)
        except Exception:
            self.display_available = False

    def draw_button(self, rect, text, color, border_color=None):
        pygame.draw.rect(self.screen, color, rect)
        if border_color:
            pygame.draw.rect(self.screen, border_color, rect, 4)
        text_surf = self.button_font.render(text, True, self.BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def run(self):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, skipping title screen.')
            return 'start_game'
        clock = pygame.time.Clock()
        running = True
        pygame.event.clear()  # Clear input buffer
        while running:
            # Gradient background effect
            for y in range(self.screen_height):
                color_val = int(25 + (100 - 25) * (y / self.screen_height))
                pygame.draw.line(self.screen, (color_val // 4, color_val // 2, color_val), (0, y), (self.screen_width, y))

            # Draw decorative circles
            pygame.draw.circle(self.screen, self.LIGHT_BLUE, (100, 100), 50)
            pygame.draw.circle(self.screen, self.LIGHT_BLUE, (self.screen_width - 100, self.screen_height - 100), 50)
            
            # Draw titles
            self.screen.blit(self.title_text, self.title_rect)
            self.screen.blit(self.subtitle_text, self.subtitle_rect)
            self.screen.blit(self.tagline_text, self.tagline_rect)
            
            # Draw buttons with enhanced styling
            self.draw_button(self.start_button, 'Start Game', self.GREEN, self.WHITE)
            self.draw_button(self.quit_button, 'Quit', (200, 100, 100), self.WHITE)
            
            # Draw hints
            hint = self.hint_font.render('Press SPACE or click to start | F to toggle fullscreen', True, (200, 200, 200))
            hint_rect = hint.get_rect(center=(self.screen_width // 2, self.screen_height - 60))
            self.screen.blit(hint, hint_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return 'quit'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        running = False
                    elif self.quit_button.collidepoint(event.pos):
                        running = False
                        return 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        running = False
                    elif event.key == pygame.K_f:
                        self.is_fullscreen = not self.is_fullscreen
                        flag = pygame.FULLSCREEN if self.is_fullscreen else 0
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flag, vsync=1)

            pygame.display.flip()
            clock.tick(60)

        return 'start_game'


class PetSelection:
    def __init__(self, screen_width=1280, screen_height=720, start_fullscreen=False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            flag = pygame.FULLSCREEN if start_fullscreen else 0
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flag, vsync=1)
            pygame.display.set_caption('Choose Your Pet')
            self.display_available = True
            self.is_fullscreen = start_fullscreen

            # Colors
            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.DARK_BLUE = (25, 50, 100)
            self.LIGHT_BLUE = (100, 180, 255)
            self.GOLD = (255, 215, 0)
            self.GREEN = (100, 255, 100)
            self.DARK_GREEN = (20, 100, 50)
            self.ORANGE = (255, 165, 0)
            self.PURPLE = (200, 100, 200)
            self.DARK_GRAY = (50, 50, 50)

            # Fonts
            self.title_font = pygame.font.Font(None, 72)
            self.pet_name_font = pygame.font.Font(None, 44)
            self.desc_font = pygame.font.Font(None, 28)
            self.stats_font = pygame.font.Font(None, 22)
            self.button_font = pygame.font.Font(None, 24)

            self.title_text = self.title_font.render('🐾 Choose Your Pet 🐾', True, self.GOLD)
            self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, 50))

            # Pet data with characteristics
            self.pets = [
                {
                    'name': 'Dog',
                    'emoji': '🐕',
                    'color': (70, 130, 200),
                    'highlight_color': (100, 160, 230),
                    'description': 'Loyal & Energetic',
                    'traits': 'Loves to play, very friendly',
                    'stats': '❤️ Health: High | ⚡ Energy: High | 😊 Happiness: High',
                    'rect': pygame.Rect(50, 150, 250, 380),
                    'key': pygame.K_1,
                    'key_name': '1'
                },
                {
                    'name': 'Cat',
                    'emoji': '🐈',
                    'color': (200, 150, 100),
                    'highlight_color': (230, 180, 130),
                    'description': 'Graceful & Independent',
                    'traits': 'Aloof but affectionate',
                    'stats': '❤️ Health: Medium | ⚡ Energy: Low | 😊 Happiness: Medium',
                    'rect': pygame.Rect(375, 150, 250, 380),
                    'key': pygame.K_2,
                    'key_name': '2'
                },
                {
                    'name': 'Bird',
                    'emoji': '🦜',
                    'color': (255, 150, 50),
                    'highlight_color': (255, 180, 100),
                    'description': 'Colorful & Cheerful',
                    'traits': 'Playful and talkative',
                    'stats': '❤️ Health: Medium | ⚡ Energy: Very High | 😊 Happiness: Very High',
                    'rect': pygame.Rect(700, 150, 250, 380),
                    'key': pygame.K_3,
                    'key_name': '3'
                },
                {
                    'name': 'Robot',
                    'emoji': '🤖',
                    'color': (150, 150, 150),
                    'highlight_color': (200, 200, 200),
                    'description': 'Reliable & Mechanical',
                    'traits': 'Advanced AI companion',
                    'stats': '❤️ Health: Very High | ⚡ Energy: Unlimited | 😊 Happiness: Quirky',
                    'rect': pygame.Rect(1025, 150, 250, 380),
                    'key': pygame.K_4,
                    'key_name': '4'
                },
            ]

            self.hovered_pet = None
            self.animation_timer = 0

        except Exception:
            self.display_available = False

    def draw_pet_card(self, pet_data, is_hovered=False):
        """Draw an enhanced pet selection card"""
        rect = pet_data['rect']
        color = pet_data['highlight_color'] if is_hovered else pet_data['color']
        
        # Card background
        pygame.draw.rect(self.screen, color, rect)
        
        # Border
        border_color = self.GOLD if is_hovered else self.WHITE
        border_width = 4 if is_hovered else 2
        pygame.draw.rect(self.screen, border_color, rect, border_width)
        
        # Pet emoji/icon
        emoji_text = pygame.font.Font(None, 100).render(pet_data['emoji'], True, self.WHITE)
        emoji_rect = emoji_text.get_rect(center=(rect.centerx, rect.y + 60))
        self.screen.blit(emoji_text, emoji_rect)
        
        # Pet name
        name_text = self.pet_name_font.render(pet_data['name'], True, self.BLACK)
        name_rect = name_text.get_rect(center=(rect.centerx, rect.y + 150))
        self.screen.blit(name_text, name_rect)
        
        # Description
        desc_text = self.desc_font.render(pet_data['description'], True, self.DARK_GRAY)
        desc_rect = desc_text.get_rect(center=(rect.centerx, rect.y + 200))
        self.screen.blit(desc_text, desc_rect)
        
        # Traits
        traits_text = self.stats_font.render(pet_data['traits'], True, self.DARK_GRAY)
        traits_rect = traits_text.get_rect(center=(rect.centerx, rect.y + 240))
        self.screen.blit(traits_text, traits_rect)
        
        # Stats
        stats_text = self.stats_font.render(pet_data['stats'], True, self.DARK_GRAY)
        stats_rect = stats_text.get_rect(center=(rect.centerx, rect.y + 300))
        self.screen.blit(stats_text, stats_rect)
        
        # Keyboard hint
        key_hint = self.button_font.render(f"Press {pet_data['key_name']}", True, self.WHITE)
        key_hint_rect = key_hint.get_rect(center=(rect.centerx, rect.y + 350))
        self.screen.blit(key_hint, key_hint_rect)
        
        # Hover animation - add frame border pulse
        if is_hovered:
            pulse = abs(self.animation_timer % 20 - 10) / 5.0
            pygame.draw.rect(self.screen, self.GOLD, rect, int(border_width + pulse))

    def run(self):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, defaulting to Dog.')
            return 'Dog'
        clock = pygame.time.Clock()
        pygame.event.clear()
        start_time = pygame.time.get_ticks()
        running = True
        selected_pet = None
        
        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 15000:
                selected_pet = 'Dog'
                running = False
                break

            # Get mouse position for hover detection
            mouse_pos = pygame.mouse.get_pos()
            self.hovered_pet = None
            
            for pet_data in self.pets:
                if pet_data['rect'].collidepoint(mouse_pos):
                    self.hovered_pet = pet_data['name']
                    break

            # Draw background
            self.screen.fill(self.DARK_BLUE)
            
            # Draw gradient-like background
            for i in range(self.screen_height):
                color_ratio = i / self.screen_height
                r = int(25 + (100 - 25) * color_ratio)
                g = int(50 + (180 - 50) * color_ratio)
                b = int(100 + (255 - 100) * color_ratio)
                pygame.draw.line(self.screen, (r, g, b), (0, i), (self.screen_width, i))
            
            # Draw title
            self.screen.blit(self.title_text, self.title_rect)
            
            # Instructions
            instr_text = self.desc_font.render('Click a pet or press 1-4 • F for fullscreen', True, self.LIGHT_BLUE)
            instr_rect = instr_text.get_rect(center=(self.screen_width // 2, self.screen_height - 50))
            self.screen.blit(instr_text, instr_rect)

            # Draw pet cards
            for pet_data in self.pets:
                is_hovered = self.hovered_pet == pet_data['name']
                self.draw_pet_card(pet_data, is_hovered)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for pet_data in self.pets:
                        if pet_data['rect'].collidepoint(event.pos):
                            selected_pet = pet_data['name']
                            running = False
                            break
                elif event.type == pygame.KEYDOWN:
                    for pet_data in self.pets:
                        if event.key == pet_data['key']:
                            selected_pet = pet_data['name']
                            running = False
                            break
                    if event.key == pygame.K_f:
                        self.is_fullscreen = not self.is_fullscreen
                        flag = pygame.FULLSCREEN if self.is_fullscreen else 0
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flag, vsync=1)

            self.animation_timer += 1
            pygame.display.flip()
            clock.tick(60)

        return selected_pet


class PetNamingScreen:
    def __init__(self, screen_width=1280, screen_height=720, pet_type='Dog', start_fullscreen=False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pet_type = pet_type
        try:
            flag = pygame.FULLSCREEN if start_fullscreen else 0
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flag, vsync=1)
            pygame.display.set_caption('Name Your Pet')
            self.display_available = True
            self.is_fullscreen = start_fullscreen

            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.BLUE = (0, 0, 255)
            self.GREEN = (0, 255, 0)
            self.YELLOW = (255, 255, 0)
            self.LIGHT_BLUE = (173, 216, 230)
            
            self.title_font = pygame.font.Font(None, 60)
            self.text_font = pygame.font.Font(None, 40)
            self.button_font = pygame.font.Font(None, 32)
            
            self.pet_name = ""
            self.cursor_visible = True
            self.cursor_timer = 0
            
        except Exception:
            self.display_available = False

    def draw_button(self, rect, text, color):
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, self.WHITE, rect, 3)
        text_surf = self.button_font.render(text, True, self.BLACK)
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def draw_input_box(self):
        """Draw the text input box with decorative border"""
        box_width = 300
        box_height = 60
        box_x = self.screen_width // 2 - box_width // 2
        box_y = self.screen_height // 2 - 30
        
        # Outer decorative box
        pygame.draw.rect(self.screen, self.LIGHT_BLUE, (box_x - 10, box_y - 10, box_width + 20, box_height + 20))
        
        # Inner input box
        pygame.draw.rect(self.screen, self.WHITE, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(self.screen, self.YELLOW, (box_x, box_y, box_width, box_height), 3)
        
        # Render text
        display_text = self.pet_name
        if self.cursor_visible:
            display_text += "|"
        
        text_surf = self.text_font.render(display_text, True, self.BLACK)
        text_rect = text_surf.get_rect(center=(self.screen_width // 2, box_y + box_height // 2))
        self.screen.blit(text_surf, text_rect)

    def run(self):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, using default name.')
            return 'Pet'
        
        clock = pygame.time.Clock()
        pygame.event.clear()  # Clear input buffer
        start_time = pygame.time.get_ticks()
        running = True
        
        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 30000:  # 30 seconds timeout
                running = False
                if not self.pet_name:
                    self.pet_name = 'Pet'

            # Update cursor blink
            self.cursor_timer += 1
            if self.cursor_timer > 30:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0

            self.screen.fill((50, 100, 150))
            
            # Title
            title = self.title_font.render('Name Your Pet', True, self.WHITE)
            title_rect = title.get_rect(center=(self.screen_width // 2, 80))
            self.screen.blit(title, title_rect)
            
            # Subtitle with pet type
            subtitle_font = pygame.font.Font(None, 36)
            subtitle = subtitle_font.render(f'Your {self.pet_type}', True, self.YELLOW)
            subtitle_rect = subtitle.get_rect(center=(self.screen_width // 2, 150))
            self.screen.blit(subtitle, subtitle_rect)
            
            # Draw input box
            self.draw_input_box()
            
            # Instructions
            hint_font = pygame.font.Font(None, 24)
            hint = hint_font.render('Type a name (1-20 characters)', True, self.WHITE)
            hint_rect = hint.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 80))
            self.screen.blit(hint, hint_rect)
            
            # Buttons
            confirm_button = pygame.Rect(self.screen_width // 2 - 200, self.screen_height - 120, 150, 50)
            skip_button = pygame.Rect(self.screen_width // 2 + 50, self.screen_height - 120, 150, 50)
            
            self.draw_button(confirm_button, 'Confirm', self.GREEN)
            self.draw_button(skip_button, 'Skip', self.BLUE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if confirm_button.collidepoint(event.pos) and self.pet_name:
                        running = False
                    elif skip_button.collidepoint(event.pos):
                        if not self.pet_name:
                            self.pet_name = 'Pet'
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.is_fullscreen = not self.is_fullscreen
                        flag = pygame.FULLSCREEN if self.is_fullscreen else 0
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flag, vsync=1)
                    elif event.key == pygame.K_RETURN:
                        if self.pet_name:
                            running = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.pet_name = self.pet_name[:-1]
                    elif event.unicode.isalnum() or event.unicode == ' ':
                        if len(self.pet_name) < 20:
                            self.pet_name += event.unicode

            pygame.display.flip()
            clock.tick(60)

        return self.pet_name if self.pet_name else 'Pet'

class ShopScreen:
    """Visual shop interface for purchasing pet items"""
    def __init__(self, screen_width=1000, screen_height=700, pet_shop=None, screen=None):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pet_shop = pet_shop
        try:
            # Use provided screen or get current surface
            if screen is not None:
                self.screen = screen
                self.screen_width = screen.get_width()
                self.screen_height = screen.get_height()
            else:
                self.screen = pygame.display.get_surface()
                if self.screen is None:
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), vsync=1)
            
            pygame.display.set_caption("Pet Shop")
            self.display_available = True
            self.is_fullscreen = False

            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.DARK_GRAY = (50, 50, 50)
            self.LIGHT_GRAY = (200, 200, 200)
            self.GOLD = (255, 215, 0)
            self.GREEN = (100, 200, 100)
            self.RED = (200, 100, 100)
            
            self.title_font = pygame.font.Font(None, 50)
            self.item_font = pygame.font.Font(None, 28)
            self.button_font = pygame.font.Font(None, 24)
            
            self.player_currency = 1000
            self.selected_item = 0
            self.scroll_offset = 0
            self.items_per_page = 3
            
        except Exception:
            self.display_available = False

    def draw_item_card(self, item, x, y, width, height, item_num):
        """Draw a visual item card"""
        # Card background
        pygame.draw.rect(self.screen, self.DARK_GRAY, (x, y, width, height))
        pygame.draw.rect(self.screen, self.GOLD, (x, y, width, height), 3)
        
        # Item type icon
        icon_data = {
            'food': '🍖',
            'toy': '🎾',
            'bed': '🛏️'
        }
        icon_text = self.item_font.render(icon_data.get(item.item_type, '?'), True, self.GOLD)
        self.screen.blit(icon_text, (x + 15, y + 15))
        
        # Item name
        name_text = self.item_font.render(item.name, True, self.WHITE)
        self.screen.blit(name_text, (x + 60, y + 15))
        
        # Description
        desc_font = pygame.font.Font(None, 18)
        desc_text = desc_font.render(item.description[:40], True, self.LIGHT_GRAY)
        self.screen.blit(desc_text, (x + 15, y + 50))
        
        # Cost
        cost_text = self.button_font.render(f"${item.cost}", True, self.GOLD)
        self.screen.blit(cost_text, (x + 15, y + 80))
        
        # Owned count
        owned_text = self.button_font.render(f"Owned: {item.owned}", True, self.GREEN)
        self.screen.blit(owned_text, (x + width - 200, y + 80))
        
        # Multiplier
        mult = item.get_total_multiplier()
        mult_color = self.GREEN if mult > 1 else self.LIGHT_GRAY
        mult_text = self.button_font.render(f"Multiplier: {mult:.2f}x", True, mult_color)
        self.screen.blit(mult_text, (x + 15, y + height - 35))
        
        # Highlight selection
        if self.selected_item == item_num:
            pygame.draw.rect(self.screen, self.GOLD, (x, y, width, height), 5)
        
        # Buy button
        buy_button = pygame.Rect(x + width - 120, y + height - 50, 100, 40)
        button_color = self.GREEN if self.player_currency >= item.cost else self.RED
        pygame.draw.rect(self.screen, button_color, buy_button)
        pygame.draw.rect(self.screen, self.WHITE, buy_button, 2)
        buy_text = self.button_font.render("Buy", True, self.BLACK)
        self.screen.blit(buy_text, buy_text.get_rect(center=buy_button.center))
        
        return buy_button

    def run(self, on_purchase=None):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, skipping shop.')
            return

        if not self.pet_shop:
            print('No shop data available.')
            return

        clock = pygame.time.Clock()
        running = True
        buy_buttons = []
        
        while running:
            self.screen.fill(self.BLACK)
            
            # Header
            pygame.draw.rect(self.screen, (50, 100, 150), (0, 0, self.screen_width, 100))
            title = self.title_font.render("🐾 Pet Shop 🐾", True, self.WHITE)
            title_rect = title.get_rect(center=(self.screen_width // 2, 35))
            self.screen.blit(title, title_rect)
            
            # Currency display
            currency_text = self.button_font.render(f"💰 Currency: ${self.player_currency}", True, self.GOLD)
            self.screen.blit(currency_text, (20, 62))
            
            # Page info
            total_pages = max(1, (len(self.pet_shop.items) + self.items_per_page - 1) // self.items_per_page)
            current_page = (self.pet_shop.current_page if self.pet_shop else 0) + 1
            page_text = self.button_font.render(f"Page {current_page}/{total_pages}", True, self.LIGHT_GRAY)
            self.screen.blit(page_text, (self.screen_width - 300, 62))
            
            # Draw items
            if self.pet_shop:
                page_items = self.pet_shop.get_page_items()
                buy_buttons = []
                
                for idx, key in enumerate(page_items):
                    item = self.pet_shop.items[key]
                    x = 40
                    y = 120 + idx * 160
                    width = self.screen_width - 80
                    height = 140
                    
                    buy_btn = self.draw_item_card(item, x, y, width, height, idx)
                    buy_buttons.append((buy_btn, key, item))
            
            # Navigation buttons
            nav_y = self.screen_height - 80
            prev_button = pygame.Rect(40, nav_y, 100, 50)
            next_button = pygame.Rect(self.screen_width - 140, nav_y, 100, 50)
            quit_button = pygame.Rect(self.screen_width // 2 - 75, nav_y, 150, 50)
            
            # Draw navigation buttons
            for btn, label in [(prev_button, "<Prev"), (next_button, "Next>"), (quit_button, "Exit Shop")]:
                btn_color = self.GOLD if label != "Exit Shop" else self.RED
                pygame.draw.rect(self.screen, btn_color, btn)
                pygame.draw.rect(self.screen, self.WHITE, btn, 2)
                text = self.button_font.render(label, True, self.BLACK)
                self.screen.blit(text, text.get_rect(center=btn.center))
            
            # Fullscreen hint
            fs_hint = pygame.font.Font(None, 18).render("Press F for fullscreen", True, self.LIGHT_GRAY)
            self.screen.blit(fs_hint, (self.screen_width - 220, 5))
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(event.pos):
                        running = False
                    elif prev_button.collidepoint(event.pos):
                        if self.pet_shop:
                            self.pet_shop.prev_page()
                    elif next_button.collidepoint(event.pos):
                        if self.pet_shop:
                            self.pet_shop.next_page()
                    else:
                        # Check if any buy button was clicked
                        for btn, item_key, item in buy_buttons:
                            if btn.collidepoint(event.pos):
                                if self.player_currency >= item.cost:
                                    self.player_currency -= item.cost
                                    item.owned += 1
                                    if on_purchase:
                                        on_purchase(item_key, item)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT:
                        if self.pet_shop:
                            self.pet_shop.prev_page()
                    elif event.key == pygame.K_RIGHT:
                        if self.pet_shop:
                            self.pet_shop.next_page()
                    elif event.key == pygame.K_f:
                        # Toggle fullscreen
                        self.is_fullscreen = not self.is_fullscreen
                        if self.is_fullscreen:
                            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            
            pygame.display.flip()
            clock.tick(60)


class InteractiveTutorialScreen:
    """Interactive tutorial that requires players to perform actions"""
    def __init__(self, screen, steps_with_requirements):
        self.screen = screen
        self.steps = steps_with_requirements  # List of tuples: (instruction_text, required_action)
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.current_step = 0
        self.completed = False
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 24)

    def is_finished(self):
        return self.current_step >= len(self.steps)

    def check_action(self, action_performed):
        """Check if the performed action matches the current step requirement"""
        if self.is_finished():
            return False
        
        required_action = self.steps[self.current_step][1]
        action_performed = action_performed.lower()
        required_action = required_action.lower()
        
        # Check if the action matches the requirement
        if required_action == 'move':
            # Any movement satisfies the move requirement
            return action_performed == 'move'
        elif required_action == 'feed':
            return action_performed == 'feed'
        elif required_action == 'play':
            return action_performed == 'play'
        elif required_action == 'rest':
            # Both rest and clean satisfy the rest requirement
            return action_performed in ['rest', 'clean']
        elif required_action == 'shop':
            return action_performed == 'shop'
        elif required_action == 'minigame':
            return action_performed == 'minigame'
        elif action_performed == required_action:
            return True
        
        return False

    def advance_step(self):
        """Move to the next tutorial step"""
        if not self.is_finished():
            self.current_step += 1

    def draw_overlay(self):
        """Draw the tutorial overlay on top of the game"""
        if self.is_finished():
            return

        instruction_text, _ = self.steps[self.current_step]
        
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, 120), pygame.SRCALPHA)
        overlay.fill((10, 10, 10, 200))
        self.screen.blit(overlay, (0, 0))

        # Title
        title = self.title_font.render('📚 Tutorial', True, (255, 215, 0))
        self.screen.blit(title, (20, 10))

        # Instruction
        instruction_render = self.font.render(instruction_text, True, (230, 230, 230))
        self.screen.blit(instruction_render, (20, 55))

        # Progress
        progress = self.small_font.render(
            f'Step {self.current_step + 1} of {len(self.steps)} - Perform the action to continue!',
            True,
            (200, 200, 200)
        )
        self.screen.blit(progress, (self.width - 420, 10))

        # Completion overlay
        if self.is_finished():
            completion = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            completion.fill((10, 10, 10, 180))
            self.screen.blit(completion, (0, 0))
            
            complete_text = self.title_font.render('Tutorial Complete!', True, (100, 255, 100))
            self.screen.blit(complete_text, complete_text.get_rect(center=(self.width // 2, self.height // 2 - 40)))
            
            hint = self.font.render('Press any key to continue...', True, (200, 200, 200))
            self.screen.blit(hint, hint.get_rect(center=(self.width // 2, self.height // 2 + 40)))


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
    def __init__(self, screen, pet_name, pet_type, animations, tutorial=None):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.animations = animations
        self.tutorial = tutorial
        self.pet_x = 200
        self.pet_y = 300
        self.speed = 4
        self.direction = 'right'
        self.walking = False
        self.frame_timer = 0
        self.current_frame = 0
        self.message = 'Use arrow keys to move. Press E to interact. Press F for fullscreen.'
        self.font = pygame.font.Font(None, 28)
        self.small_font = pygame.font.Font(None, 20)
        self.title_font = pygame.font.Font(None, 40)
        self.reaction_animator = ReactionAnimator()
        self.animation_timer = 0
        self.is_fullscreen = False

        # Interactive areas with better positioning and names
        self.action_spots = [
            {'name': 'Feed', 'x': 120, 'y': 450, 'type': 'food_bowl', 'label': 'Food Bowl'},
            {'name': 'Water', 'x': 220, 'y': 450, 'type': 'water_bowl', 'label': 'Water Bowl'},
            {'name': 'Play', 'x': 400, 'y': 380, 'type': 'play', 'label': 'Play Area'},
            {'name': 'Rest', 'x': 600, 'y': 450, 'type': 'bed', 'label': 'Bed'},
            {'name': 'Clean', 'x': 700, 'y': 300, 'type': 'bath', 'label': 'Bath Station'},
            {'name': 'Mini Game', 'x': 100, 'y': 250, 'type': 'minigame', 'label': 'Mini Game'},
            {'name': 'Shop', 'x': 750, 'y': 450, 'type': 'shop', 'label': 'Pet Shop'},
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
            if self.frame_timer > 60 and frames:  # Reduced from 120ms to 60ms for smoother animation
                self.frame_timer = 0
                self.current_frame = (self.current_frame + 1) % len(frames)
        else:
            self.frame_timer = 0
            self.current_frame = 0
        
        self.animation_timer += 1
        self.reaction_animator.update()

    def get_current_spot(self):
        pet_rect = self.get_pet_rect()
        pet_center = (pet_rect.centerx, pet_rect.centery)
        
        # Check distance to each spot
        for spot in self.action_spots:
            dist_x = pet_center[0] - spot['x']
            dist_y = pet_center[1] - spot['y']
            distance = (dist_x**2 + dist_y**2) ** 0.5
            if distance < 80:  # Interaction radius
                return spot
        return None

    def draw_action_spot(self, spot):
        """Draw interactive area with appropriate visual representation"""
        spot_type = spot['type']
        x, y = spot['x'], spot['y']
        
        if spot_type == 'food_bowl':
            visual_reactions.draw_bowl(self.screen, x, y, 'food', 0.6)
        elif spot_type == 'water_bowl':
            visual_reactions.draw_bowl(self.screen, x, y, 'water', 0.8)
        elif spot_type == 'play':
            visual_reactions.draw_play_area(self.screen, x, y, self.animation_timer)
        elif spot_type == 'bed':
            visual_reactions.draw_bed(self.screen, x, y, 0.5)
        elif spot_type == 'bath':
            visual_reactions.draw_bath_station(self.screen, x, y, 0.7)
        elif spot_type == 'minigame':
            visual_reactions.draw_minigame_screen(self.screen, x, y, "Mini Game")
        
        # Draw label
        label = self.small_font.render(spot['label'], True, (255, 255, 255))
        label_rect = label.get_rect(center=(x, y + 50))
        
        # Draw label background for visibility
        bg_rect = label_rect.inflate(10, 6)
        pygame.draw.rect(self.screen, (0, 0, 0), bg_rect)
        pygame.draw.rect(self.screen, (100, 100, 100), bg_rect, 1)
        self.screen.blit(label, label_rect)

    def draw(self):
        # Background
        self.screen.fill((90, 180, 210))
        
        # Ground
        pygame.draw.rect(self.screen, (100, 180, 100), (0, self.height - 160, self.width, 160))
        
        # Top header
        pygame.draw.rect(self.screen, (70, 130, 180), (0, 0, self.width, 100))

        # Title and pet name
        title = self.title_font.render(f"{self.pet_name}'s Home", True, (255, 255, 255))
        self.screen.blit(title, (28, 15))
        
        # Instructions
        hint = self.small_font.render('Move with arrow keys • Press E to interact', True, (240, 240, 240))
        self.screen.blit(hint, (28, 65))

        # Draw all interactive areas
        for spot in self.action_spots:
            self.draw_action_spot(spot)

        # Draw pet with visual reactions overlay
        pet_sprite = self.get_current_sprite()
        self.screen.blit(pet_sprite, (self.pet_x, self.pet_y))
        
        # Draw reactions
        self.reaction_animator.draw(self.screen, self.pet_x, self.pet_y, 64, 64)

        # Draw interaction prompt
        spot = self.get_current_spot()
        if spot:
            prompt = self.font.render(f"Press E to {spot['name']}", True, (255, 255, 200))
            prompt_rect = prompt.get_rect(center=(self.width // 2, self.height - 40))
            
            # Highlight box
            highlight = prompt_rect.inflate(20, 10)
            pygame.draw.rect(self.screen, (0, 0, 0), highlight)
            pygame.draw.rect(self.screen, (255, 255, 100), highlight, 2)
            self.screen.blit(prompt, prompt_rect)

        # Draw current message
        if self.message and self.message != 'Use arrow keys to move. Press E to interact.':
            msg = self.small_font.render(self.message, True, (255, 200, 100))
            self.screen.blit(msg, (28, self.height - 90))

    def run(self, on_action):
        clock = pygame.time.Clock()
        pygame.event.clear()  # Clear input buffer to prevent stale inputs
        running = True
        tutorial_waiting = False
        # Reset pet to starting position
        self.pet_x = 200
        self.pet_y = 300
        self.walking = False
        self.current_frame = 0
        prev_x, prev_y = self.pet_x, self.pet_y
        
        while running:
            dt = clock.tick(60)
            
            # Check for completion screen in tutorial
            if self.tutorial and self.tutorial.is_finished() and tutorial_waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        tutorial_waiting = False
                self.draw()
                self.tutorial.draw_overlay()
                pygame.display.flip()
                continue
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_f:
                        # Toggle fullscreen
                        self.is_fullscreen = not self.is_fullscreen
                        if self.is_fullscreen:
                            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN, vsync=1)
                            self.message = "Fullscreen ON (Press F to exit)"
                        else:
                            self.screen = pygame.display.set_mode((self.width, self.height), vsync=1)
                            self.message = "Fullscreen OFF"
                    elif event.key == pygame.K_e:
                        spot = self.get_current_spot()
                        if spot:
                            # Determine which reaction to show based on action
                            if spot['name'] == 'Feed':
                                self.reaction_animator.add_reaction(ReactionType.EATING, 40)
                            elif spot['name'] == 'Play':
                                self.reaction_animator.add_reaction(ReactionType.PLAYING, 40)
                            elif spot['name'] == 'Rest':
                                self.reaction_animator.add_reaction(ReactionType.TIRED, 40)
                            elif spot['name'] == 'Clean':
                                self.reaction_animator.add_reaction(ReactionType.HEALTHY, 40)
                            else:
                                self.reaction_animator.add_reaction(ReactionType.HAPPY, 40)
                            
                            result = on_action(spot['name'])
                            self.message = result or self.message
                            
                            # Check tutorial action requirement
                            if self.tutorial and not self.tutorial.is_finished():
                                action_name = spot['name'].lower() if spot['name'] != 'Mini Game' else 'minigame'
                                if self.tutorial.check_action(action_name):
                                    self.tutorial.advance_step()
                                    
            self.handle_input()
            self.update(dt)
            
            # Check for movement in tutorial
            if self.tutorial and not self.tutorial.is_finished():
                if (self.pet_x != prev_x or self.pet_y != prev_y) and self.walking:
                    if self.tutorial.check_action('move'):
                        self.tutorial.advance_step()
                prev_x, prev_y = self.pet_x, self.pet_y
            
            self.draw()
            
            # Draw tutorial overlay
            if self.tutorial:
                self.tutorial.draw_overlay()
                if self.tutorial.is_finished() and not tutorial_waiting:
                    tutorial_waiting = True
            
            pygame.display.flip()
        return


class MinigameSelectionScreen:
    """Visual minigame selection screen"""
    def __init__(self, screen_width=900, screen_height=700, screen=None):
        self.screen_width = screen_width
        self.screen_height = screen_height
        try:
            # Use provided screen or get current surface
            if screen is not None:
                self.screen = screen
                self.screen_width = screen.get_width()
                self.screen_height = screen.get_height()
            else:
                self.screen = pygame.display.get_surface()
                if self.screen is None:
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), vsync=1)
            
            pygame.display.set_caption("Choose a Minigame")
            self.display_available = True
            self.is_fullscreen = False

            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)
            self.DARK_BLUE = (30, 60, 150)
            self.LIGHT_BLUE = (100, 150, 255)
            self.GOLD = (255, 215, 0)
            self.GREEN = (100, 200, 100)
            
            self.title_font = pygame.font.Font(None, 56)
            self.game_font = pygame.font.Font(None, 36)
            self.desc_font = pygame.font.Font(None, 24)
            
            # Define minigames
            self.minigames = [
                {
                    'name': 'Treat Catch',
                    'icon': '🎾',
                    'description': 'Catch falling treats in a basket!',
                    'reward': '⭐ Increase Hunger',
                    'difficulty': 'Medium'
                },
                {
                    'name': 'Trick Time',
                    'icon': '✨',
                    'description': 'Test your reflexes!',
                    'reward': '💚 Increase Happiness',
                    'difficulty': 'Easy'
                },
                {
                    'name': 'Medicine Rush',
                    'icon': '💊',
                    'description': 'Administer medicine quickly!',
                    'reward': '🏥 Increase Health',
                    'difficulty': 'Hard'
                },
            ]
            
            self.selected_game = 0
            
        except Exception:
            self.display_available = False

    def draw_game_card(self, game, x, y, width, height, is_selected):
        """Draw a minigame selection card"""
        # Card background
        bg_color = self.LIGHT_BLUE if is_selected else self.DARK_BLUE
        pygame.draw.rect(self.screen, bg_color, (x, y, width, height))
        
        # Border
        border_color = self.GOLD if is_selected else self.WHITE
        border_width = 4 if is_selected else 2
        pygame.draw.rect(self.screen, border_color, (x, y, width, height), border_width)
        
        # Game icon
        icon_text = self.game_font.render(game['icon'], True, self.GOLD)
        icon_rect = icon_text.get_rect(center=(x + width // 2, y + 40))
        self.screen.blit(icon_text, icon_rect)
        
        # Game name
        name_text = self.game_font.render(game['name'], True, self.WHITE)
        name_rect = name_text.get_rect(center=(x + width // 2, y + 90))
        self.screen.blit(name_text, name_rect)
        
        # Description
        desc_text = self.desc_font.render(game['description'], True, (200, 200, 255))
        desc_rect = desc_text.get_rect(center=(x + width // 2, y + 130))
        self.screen.blit(desc_text, desc_rect)
        
        # Reward info
        reward_surf = self.desc_font.render(game['reward'], True, self.GREEN)
        reward_rect = reward_surf.get_rect(center=(x + width // 2, y + 170))
        self.screen.blit(reward_surf, reward_rect)
        
        # Difficulty
        diff_color = {
            'Easy': (100, 255, 100),
            'Medium': (255, 255, 100),
            'Hard': (255, 100, 100)
        }.get(game['difficulty'], (150, 150, 150))
        
        diff_text = self.desc_font.render(f"Difficulty: {game['difficulty']}", True, diff_color)
        diff_rect = diff_text.get_rect(center=(x + width // 2, y + height - 30))
        self.screen.blit(diff_text, diff_rect)

    def run(self):
        if not hasattr(self, 'display_available') or not self.display_available:
            print('No display available, defaulting to first game.')
            return 'minigame_hunger'

        clock = pygame.time.Clock()
        running = True
        selected = None
        
        while running:
            self.screen.fill(self.BLACK)
            
            # Header
            pygame.draw.rect(self.screen, (50, 100, 200), (0, 0, self.screen_width, 100))
            title = self.title_font.render("🎮 Choose Your Game", True, self.WHITE)
            title_rect = title.get_rect(center=(self.screen_width // 2, 40))
            self.screen.blit(title, title_rect)
            
            # Draw game cards
            card_width = 250
            card_height = 220
            spacing = 30
            total_width = len(self.minigames) * card_width + (len(self.minigames) - 1) * spacing
            start_x = (self.screen_width - total_width) // 2
            
            card_rects = []
            for idx, game in enumerate(self.minigames):
                x = start_x + idx * (card_width + spacing)
                y = 150
                self.draw_game_card(game, x, y, card_width, card_height, idx == self.selected_game)
                card_rects.append(pygame.Rect(x, y, card_width, card_height))
            
            # Instructions
            hint = self.desc_font.render("Use arrow keys to select • Press ENTER to play • ESC to cancel • F for fullscreen", True, (200, 200, 200))
            hint_rect = hint.get_rect(center=(self.screen_width // 2, self.screen_height - 80))
            self.screen.blit(hint, hint_rect)
            
            # Play button hint
            if self.selected_game < len(self.minigames):
                play_hint = self.game_font.render("► PLAY", True, self.GOLD)
                play_rect = play_hint.get_rect(center=(self.screen_width // 2, self.screen_height - 30))
                self.screen.blit(play_hint, play_rect)
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.selected_game = (self.selected_game - 1) % len(self.minigames)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_game = (self.selected_game + 1) % len(self.minigames)
                    elif event.key == pygame.K_RETURN:
                        # Map game selection to minigame functions
                        game_map = {
                            0: 'minigame_hunger',
                            1: 'minigame_happiness',
                            2: 'minigame_health'
                        }
                        selected = game_map.get(self.selected_game, 'minigame_hunger')
                        running = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_f:
                        # Toggle fullscreen
                        self.is_fullscreen = not self.is_fullscreen
                        if self.is_fullscreen:
                            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for idx, rect in enumerate(card_rects):
                        if rect.collidepoint(event.pos):
                            self.selected_game = idx
                            game_map = {
                                0: 'minigame_hunger',
                                1: 'minigame_happiness',
                                2: 'minigame_health'
                            }
                            selected = game_map.get(self.selected_game, 'minigame_hunger')
                            running = False
                            break
            
            pygame.display.flip()
            clock.tick(60)
        
        return selected if selected else 'minigame_hunger'



    title = TitleScreen()
    result = title.run()
    print(result)
