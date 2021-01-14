from screeninfo import get_monitors
import operations as op

SIZE = width, height = get_monitors()[0].width, get_monitors()[0].height

SIZEBACKGROUND = op.scaleX(238.88888888888888888888888888889), op.scaleY(211.11111111111111111111111111111)

FPS = 30

SCREENRECT = (0, 0, SIZE[0], SIZE[1])