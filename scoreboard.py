import pygame.font

class Scoreboard:
    #这里是计分板喔！！显示得分信息！
    
    def __init__(self,QI_game):
        #初始化显示得分的初始属性
        
        self.screen = QI_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = QI_game.settings
        self.stats = QI_game.stats
        
        #显示得分信息时使用的字体属性
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #准备初始得分图像
        self.pre_score()
        
    def pre_score(self):
        #将得分渲染为图像
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        
        #在屏幕——右上角——显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        #在屏幕上显示得分
        self.screen.blit(self.score_image,self.score_rect)
        