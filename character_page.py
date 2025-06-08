import pyautogui
import pygame
#试做
#这里是角色选择模块喔！

class Back_Button:
    
    def __init__(self):
        self.image = pygame.image.load('images/character_page_image/back_button.png')
        self.rect = self.image.get_rect()


class Character_Page:
    
    def __init__(self,QI_game):
    
        self.QI_game = QI_game
        self.screen = QI_game.screen
        self.screen_width = QI_game.screen_width
        self.screen_height = QI_game.screen_height
        self.screen_rect = self.screen.get_rect()
        self.settings = QI_game.settings
        
        self.background_image = pygame.image.load('images/character_page_image/background.png')
        self.back_button_image = pygame.image.load('images/character_page_image/back_button.png')
        self.back_button_image_rect =self.back_button_image.get_rect()
        
        self.back_button = Back_Button()
        
    def draw_character_page(self):
        draw_background()
        draw_back_button()


    
    def draw_background(self):
        
        adopted_background_image = pygame.transform.scale(self.background_image,(self.screen_width,self.screen_height))
        adopted_background_image_rect = self.background_image.get_rect()
        adopted_background_image_width,adopted_background_image_height = adopted_background_image.get_size()
        adopted_background_image_rect.x = (self.screen_width - adopted_background_image_width)//2
        adopted_background_image_rect.y = (self.screen_height - adopted_background_image_height)//2
        self.screen.blit(adopted_background_image,adopted_background_image_rect)
        
    def draw_back_button(self):
        
        self.back_button.rect = self.back_button_image.get_rect()
        self.back_button.rect.x = 10
        self.back_button.rect.y = 10
        self.screen.blit(self.back_button.image,self.back_button.rect)
        