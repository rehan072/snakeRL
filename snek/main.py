# Example file showing a basic pygame "game loop"
import pygame
from snake import Snake
import time
import random

##TODO:

#make movement in only 2 dimesnions
#make borders
#collision detection with food and then redraw food

# pygame setup
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    snake_game = Snake(screen)

    #basilisk = snake_game.draw_snake(screen=screen)
    #food = snake_game.draw_food(screen)


    ##game loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")
        basilisk_head = snake_game.draw_head(screen)
        food = snake_game.draw_food(screen)

        if len(snake_game.body) != 0:
            snake_game.draw_body(screen)
        
        ## movement
        ## limits of x and y
        ## x is limited to 0 and screen width
        ## y is limited to screen height 
        
        #boundary logic  - to fix
        if snake_game.player_pos.y <= 0:
            snake_game.player_pos.y += 15
        if snake_game.player_pos.y >= screen.get_height():
            snake_game.player_pos.y -= 20
        if snake_game.player_pos.x <= 0:
            snake_game.player_pos.x += 15
        if snake_game.player_pos.x >= screen.get_width():
            snake_game.player_pos.x -= 20

        ##moving in 2D and changing render speed
        snake_game.movement(dt=dt)

    
        ##checking if got food
        if basilisk_head.colliderect(food):
            #print("moved")
            #food.move(random.randrange(0, screen.get_width()),random.randrange(0, screen.get_height()))
            #move food
            snake_game.food_pos.x = random.randrange(0, screen.get_width())
            snake_game.food_pos.y = random.randrange(0, screen.get_height())

            ##need to add to the body
            snake_game.add_body()

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
