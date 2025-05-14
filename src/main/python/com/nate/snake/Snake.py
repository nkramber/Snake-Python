import pygame
from settings import GRID_SIZE, GREEN, GRID_WIDTH, GRID_HEIGHT

class Snake:
    def __init__(self):
        self.__body = [(5, 5)] # Protected variable indicated by single underscore
        self._direction = (1, 0) # Right by default
        self.__growing = False # Private variable indicated by double underscore
        
    @property
    def head(self):
        return self.__body[0]
    
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, new_direction):
        # Don't allow 180 degree turns
        if (new_direction[0] * -1, new_direction[1] * -1) == self._direction:
            return
        self._direction = new_direction
        
    def grow(self):
        self.__growing = True
        
    def update(self):
        # Calculate new head position
        head_x, head_y = self.__body[0]
        dir_x, dir_y = self._direction
        
        # Wrap around the sides of the screen if we over or under lap
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)
        
        # Add new head
        self.__body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.__growing:
            self.__body.pop()
        # If we were growing, stop now that we've grown
        else:
            self.__growing = False
            
    def check_collision(self):
        # Check if snake collidied with itself
        return self.head in self.__body[1:]
    
    def draw(self, surface):
        for segment in self.__body:
            rect = pygame.Rect((segment[0] * GRID_SIZE, segment[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GREEN, rect)