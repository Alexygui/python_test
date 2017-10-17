import pygame
from pygame.sprite import Group

import AlienCraft.game_functions as gf
from AlienCraft.settings import Settings
from AlienCraft.ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    #  开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船状态
        ship.update()
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, aliens, ship, bullets)


run_game()
