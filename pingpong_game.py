import pygame

pygame.init()
window = pygame.display.set_mode((1100, 700))
HEIGHT = 700
WIDTH = 1100
pygame.display.set_caption('Shooter') 

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.w = player_width
        self.h = player_height
        self.image = transform.scale(
            image.load(player_image), 
            (self.h, self.w)
        )
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.y < 920:
            self.rect.y  -= self.speed
game = True
while game = True:
    for e in event.get():
        if e.type = QUIT:
            game = False
    pygame.display.update()