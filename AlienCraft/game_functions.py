import sys
from time import sleep

import pygame
from AlienCraft.bullet import Bullet
from AlienCraft.alien import Alien


# 每次循环时都重绘屏幕
def update_screen(ai_settings, screen, aliens, ship, bullets, status, score_board):
    # 重绘制背景
    screen.fill(ai_settings.bg_color)
    # 显示得分
    score_board.show_score()
    # 重新绘制飞船
    ship.blitme()
    # 重新绘制子弹
    update_bullets(bullets)
    # 更新外星人的位置
    update_aliens(ai_settings, screen, aliens, ship, bullets, status)
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    # 应该在图形绘制结束以后检测碰撞，显得比较真实
    check_collisions(ai_settings, screen, aliens, ship, bullets, status, score_board)


# 相应鼠标和键盘事件
def check_events(ai_settings, screen, ship, bullets, status, play_button, aliens, score_board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, status, play_button, ai_settings, screen, aliens, ship, bullets,
                              score_board)


# 响应按下按键
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_a:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


# 响应松开按键
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """更新子弹的位置，删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 重新绘制所有的子弹
    for bullet in bullets:
        bullet.draw_bullet()


def check_bullet_alien_collisions(bullets, ai_settings, screen, aliens, ship, status, score_board):
    """外星人和子弹的碰撞检测"""
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, ai_settings.bullet_disappear_after_collision, True)
    if collisions:
        for c in collisions.values():
            status.score += ai_settings.alien_points * len(c)
        score_board.prep_score()
        check_high_score(status, score_board)

    if 0 == len(aliens):
        # 删除现有子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        status.level += 1
        score_board.prep_level()

        create_fleet(ai_settings, screen, aliens, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗新的子弹，将其放到编组中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """计算一行可以容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def get_number_row(ai_settings, ship_height, alien_height):
    """计算可以容纳的外形人的行数"""
    available_space_y = (ai_settings.screen_height - (4 * alien_height) - ship_height)
    return int(available_space_y / (2 * alien_height))


def create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_numbers):
    """创建一个外星人并加入当前行"""
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien_height = alien.rect.height
    alien.rect.y = alien_height + 1.5 * alien_height * row_numbers
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    ship_height = ship.rect.height
    row_numbers = get_number_row(ai_settings, ship_height, alien_height)

    for row_number in range(row_numbers):
        # 创建第一行外形人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时应该采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # 此处缩进应与循环体相同，每次改变方向只需要改变一次
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, aliens, ship, bullets, status):
    """检查外星人是否位于屏幕的边缘，并更新外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    # 重新绘制外星人
    aliens.draw(screen)
    # 改变外星人群的移动方向
    aliens.update()


def ship_hit(ai_settings, screen, aliens, ship, bullets, status, score_board):
    """响应被外星人撞到的飞船"""
    if status.ship_left > 0:
        # 将ship_left减1
        status.ship_left -= 1
        score_board.prep_ships()

        print(status.ship_left)

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # 暂停1秒
        sleep(1)
    else:
        status.game_active = False
        pygame.mouse.set_visible(True)


def check_collisions(ai_settings, screen, aliens, ship, bullets, status, score_board):
    """进行碰撞检测"""
    # 子弹和外星人的碰撞检测
    check_bullet_alien_collisions(bullets, ai_settings, screen, aliens, ship, status, score_board)
    # 外星人和飞船的碰撞检测
    check_ship_alien_collision(ai_settings, screen, aliens, ship, bullets, status, score_board)
    # 检查外星人是否到达底部
    check_aliens_bottom(ai_settings, screen, aliens, ship, bullets, status, score_board)


def check_ship_alien_collision(ai_settings, screen, aliens, ship, bullets, status, score_board):
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, aliens, ship, bullets, status, score_board)


def check_aliens_bottom(ai_settings, screen, aliens, ship, bullets, status, score_board):
    """检查外星人是否到达底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像处理外星人撞击飞船一样处理
            ship_hit(ai_settings, screen, aliens, ship, bullets, status, score_board)
            break


def check_play_button(mouse_x, mouse_y, status, play_button, ai_settings, screen, aliens, ship, bullets, score_board):
    """在玩家单击Play按钮时开始新游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not status.game_active:
        # 重置游戏统计信息
        ai_settings.initialize_dynamic_settings()
        status.game_active = True
        status.reset_status(True)

        # 重置记分牌图像
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        score_board.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的的外星人，并且让飞船居中
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # 隐藏光标
        pygame.mouse.set_visible(False)


def check_high_score(status, score_board):
    """检查是否诞生了新的最高分"""
    if status.score > status.high_score:
        status.high_score = status.score
        score_board.prep_high_score()
