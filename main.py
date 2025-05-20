class Frame:
    def __init__(self, ball1, ball2, ball3=0, third_ball=False):
        self.ball1 = ball1
        self.ball2 = ball2
        self.ball3 = ball3
        self.third_ball = third_ball
        self.score = 0

    def sum(self):
        return self.ball1 + self.ball2 + self.ball3

    def is_strike(self):
        return self.ball1 == 10

    def is_spare(self):
        return self.ball1 + self.ball2 == 10 and not self.is_strike()
    
def enter_score(third_ball):
    first = 1
    second = 2
    if third_ball:
        first = 2
        second = 3
    while True:
        try:
            ball1 = int(input(f"Ball {first} pins knocked down (0-10): "))
            if 0 <= ball1 <= 10:
                break
            else:
                print(f"Ball {first} must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
    if ball1 == 10:
        ball2 = 0
    else:
        while True:
            try:
                ball2 = int(input(f"Ball {second} pins knocked down (0-10): "))
                if 0 <= ball2 <= 10 and ball1 + ball2 <= 10:
                    break
                else:
                    print(f"Ball {second} must be between 0 and 10, and total pins in a frame cannot exceed 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 10.")
    return ball1, ball2

def enter_ball3():
    while True:
        try:
            ball3 = int(input("Ball 3 pins knocked down (0-10): "))
            if 0 <= ball3 <= 10:
                break
            else:
                print("Ball 3 must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
    return ball3

def main():
    print("Welcome to the Bowling Score Tracker!")
    frames = [Frame(0, 0) for _ in range(10)]
    for idx, frame in enumerate(frames):
        print(f"Frame {idx + 1}:")
        if idx == 9:
            frame.ball1, frame.ball2 = enter_score(frame.third_ball)
            if frame.is_strike():
                frame.third_ball = True
                frame.ball2, frame.ball3 = enter_score(frame.third_ball)
                if frame.ball2 == 10:
                    frame.ball3 = enter_ball3()
            elif frame.is_spare():
                frame.ball3 = enter_ball3()
                frame.third_ball = True
        else:
            frame.ball1, frame.ball2 = enter_score(frame.third_ball)
        # scoring logic
        match idx:
            case 0:
                frame.score = frame.sum()
            case 1:
                frame.score = frame.sum()
                if frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                print(f"Frame {idx} Score: {frames[idx - 1].score}")
            case 2 | 3 | 4 | 5 | 6 | 7 | 8:
                frame.score = frame.sum()
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                    frames[idx - 2].score += frame.ball1
                elif not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                print(f"Frame {idx - 1} Score: {frames[idx - 2].score}")
                print(f"Frame {idx} Score: {frames[idx - 1].score}")
            case 9:
                frame.score = frame.sum()
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.ball1 + frame.ball2
                    frames[idx - 2].score += frame.ball1
                if not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.ball1 + frame.ball2
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                print(f"Frame {idx - 1} Score: {frames[idx - 2].score}")
                print(f"Frame {idx} Score: {frames[idx - 1].score}")
        print(f"Frame {idx + 1} Score: {frames[idx].score}")
    total_score = sum(frame.score for frame in frames)
    print("Total Score:", total_score)

    return

if __name__ == "__main__":
    main()