import sys, pygame

pygame.init()

# define constants
FPS = 60

MAP_WIDTH, MAP_HEIGHT = 25, 20
TILE_SIZE = 24
SIDE_BORDER = 35
TOP_BORDER = SIDE_BORDER * 3

WIDTH = MAP_WIDTH * TILE_SIZE + SIDE_BORDER * 2
HEIGHT = MAP_HEIGHT * TILE_SIZE + TOP_BORDER + SIDE_BORDER

# dictionary (hash map) of game speed rates depending on score, game_speed (measured in ms)
GAME_UPDATE_RATES = {
    0: 333,
    5: 300,
    10: 275,
    15: 250,
    20: 225,
    30: 200,
    45: 175,
    60: 150,
    80: 125,
    100: 100
}

MENU, GAME = 0, 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (204, 204, 204)
GRAY = (153, 153, 153)
DARK_GRAY = (64, 64, 64)
GREEN = (0, 204, 0)
ORANGE = (255, 102, 0)

# define game variables
keys = {
    pygame.K_ESCAPE,
    pygame.K_RETURN,
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_LEFT,
    pygame.K_RIGHT
}

game_state = MENU
keys_held = {}
keys_pressed = {key: False for key in keys}

game_over = False
score = 0
game_speed = GAME_UPDATE_RATES.get(score)

# create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# main loop
def main():
    global keys_held, keys_pressed
    
    running = True
    while running:
        keys_held = {key: False for key in keys}
        keys_pressed = {key: False for key in keys}
    
        # read through input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # check for one-off key presses
            if event.type == pygame.KEYDOWN:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = True
                
        # update which keys are held down
        keys_held = pygame.key.get_pressed()
            
        # clear the screen
        screen.fill(DARK_GRAY)
        
        draw_board()
            
        if game_state == MENU:
            menu_tick()
            menu_render()
        
        if game_state == GAME:
            game_tick()
            game_render()
            
        # update the display and cap the frame rate
        pygame.display.flip()
        clock.tick(FPS)

# game logic        
def game_tick():
    return

def game_render():
    return
            
# menu logic
def menu_tick():
    if keys_pressed[pygame.K_RETURN]:
        set_game_state(GAME)

def menu_render():
    return

def draw_board():
    pygame.draw.rect(screen, GRAY, (SIDE_BORDER, TOP_BORDER, WIDTH - SIDE_BORDER * 2, HEIGHT - TOP_BORDER - SIDE_BORDER))
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                pygame.draw.rect(screen, LIGHT_GRAY, (SIDE_BORDER + x * TILE_SIZE, TOP_BORDER + y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
def set_game_state(new_game_state):
    global game_state
    game_state = new_game_state      
        
if __name__ == "__main__":
    main()