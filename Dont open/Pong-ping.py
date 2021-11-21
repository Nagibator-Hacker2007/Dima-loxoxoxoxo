from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700,500))
display.set_caption("tipycal bitcoin stock Exchange")
background = transform.scale(image.load('13.jpg'),(700,500))
class Game(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,palyer_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed = palyer_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bennito(Game):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 433:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 433:
            self.rect.y += self.speed

game = True
finish = False
FPS = 144
font.init()
font = font.Font(None,70)
player = Bennito("14.jpg",0,50,5)
player2 = Bennito("15.png",633,50,5)
ball = Game("12.png",350,250,3)






while game :
    clock = time.Clock()
    clock.tick(FPS)
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        player2.reset()
        player.update_l()
        player2.update_r()
        ball.reset()
        
        for e in event.get():
            if e.type ==QUIT:
                game= False
    key_pressed=key.get_pressed()
    display.update()
    #time.delay(50)