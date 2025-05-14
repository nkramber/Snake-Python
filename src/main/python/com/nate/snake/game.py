import pygame
import sys
from snake import Snake
from food import Food
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, FRAME_RATE, GAME_NAME

class Game:
    # Initialization method
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()
        self._score = 0 # Protected variable indicated by single underscore
        self.__running = True # Private variable indicated by double underscore
        
        self._snake = Snake() # Public variable indicated by no underscore
        self._food = Food()
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self._snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    self._snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self._snake.direction = (1, 0)
                    
    def _update(self):
        self._snake.update()
        
        # Check food collision
        if self._snake.head == self._food.position:
            self._food.spawn()
            self._snake.grow()
            self._score += 1
            
        # Check self collision
        if self._snake.check_collision():
            self.__running = False
        
    def _draw(self):
        # Draw entities
        self._screen.fill(BLACK)
        self._snake.draw(self._screen)
        self._food.draw(self._screen)
        
        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self._score}', True, WHITE)
        self._screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        
    # Getter method
    @property
    def _score(self):
        return self.__score
    
    # Setter method
    @_score.setter
    def _score(self, value):
        if not isinstance(value, int): # Make sure our score is an int
            raise TypeError("Score must be an integer")
        if value < 0:
            raise ValueError("Score cannot be negative")
        
        self.__score = value
        
    def run(self):
        while self.__running:
            self._handle_events()
            self._update()
            self._draw()
            self._clock.tick(FRAME_RATE)
            
        pygame.quit()
        sys.exit()