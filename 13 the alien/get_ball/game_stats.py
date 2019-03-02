#coding=utf-8

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, b_settings):
        """初始化统计信息"""
        self.b_settings = b_settings
        self.reset_stats()
        # 游戏刚启动的时候处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ball_left = self.b_settings.ball_limit