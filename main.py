import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asterioidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =pygame.sprite.Group()

    #initializing pygame and setting screen, game clock, player
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    #adding all Players to groups updatable and drawable
    Player.containers = (updatable, drawable)
    #adding all Asteroids to groups updatable, drawable, asteroids
    Asteroid.containers = (updatable, drawable, asteroids)
    #adding AsteroidField to groups updatable
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        #limiting framerate to 60 FPS and calculating delta time(time passed since last frame)
        dt = game_clock.tick(60) / 1000
        #quit the game using exit button on top right of the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #filling screen with black color
        screen.fill("#000000")

        #drawing everything in group drawable to screen
        for drawing in drawable:
            drawing.draw(screen)
        #player.draw(screen)

        #updating everything in group updatable
        for upd in updatable:
            upd.update(dt)
        #player.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()