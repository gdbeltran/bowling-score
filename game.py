from bowl_frame import BowlFrame
from enter import enter_score, enter_ball3

def game():
    frames = [BowlFrame(0, 0) for _ in range(10)]
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
            case 2 | 3 | 4 | 5 | 6 | 7 | 8:
                frame.score = frame.sum()
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                    frames[idx - 2].score += frame.ball1
                elif not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
            case 9:
                frame.score = frame.sum()
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.ball1 + frame.ball2
                    frames[idx - 2].score += frame.ball1
                if not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.ball1 + frame.ball2
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
    total_score = sum(frame.score for frame in frames)
    return total_score