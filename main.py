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
        try:
            ball2 = int(input("Ball 2 pins knocked down (0-10): "))
            if 0 <= ball2 <= 10 and ball1 + ball2 <= 10:
                break
            else:
                print("Ball 2 must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
        
    return ball1, ball2






def main():
    print("Welcome to the Bowling Score Tracker!")
    score = 0
    frames = []
    while len(frames) < 10:
        # frame 1
        ball1, ball2 = enter_score()
        
        
        
        
    return