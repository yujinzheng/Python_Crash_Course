#coding=utf-8
import pygame

from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    """表示球的类"""

    def __init__(self, b_settings, screen):
        """
        初始化初始化球并设置其起始位置
        :param b_settings: 设置信息
        :param screen: 屏幕信息
        """
        super(Ball, self).__init__()
        self.screen = screen
        self.b_settings = b_settings

        # 加载球的图像，并设置其起始位置
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        # 球的垂直位置是固定的，但是水平位置不固定
        random_x = randint(0, self.b_settings.screen_width - self.rect.width)
        self.rect.x = random_x
        self.rect.y = 0

        # 存储雨滴的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """
        在指定的位置绘制雨滴
        :return: None
        """
        self.screen.blit(self.image, self.rect)

    def reset(self):
        """重置球的位置信息"""
        random_x = randint(0, self.b_settings.screen_width)
        self.rect.x = random_x
        self.y = 0

    def update(self):
        """更新球的位置信息"""
        self.rect.y = self.y