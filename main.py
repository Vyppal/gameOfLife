import pygame
import sys

from conwayGrid import ConwayGrid


# Define useful values
LIVING_COLOUR_RGB = (255, 255, 255)
DEAD_COLOUR_RGB = (0, 0, 0)
SCREEN_SIZE = [2000, 1000]
PIXES_TO_CELL_SCALE_FACTOR = 1

# check if the scale factor allows all pixels to be used
if SCREEN_SIZE[0] % PIXES_TO_CELL_SCALE_FACTOR != 0 or SCREEN_SIZE[1] % PIXES_TO_CELL_SCALE_FACTOR != 0:
  raise f"Mismatched pixel scale factor (of {PIXES_TO_CELL_SCALE_FACTOR}) and screen size (of {SCREEN_SIZE})."


# initialise conway grid
conwayGrid: ConwayGrid = ConwayGrid(int(SCREEN_SIZE[0] / PIXES_TO_CELL_SCALE_FACTOR), int(SCREEN_SIZE[1] / PIXES_TO_CELL_SCALE_FACTOR))

# Set up the display screen
screen = pygame.display.set_mode(SCREEN_SIZE)


def drawGrid(conway: ConwayGrid) -> None:
  conwayDimensions: list[int] = conway.getDimensions()
  
  # clear previous generation screen
  screen.fill(DEAD_COLOUR_RGB)
  
  # draw living cells
  for row in range(conwayDimensions[1]):
    for column in range(conwayDimensions[0]):
      if conway.checkIfCellLiving(column, row):
        pygame.draw.rect(screen, LIVING_COLOUR_RGB, (PIXES_TO_CELL_SCALE_FACTOR * column, PIXES_TO_CELL_SCALE_FACTOR * row, PIXES_TO_CELL_SCALE_FACTOR, PIXES_TO_CELL_SCALE_FACTOR))
  
  # refresh display
  pygame.display.update()



# Handle game loop
while True:
  # check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        conwayGrid.update(debugMode=True)

  drawGrid(conwayGrid)
  
