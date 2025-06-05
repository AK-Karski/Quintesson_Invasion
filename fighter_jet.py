import pygame
from pygame.sprite import Sprite

#这里是堂堂~战斗机模块喔！！

class Fighter_Jet(Sprite):
    
    def __init__(self,QI_game):
        
    #初始化F_QI_game并设置其初始位置
        super().__init__()
        #获取（游戏实例）屏幕大小并获取其外接矩形
        self.screen = QI_game.screen
        self.settings = QI_game.settings
        
        self.screen_rect = QI_game.screen.get_rect()
        self.screen_width = QI_game.screen_width
        self.screen_height = QI_game.screen_height
    
        #加载战斗机图像并获取其外接矩形
        self.image = pygame.image.load('images/jet_1.bmp')
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        #战斗机矩形的底部中央 ——对准——屏幕矩形的底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        #在战斗机的属性x中存储一个浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #移动标志（战斗机一开始不移动）
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def center_fighter_jet(self):
        #将战斗机放至屏幕底部中央
        #随后重置用于跟踪战斗机确切位置的self.x

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        #我靠！！你原来缺了这个！，我就说怎么每次都跑屏幕中间
        self.y = float(self.rect.y)
        
    def blit_me(self):
        #在指定位置（？）（self.rect）绘制战斗机图像
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.fighter_jet_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.fighter_jet_speed
        elif self.moving_up and self.rect.y > 0:
            self.y -= self.settings.fighter_jet_speed
        elif self.moving_down and self.rect.y < (self.screen_height - (self.height)):
            self.y += self.settings.fighter_jet_speed
            
        #根据rect更新对象
        self.rect.x = self.x
        self.rect.y = self.y
            
#        print(self.screen_rect.midbottom,self.rect.midbottom,self.x)    
            
    