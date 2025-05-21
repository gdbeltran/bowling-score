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