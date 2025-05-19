class Frame:
    def __init__(self, ball1, ball2):
        self.ball1 = ball1
        self.ball2 = ball2
        self.ball3 = 0
        self.score = 0

    def score(self):
        return self.ball1 + self.ball2

    def is_strike(self):
        return self.ball1 == 10

    def is_spare(self):
        return self.ball1 + self.ball2 == 10 and not self.is_strike()
    
def enter_score():
    while True:
        try:
            ball1 = int(input("Ball 1 pins knocked down (0-10): "))
            if 0 <= ball1 <= 10:
                break
            else:
                print("Ball 1 must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
    if ball1 == 10:
        ball2 = 0
    else:
        while True:
            try:
                ball2 = int(input("Ball 2 pins knocked down (0-10): "))
                if 0 <= ball2 <= 10 and ball1 + ball2 <= 10:
                    break
                else:
                    print("Ball 2 must be between 0 and 10, and total pins in a frame cannot exceed 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 10.")
    return ball1, ball2

def main():
    print("Welcome to the Bowling Score Tracker!")
    frames = []
    counter = 1
    while counter <= 10:
        print(f"Frame {counter}:")
        ball1, ball2 = enter_score()
        frames.append(Frame(ball1, ball2))
        frames[counter - 1].score = ball1 + ball2
        if counter >= 2 and counter < 10:
            if frames[counter - 2].is_spare():
                frames[counter - 2].score += ball1
            if frames[counter - 2].is_strike():
                frames[counter - 2].score += ball1 + ball2
            if counter >= 3:
                
                if counter > 2 and frames[counter - 3].is_strike():
                    frames[counter - 3].score += ball1 + ball2
        if counter == 10:
            if frames[counter -1].is_strike():
                ball2 = int(input("Ball 2 pins knocked down (0-10): "))
                frames[counter - 1].ball2 = ball2
                frames[counter - 1].score += ball2
            if frames[counter - 1].is_spare() or frames[counter -1].is_strike():
                ball3 = int(input("Ball 3 pins knocked down (0-10): "))
                frames[counter - 1].ball3 = ball3
                frames[counter - 1].score += ball3
        if counter >= 3:
            print(f"Frame {counter - 2} Score: {frames[counter - 3].score}")
        if counter >= 2:
            print(f"Frame {counter - 1} Score: {frames[counter - 2].score}")
        print(f"Frame {counter} Score: {frames[counter - 1].score}")
        counter += 1
    total_score = sum(frame.score for frame in frames)
    print("Total Score:", total_score)

    return

if __name__ == "__main__":
    main()