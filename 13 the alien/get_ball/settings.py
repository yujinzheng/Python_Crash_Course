#coding=utf-8

class Settings():
    """存储所有设置的类"""

    def __init__(self):
        """
        初始化设置
        """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 球的设置
        self.ball_drop_speed = 0.1

        # 碗的设置
        self.bowl_speed_factor = 0.5
