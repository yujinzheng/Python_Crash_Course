#coding=utf-8

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 5
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 1

        # 矩形设置
        self.rectangular_width = 50
        self.rectangular_height = 100
        self.rectangular_color = (255, 0, 0)

        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        """用来初始化游戏的动态设置"""
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 1
        self.rectangular_speed_factor = 0.1

        # rectangular_direction为1表示向右移，为-1表示向左移
        self.rectangular_direction = 1

    def increase_speed(self):
        """用来提升游戏速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.rectangular_speed_factor *= self.speedup_scale
        self.rectangular_direction = 1