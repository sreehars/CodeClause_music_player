import pygame
import os

# initialize pygame
pygame.init()

# set up the window
win = pygame.display.set_mode((400, 400))

# set the title of the window
pygame.display.set_caption("Music Player")

# set up the clock
clock = pygame.time.Clock()

# set up the font
font = pygame.font.SysFont(None, 20)

# get the list of music files in the directory
music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

# initialize the current song index
current_song_index = 0

# load the first song
pygame.mixer.music.load(music_files[current_song_index])

# play the first song
pygame.mixer.music.play()

# main loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # play the previous song
                current_song_index = (current_song_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                # play the next song
                current_song_index = (current_song_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
                
    # update the window
    win.fill((255, 255, 255))
    text = font.render(music_files[current_song_index], True, (0, 0, 0))
    win.blit(text, (10, 10))
    pygame.display.update()

    # limit the frame rate
    clock.tick(60)
