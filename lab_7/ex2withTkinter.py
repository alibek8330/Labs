import pygame
from tkinter import *
from tkinter import ttk
from pygame import mixer
import os

#ВНИМАНИЕ
#КОД ПОКА В РАЗРАБОТКЕ
#АЛЬТЕРНАТИВНЫЙ И ЗАКОНЧЕННЫЙ КОД НА ПАЙГЕЙМЕ - ex2-pygame.py


pygame.mixer.init()
pygame.init()

# Songs
path = r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\songs"
songs = []
for root, dirs, files in os.walk(path):
  for file in files:
    if file.endswith(".mp3"):
      songs.append(os.path.join(root, file))


# Функции кнопок
current_song = 0
played = False

def play_song():
  global current_song
  global played
  if played == False:
    # Загрузка и воспроизведение песни, если она еще не играла
    mixer.music.load(songs[current_song])
    mixer.music.play()
    played = True
  if played == True:
    # Пауза или возобновление воспроизведения, если песня уже играла
    if mixer.music.get_busy():  # Проверка, играет ли музыка в данный момент
      mixer.music.pause()  # Пауза, если музыка играет
    else:
      mixer.music.unpause()  # Возобновление, если музыка на паузе


def next_song():
  global current_song
  current_song = (current_song + 1) % len(songs)
  play_song()

def previous_song():
  global current_song
  current_song = (current_song - 1) % len(songs)
  play_song()

# def update_status():
#   # Код для обновления статуса плеера или интерфейса
#   print("Обновление статуса")
#   root.after(1000, update_status)  # Вызов функции снова через 1000 мс (1 секунда)
#   for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_RIGHT:
#         next_song()
#       if event.key == pygame.K_LEFT:
#         previous_song()
#       if event.key == pygame.K_SPACE:
#         pause_song()

# Настройка скелета интерфейса используя Ткинтер
root = Tk()
root.title("MelodyStream")
root.geometry("400x350+568+257")

icon = PhotoImage(file=r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\icon_player.png")
root.iconphoto(False, icon)

root.minsize(400, 350)
root.maxsize(400, 350)
#Icons
background = PhotoImage(file=r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\background.png") 

label1 = Label(root, image = background) 
label1.place(x = 0, y = 0) 
play_icon = PhotoImage(file=r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\play_cut.png")
pause_icon = PhotoImage(file=r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\pause_cut.png")
next_icon = PhotoImage(file=r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\next_cut.png")
previous_icon = PhotoImage(file=r"C:\Users\Алибек\Desktop\repositories\labs\lab_7\images\previous_cut.png")
# Создание фрейма для кнопок
buttons_frame = ttk.Frame(root)
buttons_frame.pack(side='bottom', pady=20) 

# Создание кнопок
left_btn = ttk.Button(buttons_frame, image=previous_icon, command=previous_song)
left_btn.pack(side='left', padx=10, )  # padx добавляет пространство между кнопками
left_btn = Label(image=previous_icon)

play_btn = ttk.Button(buttons_frame, image=play_icon, command=play_song)
play_btn.pack(side='left', padx=10)  # Установка этой кнопки между двумя другими

right_btn = ttk.Button(buttons_frame, image=next_icon, command=next_song)
right_btn.pack(side='left', padx=10)



root.mainloop()
