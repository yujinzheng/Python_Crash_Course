#coding=utf-8

import sys
import pygame
from pygame.sprite import Sprite, Group

class Rufu():
    """路飞类，描述的是路飞图片的动作"""

    def __init__(self, screen):
        """初始化函数"""
        self.screen = screen

        # 加载图片
        self.image = pygame.image.load('images/rufu.bmp')

        # 初始化图片位置
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 上下左右的标志
        self.right_flag = False
        self.left_flag = False
        self.up_flag = False
        self.down_flag = False

    def blitme(self):
        """用于绘制图片"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """用来刷新图片的位置，还需要保证图片不超过边界"""
        if self.right_flag and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.left_flag and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
        if self.up_flag and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        if self.down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

class Bullets(Sprite):
    """子弹类，描述的是子弹的属性"""

    def __init__(self, screen, rufu):
        super(Bullets, self).__init__()
        self.screen = screen

        # 在(0,0)处先创建一个子弹，然后再寻找子弹的位置
        self.rect = pygame.Rect(0, 0, 5, 3)
        self.rect.centery = rufu.rect.centery
        self.rect.left = rufu.rect.left

        # 用小数点存储子弹的位置
        self.x = float(self.rect.x)

        self.color = (0, 0, 0)
        self.speed_factor = 0.01

    def update(self):
        """刷新子弹的位置"""
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上画出子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


def check_keyup_events(event, rufu):
    """检查按键松开的动作"""
    if event.key == pygame.K_RIGHT:
        rufu.right_flag = False
    elif event.key == pygame.K_LEFT:
        rufu.left_flag = False
    elif event.key == pygame.K_UP:
        rufu.up_flag = False
    elif event.key == pygame.K_DOWN:
        rufu.down_flag = False

def check_keydown_events(event, screen, rufu, bullet):
    """检查按键按下的动作"""
    if event.key == pygame.K_RIGHT:
        rufu.right_flag = True
    elif event.key == pygame.K_LEFT:
        rufu.left_flag = True
    elif event.key == pygame.K_UP:
        rufu.up_flag = True
    elif event.key == pygame.K_DOWN:
        rufu.down_flag = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(screen, rufu, bullet)

def update_bullets(bullets):
    """更新子弹信息"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.x <= 0:
            bullets.remove(bullet)

def fire_bullets(screen, rufu, bullets):
    """添加子弹信息"""
    new_bullet = Bullets(screen, rufu)
    bullets.add(new_bullet)

def run_game():
    screen = pygame.display.set_mode((1200, 800))
    rufu = Rufu(screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, rufu)
            elif event.type == pygame.KEYDOWN:
                # print(event.key)
                check_keydown_events(event, screen, rufu, bullets)

        # 刷新屏幕状态
        rufu.update()
        screen.fill((205, 56, 16))
        rufu.blitme()
        update_bullets(bullets)
        for bullet in bullets:
            bullet.draw_bullet()
        pygame.display.flip()

run_game()

