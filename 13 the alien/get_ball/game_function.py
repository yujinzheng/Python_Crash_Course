#coding=utf-8
import sys
import pygame


from bowl import Bowl
from ball import Ball
from time import sleep

def check_events(bowl):
    """
    相应按键和鼠标事件
    :return: None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, bowl)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, bowl)

def check_keydown_events(event, bowl):
    """相应按键"""
    if event.key == pygame.K_RIGHT:
        bowl.moving_right = True
    elif event.key == pygame.K_LEFT:
        bowl.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, bowl):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        bowl.moving_right = False
    elif event.key == pygame.K_LEFT:
        bowl.moving_left = False

def update_screen(b_settings, screen, bowl, ball):
    """
    更新屏幕上的图像，并切换到新屏幕上
    :param b_settings: 设置类
    :param screen: 屏幕
    :param bowl: 碗
    :param ball: 球
    :return: None
    """
    # 每次循环时重绘屏幕
    screen.fill(b_settings.bg_color)
    ball.blitme()
    bowl.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_ball(b_settings, stats, bowl, ball):
    """更新球的位置"""
    ball.y += b_settings.ball_drop_speed
    ball.update()
    check_ball_dispear(b_settings, stats, ball)
    check_ball_bowl_collisions(bowl, ball)

def check_ball_dispear(b_settings, stats, ball):
    """检查球是否消失，如果消失就要新建一个球"""
    if stats.ball_left > 0:
        if ball.rect.top > b_settings.screen_height:
            stats.ball_left -= 1
            sleep(0.5)
            ball.reset()
    else:
        stats.game_active = False


def check_ball_bowl_collisions(bowl, ball):
    """响应碗和球的碰撞"""
    # 检测到碗和球相交
    if  pygame.Rect.colliderect(ball.rect, bowl.rect):
        sleep(0.5)
        ball.reset()