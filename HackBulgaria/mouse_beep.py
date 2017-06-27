import pymouse


def mouse_beep(coords):
    mouse = pymouse.PyMouse()
    yield mouse.position()

