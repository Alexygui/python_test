import sys
import pygame
from AlienCraft.bullet import Bullet
from AlienCraft.alien import Alien


# 相应鼠标和键盘事件
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


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


# 每次循环时都重绘屏幕
def update_screen(ai_settings, screen, aliens, ship, bullets):
    # 重绘制背景
    screen.fill(ai_settings.bg_color)
    # 重新绘制飞船
    ship.blitme()
    # 重新绘制外星人
    aliens.draw(screen)
    # 重绘外星人的位置
    update_aliens(ai_settings, aliens)
    # 重新绘制子弹
    update_bullets(bullets)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


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
        ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """检查外星人是否位于屏幕的边缘，并更新外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
