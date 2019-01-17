#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """表示星星的类"""

    def __init__(self, screen):
        """初始化星星并设置其起始位置"""
        super(Star, self).__init__()
        self.screen = screen

        # 加载星星图像，并设置其位置属性
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # 每个星星都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)