import random
import pygame
from settings import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, RED

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()
        
    def spawn(self):
        # Generate a random starting position
        self.position = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )
    
    def draw(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, RED, rect)