import sys
import pygame
#在数组中随机选中一个元素
from random import randint
#让程序暂停一会儿
from time import sleep
from settings import Settings
from fighter_jet import Fighter_Jet
from bullet import Bullet
from quintesson import Quintesson
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import page_switch
from main_page import Main_Page,Play_Button,Choose_Character_Button,Quit_Button
from character_page import Back_Button,Character_Page

class QuintessonInvasion:
        
        #初始化游戏并创造游戏资源    
    def __init__(self):
    
        #调用pygame.ini()函数来初始化背景
        pygame.init()
        #创建Clock以控制游戏帧率
        self.clock = pygame.time.Clock()
        #根据Setting类创建setting实例，并使用它来访问游戏设置
        self.settings = Settings()
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        '''
        #设置全屏模式
            #传入尺寸（0,0）以及参数pygame.FULLSCREEN
            #创建覆盖全屏的屏幕后使用get_rect()来获取全屏屏幕的大小
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self_screen.get_rect().width
        self.settings.screen_height = self_screen.get_rect(),height
        
        '''
                        #设置游戏窗口左上角游戏名    
        pygame.display.set_caption("五面怪入侵~博派飞行小队の大突围desu~")
        

        #创建你的主页面！
        self.main_page = Main_Page(self)
        self.play_button = Play_Button()
        self.choose_character_button = Choose_Character_Button()
        self.quit_button = Quit_Button()
        
        #创建你的角色选择页面
        self.character_page = Character_Page(self)
        self.back_button = Back_Button()
        #创建你的用于存储游戏统计信息的实例~
        self.stats = GameStats(self)
        
        #创建你的记分牌~
        self.scoreboard = Scoreboard(self)
        
        #创建你的主角战斗机~
        self.fighter_jet = Fighter_Jet(self)

        #创建你的子弹编组~
        self.bullets = pygame.sprite.Group()
        
        #创建你的五面怪编组~
        self.quintessons = pygame.sprite.Group()
        self._creat_fleet()
        
        
        #判断游戏结束条件
        self.game_active = False
        

        
        
        #游戏总控
    def run_game(self):
        #游戏的主循环
        while True:
            
            self._check_events()
            
            if self.game_active:
                self.fighter_jet.update()
                self._update_bullet()
                self._update_quintessons()
            self._update_screen()
            #维持稳定帧率             #pygame会尽可能确保此循环每秒运行（60）次
            self.clock.tick(60)

    #通过重构简化run game方法，将部分功能收入其他方法中以缩减其篇幅
    
    #管理事件
    def _check_events(self):
        #侦听鼠标和键盘事件（一直监测，直到玩家单击游戏窗口中的退出按钮）
        #event事件（玩家执行的操作）      
        #访问pygame检测到的事件：此函数返回一个列表，包括他在上一次调用后的发生的所有事件
        for event in pygame.event.get():
            #如果监听到的事件为pygame中的QUIT(退出)操作，则使用sys模块的exit()函数来退出游戏
             
            #事件为--点击窗口上的quit键   或   按下Q键
            if event.type == pygame.QUIT or event.type == pygame.K_q:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #get_pos方法返回一个元组，包含鼠标点击时光标的x，y坐标
                #检查主页面按钮
                self._check_play_button(mouse_pos)
                self._check_choose_character_button(mouse_pos)
                self._check_quit_button(mouse_pos)
                #检查角色选择页面按钮
                self._check_back_button_in_2_page(mouse_pos)
            
            #用户按一次键盘上的按键——会在pygame中产生一个KEYDOWN事件
            #事件为--按下键盘按键
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                                
            #用户放开键盘上的按键——会在pygame中产生一个KEYUP事件
            #事件为-放开键盘按键
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self,mouse_pos):
        #在玩家单击play按钮时开始新游戏
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #重置游戏的动态设置
            self.settings.initialize_dynamic_settings()
            #重置游戏的统计信息
            self.stats.reset_stats()            
            self.game_active = True
            
            self.scoreboard.prep_score
            
            #清空子弹列表和五面怪列表
            self.bullets.empty()
            self.quintessons.empty()
            
            #创建新五面怪舰队并将战斗机放至屏幕底部中央
            self._creat_fleet()
            self.fighter_jet.center_fighter_jet()
            
            #令鼠标光标不可见
            pygame.mouse.set_visible(False)

    def _check_choose_character_button(self,mouse_pos):
        #在玩家单击choose_character按钮时进入选择角色页面
        button_clicked = self.choose_character_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            page_switch.switch_to_character_page
    
    def _check_back_button_in_2_page(self,mouse_pos):
        #玩家单击角色选择页面的back按钮
        button_clicked = self.back_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            page_switch.switch_to_main_page
        
        
    def _check_quit_button(self,mouse_pos):
        #在玩家单击quit按钮时退出游戏
        button_clicked = self.quit_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            sys.exit()

    #管理keydown事件               
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT and self.fighter_jet.rect.right < self.settings.screen_width:
            #向右移动——self.settings.fighter_jet_speed
            self.fighter_jet.x += self.settings.fighter_jet_speed 
            self.fighter_jet.moving_right = True
        elif event.key == pygame.K_LEFT and self.fighter_jet.rect.left > 0 :
            #向左移动——self.settings.fighter_jet_speed
            self.fighter_jet.x -= self.settings.fighter_jet_speed
            self.fighter_jet.moving_left = True               
        elif event.key == pygame.K_UP and self.fighter_jet.y > 0:
            #向上移动——self.settings.fighter_jet_speed
            self.fighter_jet.y -= self.settings.fighter_jet_speed
            self.fighter_jet.moving_up = True
        elif event.key == pygame.K_DOWN and self.fighter_jet.y < (self.settings.screen_height - (self.fighter_jet.height) ):
            #向下移动——self.settings.fighter_jet_speed
            self.fighter_jet.y += self.settings.fighter_jet_speed
            self.fighter_jet.moving_down = True    
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            

    #管理keyup事件                   
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.fighter_jet.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fighter_jet.moving_left = False
        elif event.key == pygame.K_UP:
            self.fighter_jet.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.fighter_jet.moving_down = False    


    #开火~
    def _fire_bullet(self):
        #创建一颗子弹，并将其加入编组bullets
        #并将其图像随机切换一个
        new_bullet = Bullet(self)
        self.settings.generate_random_image(new_bullet)
        self.bullets.add(new_bullet)
    
    #更新子弹位置并在子弹飞至屏幕外后删除子弹
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_collisions_between_bullets_quintesssons()

    #检查是否有子弹击中了五面怪
    def _check_collisions_between_bullets_quintesssons(self):
        #如果结果为“是”，那么就删除相应的子弹和五面怪
        collisions = pygame.sprite.groupcollide(self.bullets,self.quintessons,True,True)
        #将bullets列表中的所有bullet的rect与quintesons列表中的所有quintesson进行比较，
        #看它们是否重叠在了一起，每当有重叠时，groupcollide()就在返回的字典中新增对应重叠子弹与五面怪的键值对
        #两个值为True的实参告诉pygame在发生碰撞时删除对应的子弹和五面怪
        #（*若要模拟能够穿透五面怪的高能子弹，可将第一个True改为False，这样被击中的五面怪消失而子弹始终有效
    
        if collisions:
            #确保每个被击落的五面怪都记入分数
            #防止出现比如一颗子弹击中两个五面怪
            for quintessons in  collisions.values():
                #将碰撞列表中被打中的五面怪记入得分
                self.stats.score += self.settings.quintesson_points
            self.scoreboard.prep_score()
            self.scoreboard.check_highest_score()
    
    #当前五面怪舰队被消灭干净后生成一队新的五面怪舰队
        if not self.quintessons:
            #删除现有的子弹并创建一个新的五面怪舰队
            self.bullets.empty()
            self._creat_fleet()
            self.settings.increase_speed()
            
            #提高等级
            self.stats.level += 1
            self.scoreboard.prep_level()
            
    #更新五面怪位置
    def _update_quintessons(self):

        if self.settings.switch_horizonal_movement:
            self._check_fleet_edges()
            self.quintessons.update()
        else:
            for quintesson in self.quintessons.sprites():
                quintesson.rect.y += self.settings.fleet_drop_speed

        #Spritecollideany()函数接受两个实参，一个精灵和一个编组。
        #它检查编组中是否有成员与精灵发生碰撞，并在找到与精灵碰撞的成员后停止遍历编组
        #在这里，它遍历五面怪编组，并返回第一个与战斗机发生碰撞的五面怪
        if pygame.sprite.spritecollideany(self.fighter_jet,self.quintessons):
            self._fighter_jet_hit()
   
        #检查五面怪编队是否到达屏幕边缘
        self._check_quintessons_hit_bottom()
   
   
    #创建用于存储五面怪舰队的编组
    def _creat_fleet(self):
        #创建一个五面怪，再不断向右添加，间隔为一个五面怪图像的width
        #直到所剩空间小于  五面怪图像的两倍
        #在下面再生成一行，直到生成完指定行数的五面怪  
        quintesson = Quintesson(self)
        current_x,current_y = quintesson.rect.size
        row = self.settings.quintesson_row
        
        while row:
            while current_x < (self.settings.screen_width - 1.5*quintesson.width):
                self._creat_quintesson(current_x,current_y)
                current_x += 2*quintesson.width
            #每次生成完一行后重置x值并递增y值
            current_x = quintesson.width
            current_y += 2*quintesson.height  
            row-=1
    
    def _creat_quintesson(self,x_position,y_position):
        #创建一个五面怪并将其放在当前位置中
        #并将其图像随机切换一个
        new_quintesson = Quintesson(self)
        self.settings.generate_random_image(new_quintesson)
        new_quintesson.x = x_position
        new_quintesson.y = y_position
        new_quintesson.rect.x = new_quintesson.x
        new_quintesson.rect.y = new_quintesson.y
        
        self.quintessons.add(new_quintesson)


    def _check_fleet_edges(self):
        #检查五面怪编队是否到达屏幕边缘    并采取相应措施
        for quintesson in self.quintessons.sprites():
            if quintesson.check_edge():
                self._change_fleet_direction()
                break
    
    def _check_quintessons_hit_bottom(self):
        #检查是否有五面怪到达屏幕底端
        for quintesson in self.quintessons.sprites():
            if quintesson.rect.bottom >= self.settings.screen_height:
            #像战斗机被撞到一样处理
                self._fighter_jet_hit()
                break
    
    
    def _change_fleet_direction(self):
        #将整个舰队向下移动  并   改变五面怪水平移动时的方向
        for quintesson in self.quintessons.sprites():
            quintesson.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _fighter_jet_hit(self):
        #响应战斗机和五面怪之间的碰撞
        if self.stats.fighter_jet_left > 0:
            #扣一滴血/少一只战斗机
            self.stats.fighter_jet_left -= 1
            self.scoreboard.prep_left_fighter_jet()
            
            #清空子弹列表和五面怪列表
            self.bullets.empty()
            self.quintessons.empty()

            #创建一个新的五面怪编队，并重新将飞船放在屏幕底部中央
            self._creat_fleet()
            self.fighter_jet.center_fighter_jet()
            
            #暂停一小会儿，让玩家能够看到自己撞五面怪了
            #接下来再顺次序执行下面的update_screen，将新的五面怪舰队绘制在屏幕上
            sleep(2)
    
        else:
            #结束游戏并重新将鼠标光标可视化
            self.game_active = False
            pygame.mouse.set_visible(True)
    


    #更新屏幕
    def _update_screen(self):
           #每次循环时都重置屏幕（填充颜色）
            #fill()方法适用于surface，不过仅接受一种颜色rgb值作为实参
            self.screen.fill(self.settings.bg_color)
            #只要编组中有子弹，就将其绘制
            for bullet in self.bullets.sprites():
                bullet.blit_me()
            #填充背景后绘制主角战斗机，这样可以让战斗机显示在背景之上，你懂我意思吧...）
            self.fighter_jet.blit_me()
            
            #绘制五面怪
            self.quintessons.draw(self.screen)
            
            #绘制记分牌
            self.scoreboard.show_score()
            
            #绘制开始按钮
            #为了要让play按钮显示在屏幕所有元素之上
            #要在绘制完其他所有元素之后再绘制这个按钮
            if not self.game_active:
                
                page_switch.draw_page(QI_game)
                
            #让最近绘制的屏幕可见（即实时更新屏幕）
            pygame.display.flip()
            #让此clock（时钟）计算每次游戏主循环的时间

if __name__ == '__main__':
    #创建游戏实例
    QI_game=QuintessonInvasion()
    #运行游戏
    QI_game.run_game()
            
            