import numpy as np
import cv2 as cv

WHITE_COLOR = (0,0,0)
BLACK_COLOR = (255, 255, 255)
YELLOW_COLOR = (0, 255, 255)
RED_COLOR = (0, 0, 255)


def create_colored_frame(shape, colors):
    height, width = shape
    frame = np.zeros((height, width, 3), np.uint8)
    
    frame[:,:] = colors

    return frame

def add_text(frame, text, font_color, pos=(50, 50), font=cv.FONT_HERSHEY_SIMPLEX ,font_scale=1, line_type=2):
    text_width, text_height = cv.getTextSize(text, font, font_scale,line_type)[0]
    
    bottom, left, _ = frame.shape

    bottom *= pos[0] / 100
    bottom += text_height / 2

    left *= pos[1] / 100
    left -= text_width / 2

    cv.putText(frame, text, (int(left), int(bottom)), font, font_scale, font_color, line_type)


def create_prime_frame(size):
    frame = create_colored_frame(size, WHITE_COLOR)
    add_text(frame, "Black text here", BLACK_COLOR, (25, 50))

    return frame


def create_fib_frame(size):
    frame = create_colored_frame(size, BLACK_COLOR)
    add_text(frame, "White text here", WHITE_COLOR, (75, 50))

    return frame


def create_fib_prime_frame(size):
    frame = create_colored_frame(size, YELLOW_COLOR)
    add_text(frame, "Red text here", RED_COLOR, (50, 50))

    return frame

