from display import *

def draw_line( x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    dy = y1-y0
    dx = x1-x0
    m = dy/dx
    #oct1
    if( m <= 1 and m >= 0):
        d = (2*dy) - dx
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d -= (2*dx)
            x += 1
            d += (2*dy)

    #oct2
    elif( m > 1 ):
        d = dy - (dx*2)
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += (2*dy)
            y += 1
            d -= (2*x)

    #oct7
    elif( m < -1):
        d = dy + (2*dx)
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += (2*dy)
            y -= 1
            d += (2*dx)
    #oct8
    elif( m >= -1 and m < 0):
        d = (2*dy)+dx
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d += (2*dx)
            x += 1
            d += (2*dy)
