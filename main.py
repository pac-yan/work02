from display import *
from draw import *
import random

#def draw_line( x0, y0, x1, y1, screen, color):

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0,0,500,500, screen, color)
#draw_line(0,0,500,0, screen, color)
draw_line(0,500,500,0, screen, color)
#draw_line(500,0,0,0, screen, color)

draw_line(0,250,500,0, screen, [255,0,0])
draw_line(0,500,250,0, screen, [255,0,0])

draw_line(0,0,500,250, screen, [0,0,255])
draw_line(0,0,250,500, screen, [0,0,255])

draw_line(500,500,250,250, screen, [107,243,120])
draw_line(250,500,500,250, screen, [107,243,120])
draw_line(500,250,250,500, screen, [107,243,120])
draw_line(250,250,500,500, screen, [107,243,120])

draw_line(100,200,200,100, screen, [250,107,46])
draw_line(200,200,100,100, screen, [250,107,46])
draw_line(100,100,200,200, screen, [250,107,46])
draw_line(200,100,100,200, screen, [250,107,46])

display(screen)
save_extension(screen, 'img.png')

