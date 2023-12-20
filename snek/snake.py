
import pygame
import random

class Snake:
    def __init__(self, screen):
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) ##spawns in the middle 
        self.food_pos = pygame.Vector2(random.randrange(0, screen.get_width()) , random.randrange(0, screen.get_height())) ##spawns radomly
        self.body = []

    def draw_head(self, screen, color="black", size=15):
        head = pygame.Rect((self.player_pos.x, self.player_pos.y, size, size))
        pygame.draw.rect(screen, color, head)  
        return head

    def draw_food(self, screen, color="red", size=15):
        apple = pygame.Rect((self.food_pos.x, self.food_pos.y, size, size))
        pygame.draw.rect(screen, color, apple)
        return apple

    def draw_body(self, screen, color="black"):
        for body in self.body:
            pygame.draw.rect(screen, color, body)
        
    def add_body(self, disp = 15, size= 15):
        body_pos = pygame.Vector2(self.player_pos.x - (disp * len(self.body)), self.player_pos.y - (disp * len(self.body))) ##this needs to add 15 each time its called
        self.body.append(pygame.Rect((body_pos.x, body_pos.y, size, size)))
    
    def movement(self, body_list: list, dt: int): #position needs to be common
        for rect in body_list:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                #self.player_pos.y -= 200 * dt
                body_list[rect].y -= 200 * dt
            elif keys[pygame.K_s]:
                #self.player_pos.y += 200 * dt 
                body_list[rect].y += 200 * dt
            elif keys[pygame.K_a]:
                #self.player_pos.x -= 200 * dt   
                body_list[rect].x += 200 * dt
            elif keys[pygame.K_d]:
                #self.player_pos.x += 200 * dt
                body_list[rect].x += 200 * dt 

    def reset():
        pass
    
    def collision_detection():
        pass