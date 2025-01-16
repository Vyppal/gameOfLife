import pygame
import sys

from conwayGrid import ConwayGrid


# Define useful values
LIVING_COLOUR_RGB = (255, 255, 255)
DEAD_COLOUR_RGB = (0, 0, 0)
SCREEN_SIZE = [2000, 1000]
PIXELS_TO_CELL_SCALE_FACTOR = 5

# check if the scale factor allows all pixels to be used
if SCREEN_SIZE[0] % PIXELS_TO_CELL_SCALE_FACTOR != 0 or SCREEN_SIZE[1] % PIXELS_TO_CELL_SCALE_FACTOR != 0:
  raise f"Mismatched pixel scale factor (of {PIXELS_TO_CELL_SCALE_FACTOR}) and screen size (of {SCREEN_SIZE})."


# initialise conway grid
conwayGrid: ConwayGrid = ConwayGrid(int(SCREEN_SIZE[0] / PIXELS_TO_CELL_SCALE_FACTOR), int(SCREEN_SIZE[1] / PIXELS_TO_CELL_SCALE_FACTOR))

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
        pygame.draw.rect(screen, LIVING_COLOUR_RGB, (PIXELS_TO_CELL_SCALE_FACTOR * column, PIXELS_TO_CELL_SCALE_FACTOR * row, PIXELS_TO_CELL_SCALE_FACTOR, PIXELS_TO_CELL_SCALE_FACTOR))
  
  # refresh display
  pygame.display.update()


# converts pixel based coordinates into cell based coordinates
def pixelToCell(pixelColumn: int, pixelRow: int) -> list[int]:
  return [pixelColumn // PIXELS_TO_CELL_SCALE_FACTOR, pixelRow // PIXELS_TO_CELL_SCALE_FACTOR] 


# Handle game loop
while True:
  # check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        conwayGrid.update(debug=False, debugMode=2)
      # if any mouse button is pressed, force the cell to be living
    if event.type == pygame.MOUSEBUTTONDOWN:
      # use of unpack operators to fill parameters
      conwayGrid.forceLiving(*pixelToCell(*pygame.mouse.get_pos()))

  drawGrid(conwayGrid)
  
