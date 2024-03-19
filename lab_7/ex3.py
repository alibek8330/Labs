import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
title = pygame.display.set_caption("red ball")
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("white")
  pygame.draw.circle(screen, "red", player_pos, 25)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP] and player_pos.y > 30:
    player_pos.y -= 20
  if keys[pygame.K_DOWN] and player_pos.y < 370:
    player_pos.y += 20
  if keys[pygame.K_LEFT] and player_pos.x > 30:
    player_pos.x -= 20
  if keys[pygame.K_RIGHT] and player_pos.x < 470:
    player_pos.x += 20

  pygame.display.flip()
  clock.tick(60)

pygame.quit()