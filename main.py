from game import game

def main():
    print("Welcome to the Bowling Score Tracker!")
    print("Game 1:")
    game1 = game()
    print(f"Game 1 score: {game1}")
    print("Game 2:")
    game2 = game()
    print(f"Game 2 score: {game2}")
    print("Game 3:")
    game3 = game()
    print(f"Game 3 score: {game3}")
    series = game1 + game2 + game3
    print(f"Series: {series}")
    average = series / 3
    print(f"Average: {average:.2f}")

    return

if __name__ == "__main__":
    main()