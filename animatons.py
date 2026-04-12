import os
import pygame


def make_placeholder_surface(size, color):
    surface = pygame.Surface(size, pygame.SRCALPHA)
    surface.fill(color)
    return surface


def load_frames(folder):
    if not os.path.isdir(folder):
        return []

    frames = []
    for filename in sorted(os.listdir(folder)):
        if filename.lower().endswith('.png'):
            path = os.path.join(folder, filename)
            try:
                frames.append(pygame.image.load(path).convert_alpha())
            except Exception:
                continue
    return frames


def make_dog_sprite(frame=0, direction='down'):
    """Create an 8-bit style top-down dog sprite"""
    surface = pygame.Surface((64, 64), pygame.SRCALPHA)
    
    # 8-bit colors
    brown = (139, 69, 19)
    light_brown = (160, 110, 60)
    dark_brown = (101, 67, 33)
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    # Pixel size for 8-bit look
    pixel = 4
    
    # Base dog shape (top-down view)
    # Body (oval-ish)
    pygame.draw.rect(surface, brown, (20, 28, 24, 16))
    pygame.draw.rect(surface, brown, (16, 32, 32, 8))
    
    # Head
    pygame.draw.rect(surface, light_brown, (24, 16, 16, 16))
    
    # Ears
    pygame.draw.rect(surface, dark_brown, (20, 12, 8, 8))
    pygame.draw.rect(surface, dark_brown, (36, 12, 8, 8))
    
    # Eyes (directional)
    if direction == 'up':
        pygame.draw.rect(surface, black, (26, 20, 4, 4))
        pygame.draw.rect(surface, black, (34, 20, 4, 4))
    elif direction == 'down':
        pygame.draw.rect(surface, black, (26, 24, 4, 4))
        pygame.draw.rect(surface, black, (34, 24, 4, 4))
    elif direction == 'left':
        pygame.draw.rect(surface, black, (24, 22, 4, 4))
        pygame.draw.rect(surface, black, (32, 22, 4, 4))
    elif direction == 'right':
        pygame.draw.rect(surface, black, (28, 22, 4, 4))
        pygame.draw.rect(surface, black, (36, 22, 4, 4))
    
    # Nose
    pygame.draw.rect(surface, black, (30, 26, 4, 2))
    
    # Legs (4 legs around body)
    leg_offset = (frame % 4) * pixel - 2 * pixel  # Simple animation
    
    # Front legs
    pygame.draw.rect(surface, dark_brown, (22, 40 + leg_offset, 4, 8))
    pygame.draw.rect(surface, dark_brown, (38, 40 - leg_offset, 4, 8))
    
    # Back legs
    pygame.draw.rect(surface, dark_brown, (26, 44 + leg_offset, 4, 8))
    pygame.draw.rect(surface, dark_brown, (34, 44 - leg_offset, 4, 8))
    
    # Tail (wags for animation)
    tail_x = 44
    tail_y = 36
    if frame % 2 == 0:
        pygame.draw.rect(surface, brown, (tail_x, tail_y, 8, 4))
    else:
        pygame.draw.rect(surface, brown, (tail_x + 2, tail_y - 2, 4, 8))
    
    return surface


def load_pet_animation(pet_type):
    """Load walk/idle animation frames for a pet, or return placeholders if PNGs are not present."""
    pygame.init()
    pet_key = pet_type.lower()
    
    if pet_key == 'dog':
        # Create dog animations programmatically for all directions
        idle = [make_dog_sprite(0, 'down')]  # Single idle frame facing down
        
        walk_up = [make_dog_sprite(i, 'up') for i in range(4)]
        walk_down = [make_dog_sprite(i, 'down') for i in range(4)]
        walk_left = [make_dog_sprite(i, 'left') for i in range(4)]
        walk_right = [make_dog_sprite(i, 'right') for i in range(4)]
    else:
        # Leave others blank
        idle = []
        walk_up = []
        walk_down = []
        walk_left = []
        walk_right = []

    return {
        'idle': idle,
        'walk_up': walk_up,
        'walk_down': walk_down,
        'walk_left': walk_left,
        'walk_right': walk_right,
    }
