from threading import Thread
from pydub import AudioSegment
from pydub.playback import play

is_playing = False


def loop_play(sound_file):
    global is_playing
    audio = AudioSegment.from_file(sound_file)
    while is_playing:
        play(audio)


def create_new_thread(func, args=[]):
    thread = Thread(target=func, args=args)
    thread.daemon = True
    thread.start()
    return thread
