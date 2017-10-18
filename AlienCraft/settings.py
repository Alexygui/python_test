class Settings():
    """保存设置的类"""

    def __init__(self):
        """ 初始化游戏的设置 """

        #  屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 500
        self.bullet_disappear_after_collision = False

        # 存储外星人的移动速度
        self.fleet_drop_speed = 100

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """随着游戏进行而变化的设置"""
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1.4
        self.alien_points = 50

        # fleet_direction保存移动方向，1表示向右，-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度的设置"""
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale

        self.alien_points *= self.score_scale
