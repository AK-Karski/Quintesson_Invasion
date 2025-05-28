import pygame
from pygame.sprite import Sprite
#这里是堂堂~子弹模块喔！

#你可以通过修改子弹的尺寸或者其他属性来设计出威力更强的武器喔！

#Bullet类继承从模块pygame.sprite中导入的Sprite类
class Bullet(Sprite):
    
    def __init__(self,QI_game):
        #继承Sprite类
        super().__init__()
        self.screen = QI_game.screen
        self.settings = QI_game.settings
        self.image = pygame.image.load('images/alian_1.bmp')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        '''#嗯...也可以直接做成图形样式
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,255,255)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        '''
        self.rect = self.image.get_rect()
        self.rect.midtop = QI_game.fighter_jet.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self):
        #向上移动子弹
        #更新子弹的准确位置
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def blit_me(self):
        self.screen.blit(self.image,self.rect)
        