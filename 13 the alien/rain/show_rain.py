#coding=utf-8
import sys
import pygame
import game_function as gf

from settings import Settings
from pygame.sprite import Group

def show_rain():
    # 初始化Pygame、设置和屏幕对象
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode((r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("rains dropping")

    # 创建雨滴编组
    rains = Group()

    # 创建一行雨滴
    gf.create_fleet(r_settings, screen, rains)

    # 开始主循环
    while True:
        gf.check_events()
        gf.update_screen(r_settings, screen, rains)
        gf.update_rains(r_settings, screen, rains)

show_rain()