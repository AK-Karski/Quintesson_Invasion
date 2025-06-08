import pyautogui
import pygame
#试做
#这里是看板模块喔！
class Play_Button:
    def __init__(self):
        self.image = pygame.image.load('images/main_page_image/buttons_image/play_button.png')
        self.rect = self.image.get_rect()

class Choose_Character_Button:
    def __init__(self):
        self.image = pygame.image.load('images/main_page_image/buttons_image/choose_character_button.png')
        self.rect = self.image.get_rect()        

class Quit_Button:
    def __init__(self):
        self.image = pygame.image.load('images/main_page_image/buttons_image/quit_button.png')
        self.rect = self.image.get_rect()
        
class Main_Page:
    
    def __init__(self,QI_game):
        
        self.QI_game = QI_game
        self.screen = QI_game.screen
        self.screen_width = QI_game.screen_width
        self.screen_height = QI_game.screen_height
        self.screen_rect = self.screen.get_rect()
        self.settings = QI_game.settings

        self.background_image = pygame.image.load('images/main_page_image/background_image/background_normal.png')
        
    def draw_main_page(self):
        self.draw_background()
        self.draw_play_button()
        self.draw_choose_charcter_button()
        self.draw_quit_button() 
    
    
    def draw_background(self):
        
        adopted_background_image = pygame.transform.scale(self.background_image,(self.screen_width,self.screen_height))
        adopted_background_image_rect = self.background_image.get_rect()
        adopted_background_image_width,adopted_background_image_height = adopted_background_image.get_size()
        adopted_background_image_rect.x = (self.screen_width - adopted_background_image_width)//2
        adopted_background_image_rect.y = (self.screen_height - adopted_background_image_height)//2
        self.screen.blit(adopted_background_image,adopted_background_image_rect)
        
    def draw_play_button(self):
        
        self.play_button = Play_Button()
        self.play_button.rect.center = self.screen_rect.center
        self.screen.blit(self.play_button.image,self.play_button.rect)

    def draw_choose_charcter_button(self):
        
        self.choose_character_button = Choose_Character_Button()
        self.choose_character_button.rect.x = self.play_button.rect.x
        self.choose_character_button.rect.y = self.play_button.rect.y + 50
        self.screen.blit(self.choose_character_button.image,self.choose_character_button.rect)


    def draw_quit_button(self):
    
        self.quit_button = Quit_Button()
        self.quit_button.rect.x = self.play_button.rect.x
        self.quit_button.rect.y = self.play_button.rect.y + 100
        self.screen.blit(self.quit_button.image,self.quit_button.rect)
    

    
        