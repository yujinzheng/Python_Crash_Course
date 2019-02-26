#coding=utf-8

class Settings():
    """存储雨滴下落所有设置的类"""

    def __init__(self):
        """
        初始化雨滴的设置
        """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 雨滴设置
        self.rain_drop_speed = 0.01
