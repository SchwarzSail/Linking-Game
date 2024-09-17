import pygame

def load_patterns():
    patterns = [pygame.image.load(f"../assets/patterns/pattern_{i}.png") for i in range(1, 7)]
    patterns = [pygame.transform.scale(p, (100, 100)) for p in patterns]
    return patterns