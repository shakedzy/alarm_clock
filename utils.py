from datetime import datetime
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play

MAX_WEEK_MINUTE = 59 + 60*23 + 24*60*6

_is_playing = False
_sound_thread = Thread()
_sound_thread.daemon = True


def datetime_to_week_minute(dtime=datetime.now()):
    return dtime.minute + dtime.hour*60 + dtime.weekday()*24*60


def _loop_play(sound_file):
    global _is_playing
    audio = AudioSegment.from_file(sound_file)
    while _is_playing:
        play(audio)
    return None


def play_sound(sound_file):
    global _is_playing
    global _sound_thread
    if not _is_playing:
        _is_playing = True
        _sound_thread = Thread(target=_loop_play,args=[sound_file])
        _sound_thread.daemon = True
        _sound_thread.start()


def stop_sound():
    global _is_playing
    _is_playing = False
