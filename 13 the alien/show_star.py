#coding=utf-8
import sys
import pygame

from star import Star
from ship import Ship
from pygame.sprite import Group

class Settings():
    """存储所有设置的类"""
    def __init__(self):
        self.bg_color = (0, 0, 0)
        self.screen_width = 1200
        self.screen_height = 800


def check_events():
    """检查事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def create_fleet(my_settings, screen, stars):
    """创建一组星星"""
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    available_space_x = my_settings.screen_width - 2 * star_width
    available_space_y = my_settings.screen_height - 2 * star_height
    number_star_x = int(available_space_x / (2 * star_width))
    number_star_y = int(available_space_y / (2 * star_height))
    for row_number in range(number_star_y):
        for col_number in range(number_star_x):
            create_star(screen, stars, col_number, row_number)
    
def create_star(screen, stars, col_number, row_number):
    """根据提供的信息，在指定的位置创造星星"""
    star = Star(screen)
    star.rect.x = star.rect.width + col_number * star.rect.width * 2
    star.rect.y = star.rect.height + row_number * star.rect.height * 2
    stars.add(star)


def run_game():
    # 初始化Pygame、设置和屏幕对象
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Show Stars")

    # 创建一颗星星
    stars = Group()

    # 创建星星群
    create_fleet(my_settings, screen, stars)

    # 开始游戏的主循环
    while True:
        check_events()
        screen.fill(my_settings.bg_color)
        stars.draw(screen)
        pygame.display.flip()

run_game()