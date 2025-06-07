import pyautogui
import pygame
#试做
#这里是看板模块喔！

class Main_Page:
    
    def __init__(self,QI_game):
        
        self.QI_game = QI_game
        self.screen = QI_game.screen
        self.screen_width = QI_game.screen_width
        self.screen_height = QI_game.screen_height
        self.screen_rect = self.screen.get_rect()
        self.settings = QI_game.settings
        
        self.background_image = pygame.image.load('images/background_image/background_normal.png')
        self.play_button_image = pygame.image.load('images/buttons_image/play_button.png')
        self.choose_character_button_button_image = pygame.image.load('images/buttons_image/choose_character_button.png')
        self.quit_button_image = pygame.image.load('images/buttons_image/quit_button.png')
        
    def draw_main_page(self):
        
        adopted_background_image = pygame.transform.scale(self.background_image,(self.screen_width,self.screen_height))
        adopted_background_image_rect = self.background_image.get_rect()
        adopted_background_image_width,adopted_background_image_height = adopted_background_image.get_size()
        adopted_background_image_rect.x = (self.screen_width - adopted_background_image_width)//2
        adopted_background_image_rect.y = (self.screen_height - adopted_background_image_height)//2
        self.screen.blit(adopted_background_image,adopted_background_image_rect)
        
    def draw_play_button(self):
        
        self.play_button_image_rect = self.play_button_image.get_rect()
        self.play_button_image_rect.center = self.screen_rect.center
        self.screen.blit(self.play_button_image,self.play_button_image_rect)

    def draw_choose_charcter_button(self):

        self.choose_character_button_button_image_rect = self.choose_character_button_button_image.get_rect()
        self.choose_character_button_button_image_rect.x = self.play_button_image_rect.x
        self.choose_character_button_button_image_rect.y = self.play_button_image_rect.y + 50
        self.screen.blit(self.choose_character_button_button_image,self.choose_character_button_button_image_rect)


    def draw_quit_button(self):
    
        self.quit_button_image_rect = self.quit_button_image.get_rect()
        self.quit_button_image_rect.x = self.play_button_image_rect.x
        self.quit_button_image_rect.y = self.play_button_image_rect.y + 100
        self.screen.blit(self.quit_button_image,self.quit_button_image_rect)
    

    
        