#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, pygame
from settings import Settings
from ship import Ship
import colorsys

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # 每次循环时都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        screen.fill((230, 230, 0))

        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        pygame.display.update()



run_game()





















