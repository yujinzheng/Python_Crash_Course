#coding=utf-8
import pygame
from pygame.sprite import Sprite
from random import randint

class Rectangular(Sprite):
    """表示单个矩形的类"""

    def __init__(self, ai_settings, screen):
        """初始化矩形并设置其起始位置"""
        super(Rectangular, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.color = ai_settings.rectangular_color

        # 在(0,0)处创建一个矩形，再设置正确的位置
        self.rect = pygame.Rect(-500, -500, ai_settings.rectangular_width, ai_settings.rectangular_height)
        self.y = float(self.rect.y)

        # 矩形在页面的右边，矩形的高度不确定
        self.rect.right = self.screen_rect.right
        self.y = randint(0, self.screen_rect.bottom - ai_settings.rectangular_height)


    def draw_rectangular(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        """如果矩形位于屏幕边缘，就返回true"""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.y += (self.ai_settings.rectangular_speed_factor * self.ai_settings.rectangular_direction)
        self.rect.y = self.y