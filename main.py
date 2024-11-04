import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initializing pygame and setting screen, game clock, player
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        #quit the game using exit button on top right of the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #filling screen with black color
        screen.fill("#000000")
        player.draw(screen)
        pygame.display.flip()

        #limiting framerate to 60 FPS and calculating delta time(time passed since last frame)
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()