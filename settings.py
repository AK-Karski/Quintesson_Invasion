from random import randint
import pygame
#这里是堂堂~设置模块喔！！






#这是一个存储游戏中所有’设置‘的类
class Settings:
    
    def __init__(self):
        
        #❤初始化游戏的静态设置
        
        self.screen_width = 960
        self.screen_height = 540
            #背景颜色的RGB值
        self.bg_color = (0,0,0)

            #玩家初始拥有几只战斗机（几条命）
        self.fighter_jet_limit = 2

        
            #生成五面怪的排数
        self.quintesson_row = 2

        
            #以什么样的速度加快游戏节奏
            #2表示玩家每提高一个等级（每顺利打掉一波五面怪），游戏节奏就翻一倍
            #1表示游戏节奏不变
        self.speedup_scale = 1.1
        
            #随玩家提高等级，五面怪分数的提高速度
        self.score_scale = 1.5
        
            #初始化随游戏进行而变化的属性
        self.initialize_dynamic_settings()
        
        

            #试做：开关们~
                #五面怪们要不要水平方向移动
        self.switch_horizonal_movement = True


    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的属性（动态属性）
            
            #战斗机的速度
        self.fighter_jet_speed = 1.5        
        
            #子弹的速度！
        self.bullet_speed = 2.0

            #五面怪水平移动的速度
        self.quintesson_speed = 1.0
            #当有五面怪接触到屏幕边缘时整个舰队向下移动的速度
        self.fleet_drop_speed = 1.0
            #fleet_direction  = 1时表示向右移动（也正应着向右x值增大）
            #fleet_direction = -1时表示向左移动（也正应着向左x值减少）
        self.fleet_direction = 1
        
            #每击落一个五面怪所获得的分数
        self.quintesson_points = 50
        
    
    def increase_speed(self):
        #提高速度设置的值
        self.fighter_jet_speed *= self.speedup_scale
        self.quintesson_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        
        self.quintesson_points = int(self.quintesson_points * self.score_scale)


           #生成随机数以选择图像
    def generate_random_image(self,replace):
        random_number = randint(1,4)
        if random_number == 1:
            replace.image = pygame.image.load('images/alian_1.bmp')
        elif random_number == 2:
            replace.image = pygame.image.load('images/alian_2.bmp')
        elif random_number == 3:
            replace.image = pygame.image.load('images/alian_3.bmp')

 
        