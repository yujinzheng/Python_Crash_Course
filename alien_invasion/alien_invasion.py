#coding=utf-8
import sys
import pygame
import game_function as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化Pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()