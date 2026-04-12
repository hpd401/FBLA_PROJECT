"""Visual reactions and animations for pet care actions"""
import pygame
from enum import Enum


class ReactionType(Enum):
    HAPPY = 1
    EATING = 2
    TIRED = 3
    HEALTHY = 4
    PLAYING = 5
    RESTING = 6


def draw_reaction_animation(surface, reaction_type, center_x, center_y, animation_frame):
    """Draw visual reaction above the pet based on action type"""
    font_small = pygame.font.Font(None, 24)
    font_medium = pygame.font.Font(None, 32)
    
    # Calculate particle positions
    particles = []
    
    if reaction_type == ReactionType.HAPPY:
        # Happy hearts floating up
        for i in range(3):
            offset = (i - 1) * 15
            y_pos = center_y - 40 - (animation_frame * 2)
            particles.append(draw_heart(surface, center_x + offset, y_pos, 255 - animation_frame * 10))
    
    elif reaction_type == ReactionType.EATING:
        # Floating food particles
        for i in range(2):
            offset = (i - 0.5) * 10
            y_pos = center_y - 20 - (animation_frame * 1.5)
            draw_food_particle(surface, center_x + offset, y_pos, animation_frame)
    
    elif reaction_type == ReactionType.TIRED:
        # Z's for sleeping
        offset = -15 if animation_frame % 2 == 0 else 0
        text = font_medium.render("Z", True, (150, 150, 255))
        alpha = max(0, 255 - animation_frame * 20)
        text.set_alpha(alpha)
        y_pos = center_y - 50 - (animation_frame * 1)
        surface.blit(text, (center_x + offset, y_pos))
    
    elif reaction_type == ReactionType.HEALTHY:
        # Medical cross
        draw_health_cross(surface, center_x, center_y - 40, animation_frame)
    
    elif reaction_type == ReactionType.PLAYING:
        # Exclamation marks bouncing
        for i in range(2):
            offset = (i - 0.5) * 12
            bounce = 10 * abs((animation_frame % 20) - 10) / 10
            y_pos = center_y - 50 + bounce
            text = font_medium.render("!", True, (255, 200, 0))
            surface.blit(text, (center_x + offset, y_pos))


def draw_heart(surface, x, y, alpha_val):
    """Draw a heart shape"""
    color = (255, 100, 150)
    heart_points = [
        (x - 4, y - 2), (x - 2, y - 4), (x + 2, y - 4), (x + 4, y - 2),
        (x + 4, y), (x, y + 4), (x - 4, y)
    ]
    pygame.draw.polygon(surface, color, heart_points)


def draw_food_particle(surface, x, y, animation_frame):
    """Draw floating food particles"""
    colors = [(255, 165, 0), (255, 140, 0)]
    color = colors[animation_frame % 2]
    pygame.draw.circle(surface, color, (int(x), int(y)), 3)


def draw_health_cross(surface, x, y, animation_frame):
    """Draw a health/medical cross"""
    color = (0, 200, 100)
    size = 8
    # Vertical line
    pygame.draw.line(surface, color, (x, y - size), (x, y + size), 2)
    # Horizontal line
    pygame.draw.line(surface, color, (x - size, y), (x + size, y), 2)


class ReactionAnimator:
    """Handles continuous reaction animations"""
    def __init__(self):
        self.reactions = []  # List of (reaction_type, start_frame, duration, x, y)
        self.current_frame = 0
    
    def add_reaction(self, reaction_type, duration=30):
        """Add a new reaction animation"""
        self.reactions.append({
            'type': reaction_type,
            'start_frame': self.current_frame,
            'duration': duration,
            'frame': 0
        })
    
    def update(self):
        """Update all active reactions"""
        self.current_frame += 1
        self.reactions = [r for r in self.reactions if r['frame'] < r['duration']]
        for reaction in self.reactions:
            reaction['frame'] += 1
    
    def draw(self, surface, pet_x, pet_y, pet_width, pet_height):
        """Draw all active reactions"""
        for reaction in self.reactions:
            center_x = pet_x + pet_width // 2
            center_y = pet_y - 10
            draw_reaction_animation(surface, reaction['type'], center_x, center_y, reaction['frame'])


def draw_bowl(surface, x, y, bowl_type='food', fill_level=0.7):
    """Draw a food or water bowl"""
    # Bowl outline
    pygame.draw.ellipse(surface, (100, 100, 100), (x - 30, y - 15, 60, 20))
    
    # Bowl side
    pygame.draw.line(surface, (80, 80, 80), (x - 30, y - 15), (x - 25, y - 10), 3)
    pygame.draw.line(surface, (80, 80, 80), (x + 30, y - 15), (x + 25, y - 10), 3)
    
    if bowl_type == 'food':
        # Food fill
        food_color = (200, 140, 70)
        fill_height = int(20 * fill_level)
        pygame.draw.ellipse(surface, food_color, (x - 25, y - 10 - fill_height, 50, fill_height))
    elif bowl_type == 'water':
        # Water fill
        water_color = (100, 180, 255)
        fill_height = int(20 * fill_level)
        pygame.draw.ellipse(surface, water_color, (x - 25, y - 10 - fill_height, 50, fill_height))
    
    # Shine on bowl
    pygame.draw.ellipse(surface, (180, 180, 180), (x - 20, y - 12, 15, 5))


def draw_play_area(surface, x, y, animation_frame):
    """Draw a play area with toys"""
    # Base area
    pygame.draw.rect(surface, (220, 200, 150), (x - 50, y - 30, 100, 60))
    pygame.draw.rect(surface, (180, 160, 100), (x - 50, y - 30, 100, 60), 3)
    
    # Toys bouncing
    toy_colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
    for i in range(4):
        toy_x = x - 35 + (i * 22)
        bounce = 10 * abs((animation_frame + i * 5) % 20 - 10) / 10
        toy_y = y - 15 + bounce
        pygame.draw.circle(surface, toy_colors[i], (int(toy_x), int(toy_y)), 5)


def draw_bed(surface, x, y, sleep_level=0.5):
    """Draw a pet bed"""
    # Mattress
    bed_color = (150, 100, 200)
    pygame.draw.rect(surface, bed_color, (x - 40, y - 10, 80, 40))
    pygame.draw.rect(surface, (100, 50, 150), (x - 40, y - 10, 80, 40), 2)
    
    # Pillow
    pillow_color = (200, 180, 220)
    pygame.draw.rect(surface, pillow_color, (x - 35, y - 20, 20, 12))
    
    # Blanket (if resting)
    if sleep_level > 0.3:
        blanket_color = (200, 100, 100)
        pygame.draw.polygon(surface, blanket_color, [
            (x + 20, y + 10), (x + 30, y), (x + 30, y + 20)
        ])


def draw_bath_station(surface, x, y, water_level=0.5):
    """Draw a bath/washing station"""
    # Tub
    pygame.draw.rect(surface, (180, 180, 180), (x - 35, y - 15, 70, 40))
    pygame.draw.rect(surface, (100, 100, 100), (x - 35, y - 15, 70, 40), 2)
    
    # Water
    water_color = (100, 180, 255)
    water_height = int(30 * water_level)
    pygame.draw.rect(surface, water_color, (x - 30, y - 10 + (30 - water_height), 60, water_height))
    
    # Shower head
    pygame.draw.circle(surface, (150, 150, 150), (x, y - 25), 8)
    # Water drops
    for i in range(3):
        drop_x = x - 6 + (i * 6)
        drop_y = y - 17 + i % 2 * 2
        pygame.draw.line(surface, (100, 150, 255), (drop_x, drop_y), (drop_x, drop_y + 4), 1)


def draw_minigame_screen(surface, x, y, game_name="Mini Game"):
    """Draw a screen showing minigame selection"""
    # Screen frame
    pygame.draw.rect(surface, (50, 50, 50), (x - 45, y - 35, 90, 70))
    pygame.draw.rect(surface, (150, 150, 150), (x - 45, y - 35, 90, 70), 3)
    
    # Screen display
    pygame.draw.rect(surface, (20, 100, 200), (x - 40, y - 30, 80, 50))
    
    # Text on screen
    font = pygame.font.Font(None, 20)
    text = font.render(game_name[:10], True, (255, 255, 255))
    text_rect = text.get_rect(center=(x, y - 5))
    surface.blit(text, text_rect)
    
    # Button indicators
    pygame.draw.rect(surface, (100, 200, 100), (x - 38, y + 15, 12, 12))
    pygame.draw.rect(surface, (200, 100, 100), (x - 20, y + 15, 12, 12))
    pygame.draw.rect(surface, (200, 200, 100), (x + 10, y + 15, 12, 12))


def draw_pet_name_display(surface, pet_name, x, y):
    """Draw pet name with decorative frame"""
    font_name = pygame.font.Font(None, 36)
    
    # Name box background
    pygame.draw.rect(surface, (200, 150, 100), (x - 80, y - 25, 160, 50))
    pygame.draw.rect(surface, (150, 100, 50), (x - 80, y - 25, 160, 50), 3)
    
    # Decorative corners
    corner_size = 8
    corners = [
        (x - 80, y - 25),
        (x + 80 - corner_size, y - 25),
        (x - 80, y + 25 - corner_size),
        (x + 80 - corner_size, y + 25 - corner_size)
    ]
    for cx, cy in corners:
        pygame.draw.circle(surface, (255, 200, 100), (int(cx), int(cy)), 3)
    
    # Name text
    name_text = font_name.render(pet_name, True, (255, 255, 255))
    name_rect = name_text.get_rect(center=(x, y))
    surface.blit(name_text, name_rect)
