import pygame
from pygame.locals import *
from pygame import mixer
# Instructions:
# Red color = press R
# Green color = press G
# Blue color = press B
# Draw = press D
# Circle = press C
# Square = press S
# Erase = press E
# Exit = press ESC

mixer.init()
pygame.mixer.Sound("sounds\music_background.mp3").play()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    background_color = (255, 255, 255)
    # Initial settings
    radius = 15
    drawing = False  # True if the mouse is pressed
    mode = "draw"  # Can be 'draw', 'circle', 'square', 'erase'
    color = (0, 0, 255)  # Initial color
    shapes = []  # Store drawn shapes and their properties

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                # Change color
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                # Change mode
                elif event.key == pygame.K_c:
                    mode = "circle"
                elif event.key == pygame.K_s:
                    mode = "square"
                elif event.key == pygame.K_e:
                    mode = "erase"
                    drawing = True
                    color = background_color
                elif event.key == pygame.K_d:
                    mode = "draw"

            screen.fill(background_color)

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                if event.button == 1:  # Start drawing or resizing
                    start_pos = event.pos
                    if mode in ["circle", "square"]:
                        shapes.append((mode, color, start_pos, radius))
                    elif mode == "draw":
                        shapes.append(("points", color, [start_pos]))
                elif event.button == 3 and mode in [
                    "circle",
                    "square",
                ]:  # Resize last shape if right-click
                    if shapes:
                        shapes[-1] = (
                            shapes[-1][0],
                            shapes[-1][1],
                            shapes[-1][2],
                            shapes[-1][3] + 5,
                        )

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing and mode == "draw":
                # Add point to the last 'points' shape
                if shapes:
                    shape_type, shape_color, points = shapes[-1]
                    if shape_type == "points":
                        points.append(event.pos)
                        shapes[-1] = (shape_type, shape_color, points)

        screen.fill((255, 255, 255))
        # Draw all shapes
        for shape in shapes:
            if shape[0] == "circle":
                pygame.draw.circle(screen, shape[1], shape[2], shape[3])

            elif shape[0] == 'square':
                square_size = shape[3] * 2
                square_center = shape[2]
                # Create a rect object for the square
                square_rect = pygame.Rect(square_center[0] - shape[3], square_center[1] - shape[3], square_size, square_size)
                pygame.draw.rect(screen, shape[1], square_rect)

            elif shape[0] == "points":
                for point in shape[2]:
                    pygame.draw.circle(screen, shape[1], point, radius)

        pygame.display.flip()
        clock.tick(60)


main()
