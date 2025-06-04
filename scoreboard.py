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
        self.pre_highest_score()
        
        
    def pre_score(self):
        #将得分渲染为图像
            #rounded()函数通常让浮点数（第一个实参）精确至小数点后一位
            #其中的小数位数由第二个实参指定，如果第二个实参为负数，
            #round()函数会将第一个实参舍入到最近的10的整数倍数
        rounded_score = round(self.stats.score , -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        
        #在屏幕——右上角——显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def pre_highest_score(self):
        #将最高得分渲染为图像
        highest_score = round(self.stats.highest_score , -1)
        highest_score_str = f"{highest_score:,}"    # : ,为格式说明符，它将在数字的合适位置加上 ，
        self.highest_score_image = self.font.render(highes_score_str,True,self.text_color,self.settings.bg_color)

        #在屏幕——顶部中央——显示最高得分
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.right = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top 

    def check_highest_score(self):
        #检查是否诞生了新的最高分
        if self.stats.score >= self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.pre_highest_score()
 
 
    def show_score(self):
        #在屏幕上显示得分
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.highest_score_image,self.highest_score_rect)