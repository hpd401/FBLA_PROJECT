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


def load_pet_animation(pet_type):
    """Load walk/idle animation frames for a pet, or return placeholders if PNGs are not present."""
    pygame.init()
    pet_key = pet_type.lower()
    base_folder = os.path.join('assets', pet_key)
    colors = {
        'dog': (160, 110, 60),
        'cat': (120, 120, 180),
        'bird': (200, 170, 60),
        'robot': (100, 180, 220),
    }
    default_color = colors.get(pet_key, (200, 120, 120))

    idle = load_frames(os.path.join(base_folder, 'idle'))
    walk_right = load_frames(os.path.join(base_folder, 'walk_right'))
    walk_left = load_frames(os.path.join(base_folder, 'walk_left'))

    if not idle:
        idle = load_frames(base_folder)
    if not walk_right:
        walk_right = idle[:]
    if not walk_left:
        walk_left = [pygame.transform.flip(frame, True, False) for frame in walk_right]

    if not idle:
        placeholder = make_placeholder_surface((64, 64), default_color)
        idle = [placeholder]
    if not walk_right:
        walk_right = idle[:]
    if not walk_left:
        walk_left = [pygame.transform.flip(frame, True, False) for frame in walk_right]

    return {
        'idle': idle,
        'walk_right': walk_right,
        'walk_left': walk_left,
    }
