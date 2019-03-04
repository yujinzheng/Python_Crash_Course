#coding=utf-8

import sys
import pygame

from bullet import Bullet
from rectangular import Rectangular
from time import sleep

def check_events(ai_settings, screen, stats, ship, rectangulars, bullets, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, rectangulars, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, rectangulars, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, rectangulars, bullets, mouse_x, mouse_y):
    """在玩家单机Play按钮时开始新的游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, screen, stats, ship, rectangulars, bullets)

def update_screen(ai_settings, screen, stats, ship, rectangulars, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for rectangular in rectangulars.sprites():
        rectangular.draw_rectangular()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if  not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def start_game(ai_settings, screen, stats, ship, rectangulars, bullets):
    """用于检测开始游戏"""
    if not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人列表和子弹列表
        rectangulars.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_rectangular(ai_settings, screen, rectangulars)
        ship.center_ship()

def check_keydown_events(event, ai_settings, screen, stats, ship, rectangulars, bullets):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, ship, rectangulars, bullets)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_bullets(ai_settings, screen, stats, rectangulars, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    if stats.ships_left > 0:
        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.right >= ai_settings.screen_width:
                bullets.remove(bullet)
                stats.ships_left -= 1
        check_bullet_rectangular_collisions(ai_settings, screen, rectangulars, bullets)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_bullet_rectangular_collisions(ai_settings, screen, rectangulars, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的外星人和子弹
    collisions = pygame.sprite.groupcollide(bullets, rectangulars, True, True)

    if len(rectangulars) == 0:
        # 删除现有子弹并新建一群外星人
        bullets.empty()
        create_rectangular(ai_settings, screen, rectangulars)
        sleep(0.5)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_rectangular(ai_settings, screen, rectangulars):
    """创建一个矩形"""
    rectangular = Rectangular(ai_settings, screen)
    rectangulars.add(rectangular)

def check_rectangulars_edges(ai_settings, rectangulars):
    """有矩形到达边缘时采取相应的措施"""
    for rectangular in rectangulars.sprites():
        if rectangular.check_edges():
            ai_settings.rectangular_direction *= -1
            break

def update_rectangulars(ai_settings, rectangulars):
    """检查是否有外星人位于边缘并更新整群外星人的位置"""
    check_rectangulars_edges(ai_settings, rectangulars)
    rectangulars.update()