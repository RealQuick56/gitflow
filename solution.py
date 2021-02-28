from moviepy.editor import *
import pygame

pygame.display.set_caption('Видео')

clip = VideoFileClip('images/present.mp4')
clip.preview()

pygame.quit()