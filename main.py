import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Infinite while loop for game loop
    while True:
        log_state()
        # Processes the pygame event queue
        for event in pygame.event.get():
            pass
        # Fills screen with black
        screen.fill("black")
        # Refresh screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
