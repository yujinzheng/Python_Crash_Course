#coding=utf-8
import sys
import pygame

from rain import Rain

def check_events():
    """
    相应按键和鼠标事件
    :return: None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(r_settings, screen, rains):
    """
    更新屏幕上的图西乡，并切换到新屏幕上
    :param r_settings: 设置类
    :param screen: 屏幕
    :param rains: 雨滴的group
    :return: None
    """
    # 每次循环时重绘屏幕
    screen.fill(r_settings.bg_color)
    rains.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def get_num_rains_x(r_settings, rain_width):
    """
    计算每一行可以容纳多少滴雨
    :param r_settings: 设置
    :param rain_width: 雨滴的宽度
    :return: 雨滴的数量
    """
    available_space_x = r_settings.screen_width - rain_width
    num_rains_x = int(available_space_x/rain_width)
    return num_rains_x

def create_rain(r_settings, screen, rains, rain_number):
    """
    创建一个雨滴并将其放在第一行
    :param r_settings: 设置
    :param screen: 屏幕
    :param rains: 雨滴的group
    :param num_rains_x: 每行雨滴的数量
    :return: None
    """
    rain = Rain(r_settings, screen)
    rain_width = rain.rect.width
    rain.x = rain_width + rain_width * rain_number
    rain.rect.x = rain.x
    rain.rect.y = rain.rect.height
    rains.add(rain)

def create_fleet(r_settings, screen, rains):
    """
    创建一行雨滴
    :param r_settings: 设置
    :param screen: 屏幕
    :param rains: 雨滴group
    :return: None
    """
    # 计算一行能够容纳多少滴雨
    rain = Rain(r_settings, screen)
    number_rains_x = get_num_rains_x(r_settings, rain.rect.width)
    # 创建一行雨滴
    for rain_number in range(number_rains_x):
        create_rain(r_settings, screen, rains, rain_number)

def drop_fleet(r_settings, rains):
    """
    将一行雨滴下移
    :param r_settings: 设置
    :param rains: 雨滴的group
    :return: None
    """
    for rain in rains:
        rain.y += r_settings.rain_drop_speed
        rain.rect.y = rain.y

def check_rain_dispear(r_settings, screen, rains):
    """
    检查雨滴是否消失，如果消失就要新建一行雨滴
    :param r_settings: 设置
    :param screen: 屏幕
    :param rains: 雨滴的group
    :return: None
    """
    for rain in rains:
        print(rain.rect.top)
        if rain.rect.top > r_settings.screen_height:
            create_fleet(r_settings, screen, rains)
            break
        drop_fleet(r_settings, rains)

def update_rains(r_settings, screen, rains):
    """
    检查雨滴是否已经消失
    :param r_settings: 设置
    :param rains: 雨滴的group
    :return: None
    """
    check_rain_dispear(r_settings, screen, rains)
    rains.update()
    for rain in rains.copy():
        if rain.rect.top > r_settings.screen_height:
            rains.remove(rain)