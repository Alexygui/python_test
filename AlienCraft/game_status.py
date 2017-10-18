import pygame


class GameStatus():
    """跟踪统计游戏信息"""

    def __init__(self, ai_settings):
        """初始化信息统计"""
        self.ai_settings = ai_settings
        self.reset_status(False)
        self.score = 0
        # 最高分，不可重置
        self.high_score = 0

        # 让游戏一开始出于非活动状态
        self.game_active = False

    def reset_status(self, is_start):
        """初始化游戏进行期间可能变化的统计信息"""
        if is_start:
            self.ship_left = self.ai_settings.ship_limit - 1
        else:
            self.ship_left = self.ai_settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level = 1
