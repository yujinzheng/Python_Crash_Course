#coding=utf-8
import pygame

class Bowl():
    """表示一个碗的类"""

    def __init__(self, b_settings, screen):
        """
        初始化碗设置其起始位置
        :param b_settings: 设置信息
        :param screen: 屏幕信息
        """
        super(Bowl, self).__init__()
        self.screen = screen
        self.b_settings = b_settings

        # 加载碗的图像并获取其外接矩形
        self.image = pygame.image.load('images/bowl.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将碗加载在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 存储碗center的准确位置
        self.center = float(self.rect.centerx)

    def blitme(self):
        """
        在指定的位置绘制碗
        :return: None
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整碗的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.b_settings.bowl_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.b_settings.bowl_speed_factor

        # 更新rect对象
        self.rect.centerx = self.center