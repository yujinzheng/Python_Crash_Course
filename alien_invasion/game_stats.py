#coding=utf-8

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动的时候处于活动状态
        self.game_active = False

        # 游戏最高得分
        try:
            with open('highscore.txt') as f:
                score = f.read()
                self.high_score = int(score)
        except Exception:
            print("无法获取最高分，将最高分置为0")
            self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1