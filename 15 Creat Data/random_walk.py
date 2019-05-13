#coding=utf-8

from random import choice

class RandomWalk():
    """一个生成随机漫步数的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有的随机漫步数都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]
        self.direction_choice = [-1, 1]
        self.distance_choice = list(range(0, 5))

    def fill_walk(self):

        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """用于获取运行步长的函数"""
        direction = choice(self.direction_choice)
        distance = choice(self.distance_choice)
        step = direction * distance
        return step