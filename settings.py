# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:50:55 2021

@author: Dell
"""

class Settings:
    """存储游戏所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width =1000
        self.screen_height = 700
        self.bg_color = (230,230,230)
        
        #飞船速度
        self.ship_limit = 3
        
        #子弹设置
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = (60, 60, 60)
        self.bullet_allow = 3
        
        #外星人设置
        self.fleet_drop_speed = 10
        
        #游戏加速
        self.speedup_scale = 1.1
        #外星人分数提高的速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 0.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.3
        
        self.fleet_direction = 1
        
        #计分
        self.alien_points = 50
        
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)