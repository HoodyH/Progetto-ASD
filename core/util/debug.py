from core.config import *


def debug_lwm(string):
    if debug_en:
        print(string)
    else:
        pass


def debug_time(string):
    if debug_time:
        print(string)
    else:
        pass
