import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    clock = pygame.time.Clock()
    delta_time = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        
        player.draw(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
