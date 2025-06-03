import pygame

#这里是堂堂~跟踪游戏数据模块喔~~

class GameStats:
    
    def __init__(self,QI_game):
    #初始化统计信息
        self.settings = QI_game.settings
        self.reset_stats()

    
    def reset_stats(self):
        #初始化游戏运行期间可能会变化的统计信息
        
        #玩家剩余拥有的战斗机数量       玩家初始拥有的战斗机数量（几条命）
        #不知道为什么实际的play次数永远会多一次出来，所以这里暂时打上补丁（*-1）
        self.fighter_jet_left = self.settings.fighter_jet_limit - 1
        
        #初始化得分！因为分数在每次开始游戏时会重置，即为动态参数
        #所以放在rest_stats里
        self.score = 0
        