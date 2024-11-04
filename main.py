import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asterioidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initializing pygame and setting screen, game clock, player
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    #game_loop(screen, dt, game_clock)
    main_menu(screen, game_clock, dt)
    

#function to draw text to buttons
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu(screen, game_clock, dt):
    text_font = pygame.font.Font(None, 40)
    game_clock.tick(60) / 1000

    #buttons in main menu
    button_start = pygame.Rect(
        (SCREEN_WIDTH / 2 - MAIN_MENU_BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + 20), 
        (MAIN_MENU_BUTTON_WIDTH, MAIN_MENU_BUTTON_HEIGHT)
    )
    button_options = pygame.Rect(
        (SCREEN_WIDTH / 2 - MAIN_MENU_BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + 100),
        (MAIN_MENU_BUTTON_WIDTH, MAIN_MENU_BUTTON_HEIGHT)
    )
    button_quit = pygame.Rect(
        (SCREEN_WIDTH / 2 - MAIN_MENU_BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + 180),
        (MAIN_MENU_BUTTON_WIDTH, MAIN_MENU_BUTTON_HEIGHT)
    )

    running = True
    while running:
        screen.fill("#000000")
        
        # Draw buttons and text
        pygame.draw.rect(screen, "#FFFFFF", button_start, 2)
        pygame.draw.rect(screen, "#FFFFFF", button_options, 2)
        pygame.draw.rect(screen, "#FFFFFF", button_quit, 2)

        draw_text("Start Game", text_font, "#FFFFFF", screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 42.5)
        draw_text("Options", text_font, "#FFFFFF", screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 122.5)
        draw_text("Quit", text_font, "#FFFFFF", screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 202.5)

        choise_flag = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    print("Start Game clicked!")
                    running = False  # Transition to game
                    choise_flag = 1
                elif button_options.collidepoint(event.pos):
                    print("Options clicked!")
                    choise_flag = 2
                    # Call options function or submenu here
                elif button_quit.collidepoint(event.pos):
                    print("Game quit.")
                    return

        # Update display
        pygame.display.flip()
    
    if choise_flag == 1:
        game_loop(screen, dt, game_clock)

def game_loop(screen, dt, game_clock):
    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    #adding all Players to groups updatable and drawable
    Player.containers = (updatable, drawable)
    #adding all Asteroids to groups updatable, drawable, asteroids
    Asteroid.containers = (updatable, drawable, asteroids)
    #adding AsteroidField to groups updatable
    AsteroidField.containers = (updatable)
    #adding all Shots to groups updatable, drawable, shots
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    game_running = True

    while game_running:
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

        #updating everything in group updatable
        for upd in updatable:
            upd.update(dt)
        
        for asteroid in asteroids:
            if player.coll_check(asteroid):
                print("Game Over!")
                game_running = False

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.coll_check(asteroid):
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()

    main_menu(screen, game_clock, dt)

if __name__ == "__main__":
    main()