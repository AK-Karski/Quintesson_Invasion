import pygame
from pygame.sprite import Sprite
#这里是~堂堂~~五面怪模块喔~

class Quintesson(Sprite):
 
    def __init__(self,QI_game):
        super().__init__()
        self.screen = QI_game.screen
        self.settings = QI_game.settings
        self.image = pygame.image.load('images/enemies_image/alian_1.bmp')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        #令每只五面怪最初都生成于屏幕左上角附近
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #存储五面怪的精确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    #更新五面怪位置前先检查五面怪是否到达屏幕边缘
    def check_edge(self):
        #如果发现五面怪到达屏幕边缘，则返回True,否则返回False
        screen_rect = self.screen.get_rect()
        #看啊~如此高效优雅的做法~
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left)


    
    def update(self):
            #五面怪的移动~ ~更新五面怪移动后的位置~~
            self.x += self.settings.quintesson_speed * self.settings.fleet_direction
            self.rect.x = self.x
        
        