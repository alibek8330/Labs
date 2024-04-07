import pygame

eraser = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

pygame.display.set_caption("Paint")


def main():
    radius = 15
    mode = black
    last_pos = None
    draw = "line"

    while True:
     # handle events
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and draw == "line":
            # start a new line
            last_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION and event.buttons[0] and draw == "line":
            # draw a line from the last point to the current point  
            if last_pos is not None:
                start_pos = last_pos
                end_pos = pygame.mouse.get_pos()
                drawLineBetween(screen, start_pos, end_pos, radius, mode)
                last_pos = end_pos

        if(draw == "rect" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
        if(draw == "square" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            drawSquare(screen, pygame.mouse.get_pos(), 100, 100, mode)
        if(draw == "circle" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            drawCircle(screen, pygame.mouse.get_pos(), mode)
        if(draw == "etrien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            drawRightTriangle(screen, mode, pygame.mouse.get_pos())
        if(draw == "trien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            drawEquilateralTriangle(screen, mode, pygame.mouse.get_pos())
        if(draw == "rhombus" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            drawRhombus(screen, mode, pygame.mouse.get_pos())

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_b]:
            mode = black
        if pressed[pygame.K_g]:
            mode = green
        if pressed[pygame.K_k]:
            mode = blue
        if pressed[pygame.K_y]:
            mode = yellow
        if pressed[pygame.K_r]:
            mode = red
        if pressed[pygame.K_e]:
            mode = eraser
        if pressed[pygame.K_0]:
            draw = "line"
        if pressed[pygame.K_1]:
            draw = "rect"
        if pressed[pygame.K_2]:
            draw = "square"
        if pressed[pygame.K_3]:
            draw = "circle"
        if pressed[pygame.K_4]:
            draw = "etrien"
        if pressed[pygame.K_5]:
            draw = "trien"
        if pressed[pygame.K_6]:
            draw = "rhombus"


        pygame.display.flip()
        clock.tick(60)
    

def drawLineBetween(screen, start, end, width, color_mode):
    
     color = color_mode
     dx = start[0] - end[0]
     dy = start[1] - end[1]
     iterations = max(abs(dx), abs(dy))
    
     for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, mouse_pos, w, h, color):
     x = mouse_pos[0]
     y = mouse_pos[1]
     rect = pygame.Rect(x, y, w, h)
     pygame.draw.rect(screen, color, rect, 3) # 4th parameter is outline of the rectangle

def drawCircle(screen, mouse_pos, color):
     x = mouse_pos[0]
     y = mouse_pos[1]
     pygame.draw.circle(screen, color, (x, y), 100, 100) # 4th parameter is outline of the rectangle

def drawSquare(screen, mouse_pos, w, h, color):
     x = mouse_pos[0]
     y = mouse_pos[1]
     rect = pygame.Rect(x, y, w, h)
     pygame.draw.rect(screen, color, rect, 3) # 4th parameter is outline of the square

def drawRightTriangle(screen, color, mouse_pos):
     x = mouse_pos[0]
     y = mouse_pos[1]
     triangle_size = 50

     triangle_points = [
     (x, y - triangle_size),
     (x - triangle_size, y + triangle_size),
     (x + triangle_size, y + triangle_size),
     ]

     pygame.draw.polygon(screen, color, triangle_points)

def drawEquilateralTriangle(screen, color, mouse_pos):
     x = mouse_pos[0]
     y = mouse_pos[1]
     triangle_size = 50

     triangle_points = [
     (x, y - triangle_size - 100),
     (x - triangle_size, y + triangle_size),
     (x + triangle_size, y + triangle_size),
     ]

     pygame.draw.polygon(screen, color, triangle_points) 

def drawRhombus(screen, color, mouse_pos):
     x = mouse_pos[0]
     y = mouse_pos[1]
     rhombus_height = 50
     rhombus_width = 50
     rhombus_points = [
     (x, y - rhombus_height),
     (x + rhombus_width, y),
     (x, y + rhombus_height),
     (x - rhombus_width , y),
     ]
     pygame.draw.polygon(screen, color, rhombus_points)


main()