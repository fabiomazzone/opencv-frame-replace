from pytube import YouTube
import numpy as np
import cv2 as cv
import generators
from helpers import make_is_in_generator
from cv_utils import create_fib_frame, create_fib_prime_frame, create_prime_frame
import ffmpeg

video_url = "https://youtu.be/uHKfrz65KSU"

def download_video(url, dest='videos'):
    YouTube(url).\
        streams.\
        filter(progressive=True, file_extension='mp4').\
        first().\
        download(output_path=dest)


def iterate_frames(src, dest):
    is_prime = make_is_in_generator(generators.prime_sequence)
    is_fib = make_is_in_generator(generators.fibonacci_sequence)

    video = cv.VideoCapture(src)
    fps = video.get(cv.CAP_PROP_FPS)
    width, height = int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

    writer = cv.VideoWriter(dest, cv.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))

    while(video.isOpened()):
        frame_index = int(video.get(cv.CAP_PROP_POS_FRAMES))
        ret, frame = video.read()

        if(ret):
            if(is_prime(frame_index) and is_fib(frame_index)):
                frame = create_fib_prime_frame((height, width))
            elif(is_prime(frame_index)):
                frame = create_prime_frame((height, width))
            elif(is_fib(frame_index)):
                frame = create_fib_frame((height, width))
            
            writer.write(frame)

        else:
            break

    video.release()
    writer.release()

def add_audio(src_video, src_audio, dest_video):
    input_video = ffmpeg.input(src_video)

    input_audio = ffmpeg.input(src_audio)

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(dest_video).run()



if(__name__ == '__main__'):
    download_video(video_url)
    iterate_frames(
        'videos/Baby Cats - Cute and Funny Cat Videos Compilation 8  Aww Animals.mp4',
        'output/Video1_ohne_Tonspur.mp4'
    )
    add_audio(
        'output/Video1_ohne_Tonspur.mp4',
        'videos/Baby Cats - Cute and Funny Cat Videos Compilation 8  Aww Animals.mp4',
        'output/Video1_editiert.mp4'
    )



    cv.destroyAllWindows()
