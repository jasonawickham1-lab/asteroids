import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    # Create group containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable, updatable)
    
    # Create game clock
    clock = pygame.time.Clock()
    dt = 0.0

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create player and asteroid field object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # Infinite while loop for game loop
    while True:
        log_state()
        
        # Processes the pygame event queue
        for event in pygame.event.get():
            
            # Exit game loop when window is closed
            if event.type == pygame.QUIT:
                return
        
        # Fills screen with black
        screen.fill("black")

        # Update player rotation
        updatable.update(dt)

        # Re-render the player
        for drawing in drawable:
            drawing.draw(screen)
        
        # Refresh screen
        pygame.display.flip()

        # Check for collision
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Check for shot connecting
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    Asteroid.split(asteroid)
                    Shot.kill(shot)
        
        # Returns time since last time called
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
