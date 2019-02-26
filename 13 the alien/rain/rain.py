#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """表示一滴雨的类"""

    def __init__(self, r_settings, screen):
        """
        初始化雨滴并设置其起始位置
        :param r_settings: 设置信息
        :param screen: 屏幕信息
        """
        super(Rain, self).__init__()
        self.screen = screen
        self.r_settings = r_settings

        # 加载雨滴的图像，并设置其起始位置
        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()

        # 每滴雨都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储雨滴的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """
        在指定的位置绘制雨滴
        :return: None
        """
        self.screen.blit(self.image, self.rect)