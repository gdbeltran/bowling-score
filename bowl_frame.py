class BowlFrame:
    def __init__(self, ball1, ball2, ball3=0, third_ball=False):
        self.ball1 = ball1
        self.ball2 = ball2
        self.ball3 = ball3
        self.third_ball = third_ball
        self.score = 0
        self.running_total = 0

    def sum(self):
        return self.ball1 + self.ball2 + self.ball3

    def is_strike(self):
        return self.ball1 == 10

    def is_spare(self):
        return self.ball1 + self.ball2 == 10 and not self.is_strike()