import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initial setup
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    
    # Setup the group
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    
    # Asteroid field setup
    AsteroidField.containers = (updatable)
    AsteroidField()
    
    # Asteroid setup
    Asteroid.containers = (asteroids, drawable, updatable)
    
    # Player setup
    Player.containers = (drawable, updatable)
    
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    Player(player_x, player_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        
        for unit in updatable:
            unit.update(delta_time)
        for unit in drawable:
            unit.draw(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
