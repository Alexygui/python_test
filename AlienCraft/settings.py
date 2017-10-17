class Settings():
    """保存设置的类"""

    def __init__(self):
        """ 初始化游戏的设置 """

        #  屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # 存储外星人的移动速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction保存移动方向，1表示向右，-1表示向左
        self.fleet_direction = 1
