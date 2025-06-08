import pygame
import pyautogui
from main_page import Main_Page
from character_page import Character_Page
#试做
#这里是页面切换系统！

        
page_lib = {'main_page': 1 ,'character_page': 2 }

page_flag = 1
        
def switch_to_main_page():
    
        page_flag = 1
        
def switch_to_character_page():
    
        page_flag = 2
        
def draw_page(QI_game):
        
    if page_flag == 1:
        main_page = Main_Page(QI_game)
        main_page.draw_main_page()
        
    elif self.page_flag == 2:
        character_page = Character_Page(QI_game)
        character_page.draw_character_page()
        