import pygame
import os

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((960, 600))
done = False


# Songs
path = r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\songs"
songs = []
for root, dirs, files in os.walk(path):
  for file in files:
    if file.endswith(".mp3"):
      songs.append(os.path.join(root, file))


pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
state = True
background_image = pygame.image.load(r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\bg.png")
background_rect = background_image.get_rect()

while not done:
  background_image = pygame.image.load(r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\bg.png")
  background_rect = background_image.get_rect()
  screen.blit(background_image, background_rect)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        i = (i + 1) % len(songs)
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play()
      elif event.key == pygame.K_LEFT:
        i = (i - 1) % len(songs)
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play()
      elif event.key == pygame.K_SPACE:
        if state:
          pygame.mixer.music.stop()
          state = False
      else:
        pygame.mixer.music.play()
        state = True

    pygame.display.flip()
