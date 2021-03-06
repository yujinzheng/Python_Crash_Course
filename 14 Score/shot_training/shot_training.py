#coding=utf-8
import sys
import pygame
import game_function as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化Pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shot Training")

    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    rectangulars = Group()
    bullets = Group()

    # 创建矩阵群
    gf.create_rectangular(ai_settings, screen, rectangulars)

    # 创建一个用来存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, ship, rectangulars, bullets, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, rectangulars, bullets)
            gf.update_rectangulars(ai_settings, rectangulars)
        gf.update_screen(ai_settings, screen, stats, ship, rectangulars, bullets, play_button)

run_game()