import pygame

#Instructions:
#Red color = press R
#Green color = press G
#Blue color = press B
#Draw = press D
#Circle = press C
#Square = press S
#Erase = press E
#Exit = press ESC


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # Initial settings
    radius = 15
    drawing = False  # True if the mouse is pressed
    mode = 'draw'  # Can be 'draw', 'circle', 'square', 'erase'
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
                    mode = 'circle'
                elif event.key == pygame.K_s:
                    mode = 'square'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_d:
                    mode = 'draw'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                if event.button == 1:  # Start drawing or resizing
                    start_pos = event.pos
                    if mode in ['circle', 'square']:
                        shapes.append((mode, color, start_pos, radius))
                    elif mode == 'draw':
                        shapes.append(('points', color, [start_pos]))
                elif event.button == 3 and mode in ['circle', 'square']:  # Resize last shape if right-click
                    if shapes:
                        shapes[-1] = (shapes[-1][0], shapes[-1][1], shapes[-1][2], shapes[-1][3] + 5)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing and mode == 'draw':
                # Add point to the last 'points' shape
                if shapes:
                    shape_type, shape_color, points = shapes[-1]
                    if shape_type == 'points':
                        points.append(event.pos)
                        shapes[-1] = (shape_type, shape_color, points)

        screen.fill((0, 0, 0))
        # Draw all shapes
        for shape in shapes:
            if shape[0] == 'circle':
                pygame.draw.circle(screen, shape[1], shape[2], shape[3])
            elif shape[0] == 'square':
                pygame.draw.rect(screen, shape[1], (shape[2][0] - shape[3], shape[2][1] - shape[3], 2 * shape[3], 2 * shape[3]))
            elif shape[0] == 'points':
                for point in shape[2]:
                    pygame.draw.circle(screen, shape[1], point, radius)

        pygame.display.flip()
        clock.tick(60)

main()
