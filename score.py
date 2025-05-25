from tkinter import *
from bowl_frame import BowlFrame

def score_frame(frame_number, frames, ball1, ball2, ball3=0):
    frame = BowlFrame(ball1, ball2, ball3)
    idx = frame_number - 1
    match idx:
            case 0:
                frame.score = frame.sum()
                frames[idx].score = frame.score
                frames[idx].running_total = frame.score
            case 1:
                frame.score = frame.sum()
                frames[idx].score = frame.score
                if frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                frames[idx - 1].running_total = frames[idx - 1].score
                frames[idx].running_total = frames[idx - 1].running_total + frame.score
            case 2:
                frame.score = frame.sum()
                frames[idx].score = frame.score
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                    frames[idx - 2].score += frame.ball1
                elif not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                frames[idx - 2].running_total = frames[idx - 2].score
                frames[idx - 1].running_total = frames[idx - 2].running_total + frames[idx - 1].score
                frames[idx].running_total = frames[idx - 1].running_total + frame.score
            case 3 | 4 | 5 | 6 | 7 | 8:
                frame.score = frame.sum()
                frames[idx].score = frame.score
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                    frames[idx - 2].score += frame.ball1
                elif not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.score
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                frames[idx - 2].running_total = frames[idx - 3].running_total + frames[idx - 2].score
                frames[idx - 1].running_total = frames[idx - 2].running_total + frames[idx - 1].score
                frames[idx].running_total = frames[idx - 1].running_total + frame.score                
            case 9:
                frame.score = frame.sum()
                frames[idx].score = frame.score
                if frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.ball1 + frame.ball2
                    frames[idx - 2].score += frame.ball1
                if not frames[idx - 2].is_strike() and frames[idx - 1].is_strike():
                    frames[idx - 1].score += frame.ball1 + frame.ball2
                elif frames[idx - 1].is_spare():
                    frames[idx - 1].score += frame.ball1
                frames[idx - 2].running_total = frames[idx - 3].running_total + frames[idx - 2].score
                frames[idx - 1].running_total = frames[idx - 2].running_total + frames[idx - 1].score
                frames[idx].running_total = frames[idx - 1].running_total + frame.score