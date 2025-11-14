import sys
import pygame

from constants import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from logger import log_state


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initial setup
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    # Load the background
    background_img = pygame.image.load('./assets/img/background.png')
    # Scale the bg image up to half the screen width and height
    background_img = pygame.transform.scale(
        background_img, (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT))
    background_img_positions = [
        (0, 0),
        (HALF_SCREEN_WIDTH, 0),
        (0, HALF_SCREEN_HEIGHT),
        (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT),
    ]

    # Create sound objects
    shoot_sound = pygame.mixer.Sound("./assets/audio/shoot.wav")
    explosion_sound = pygame.mixer.Sound("./assets/audio/explosion.wav")
    player_die_sound = pygame.mixer.Sound("./assets/audio/player_die.wav")

    # Initialize the mixer
    pygame.mixer.init()
    # Load the background music
    pygame.mixer.music.load("./assets/audio/background-music.ogg")
    # Play the background music
    pygame.mixer.music.play()

    # Setup the group
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Asteroid field setup
    AsteroidField.containers = (updatable)
    AsteroidField()

    # Asteroid setup
    Asteroid.containers = (asteroids, drawable, updatable)
    Asteroid.kill_sound_effect = explosion_sound

    # Bullet setup
    Bullet.containers = (bullets, drawable, updatable)
    Bullet.init_sound_effect = shoot_sound

    # Player setup
    Player.containers = (drawable, updatable)
    Player.kill_sound_effect = player_die_sound

    player_x = HALF_SCREEN_WIDTH
    player_y = HALF_SCREEN_HEIGHT
    player = Player(player_x, player_y)

    while True:
        log_state()

        # Check for quite event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Render background
        screen.fill("black")

        for bg_pos in background_img_positions:
            screen.blit(background_img, bg_pos)

        # Update unit positions
        for unit in updatable:
            unit.update(delta_time)

        # Draw units
        for unit in drawable:
            unit.draw(screen)

        # Check for collisions
        for asteroid_obj in asteroids:
            if asteroid_obj.is_colliding(player):
                player.kill()
                print("Game Over!")
                sys.exit(1)

            for bullet_obj in bullets:
                if asteroid_obj.is_colliding(bullet_obj):
                    asteroid_obj.split()
                    bullet_obj.kill()

        # End the frame
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
