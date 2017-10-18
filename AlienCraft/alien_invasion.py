import pygame
from pygame.sprite import Group

import AlienCraft.game_functions as gf
from AlienCraft.settings import Settings
from AlienCraft.ship import Ship
from AlienCraft.game_status import GameStatus
from AlienCraft.button import Button
from AlienCraft.scoreboard import Scoreboard


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
    # 创建用于游戏信息统计的状态实例
    status = GameStatus(ai_settings)
    # 创建按钮实例
    play_button = Button(ai_settings, screen, 'Play')
    # 创建记分牌
    score_board = Scoreboard(ai_settings, screen, status)

    #  开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets, status, play_button, aliens, score_board)

        if status.game_active:
            # 更新飞船状态
            ship.update()
            # 每次循环时都重绘屏幕
            gf.update_screen(ai_settings, screen, aliens, ship, bullets, status, score_board)
        else:
            # 重绘制背景
            screen.fill(ai_settings.bg_color)
            play_button.draw_button()
            score_board.show_score()
            #  让最近绘制的屏幕可见
            pygame.display.flip()


run_game()
