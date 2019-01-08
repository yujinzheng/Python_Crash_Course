#coding=utf-8

import sys
import pygame

class Rufu():

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

def check_keyup_events(event, rufu):
    if event.key == pygame.K_RIGHT:
        rufu.right_flag = False
    elif event.key == pygame.K_LEFT:
        rufu.left_flag = False
    elif event.key == pygame.K_UP:
        rufu.up_flag = False
    elif event.key == pygame.K_DOWN:
        rufu.down_flag = False

def check_keydown_events(event, rufu):
    if event.key == pygame.K_RIGHT:
        rufu.right_flag = True
    elif event.key == pygame.K_LEFT:
        rufu.left_flag = True
    elif event.key == pygame.K_UP:
        rufu.up_flag = True
    elif event.key == pygame.K_DOWN:
        rufu.down_flag = True

def run_game():
    screen = pygame.display.set_mode((1200, 800))
    rufu = Rufu(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, rufu)
            elif event.type == pygame.KEYDOWN:
                # print(event.key)
                check_keydown_events(event, rufu)

        rufu.update()
        screen.fill((205, 56, 16))
        rufu.blitme()
        pygame.display.flip()

run_game()

