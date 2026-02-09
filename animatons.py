import pygame
import sys

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, pos, fps=10):
        super().__init__()
        self.frames = [f.convert_alpha() for f in frames]
        self.index = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=pos)
        self.frame_time = 1000 / fps     # ms per frame
        self.acc = 0                     # accumulated ms

    def update(self, dt):
        self.acc += dt
        while self.acc >= self.frame_time:
            self.acc -= self.frame_time
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

def load_frames(prefix, count):
    return [pygame.image.load(f"{prefix}{i}.png") for i in range(count)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    frames = load_frames("assets/walk_", 6)  # assets/walk_0.png ... _5.png
    sprite = AnimatedSprite(frames, pos=(320,240), fps=12)
    group = pygame.sprite.Group(sprite)

    while True:
        dt = clock.tick(60)  # milliseconds since last frame
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        group.update(dt)
        screen.fill((30, 30, 30))
        group.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()