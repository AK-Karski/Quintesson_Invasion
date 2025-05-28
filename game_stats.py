import pygame

#这里是堂堂~跟踪游戏数据模块喔~~

class GameStats:
    
    def __init__(self.QI_game):
    #初始化统计信息
        self.settings = QI_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        #初始化游戏运行期间可能会变化的统计信息
        
        #玩家剩余拥有的战斗机数量       玩家初始拥有的战斗机数量（几条命）
        fighter_jet_left = self.settings.fighter_jet_limit
        