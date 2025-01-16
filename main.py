import pygame
import sys



# Define useful values
SCREEN_SIZE = [3000, 2000]


# Set up the screen
screen = pygame.display.set_mode(SCREEN_SIZE)






# Handle game loop
while True:
  # check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.KEYDOWN:
      ...