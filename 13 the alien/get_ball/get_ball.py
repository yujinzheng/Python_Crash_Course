#coding=utf-8
import sys
import pygame
import game_function as gf

from bowl import Bowl
from ball import Ball
from settings import Settings
from game_stats import GameStats

def get_ball():
    # 初始化Pygame、设置和屏幕对象
    pygame.init()
    b_settings = Settings()
    screen = pygame.display.set_mode((b_settings.screen_width, b_settings.screen_height))
    pygame.display.set_caption("get ball")

    # 创建一个球和一个碗
    bowl = Bowl(b_settings, screen)
    ball = Ball(b_settings, screen)
    stats = GameStats(b_settings)

    # 开始主循环
    while True:
        gf.check_events(bowl)
        if stats.game_active:
            bowl.update()
            gf.update_ball(b_settings, stats, bowl, ball)
        gf.update_screen(b_settings, screen, bowl, ball)


get_ball()