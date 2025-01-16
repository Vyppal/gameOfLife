



class ConwayGrid():
  def __init__(self, columnCount, rowCount):
    # generate a 2d boolean array based on specified column and row counts
    self._rowCount: int = rowCount
    self._columnCount: int = columnCount
    self._grid: list[list[bool]] = [[False for i in range(columnCount)] for j in range(rowCount)]
    # Living cells are represented as True in the grid
  

  # accessor method
  def getGrid(self) -> list[list[bool]]:
    return self._grid


  # accessor method
  def getDimensions(self) -> list[int]:
    return [self._columnCount, self._rowCount]


  # Checks whether a specified row and column is within the grid bounds
  def isCoordInGrid(self, column: int, row: int) -> bool:
    if column < 0 or self._columnCount <= column or row < 0 or self._rowCount <= row:
      return False
    return True


  # Gets whether a cell is living
  def checkIfCellLiving(self, column: int, row: int) -> bool:
    if not self.isCoordInGrid(column, row):
      raise f"Cell located at ({column}, {row}) is not in bounds of grid with size ({self._columnCount}, {self._rowCount}). [From checkIfCellLiving]"
    return self._grid[row][column]
    

  def getLivingNeighbourCount(self, cellColumn: int, cellRow: int) -> int:
    # check if out of bounds
    if not self.isCoordInGrid(cellColumn, cellRow):
      raise f"Cell located at ({cellColumn}, {cellRow}) is not in bounds of grid with size ({self._columnCount}, {self._rowCount}). [From getLivingNeighbourCount]"

    # iterate over columns
    livingCount: int = 0
    for columnOffset in range(3):
      columnNum: int = cellColumn - 1 + columnOffset
      # iterate over rows
      for rowOffset in range(3):
        rowNum: int = cellRow - 1 + rowOffset
        
        # ensure the origin cell is not checked
        if [columnNum, rowNum] != [cellColumn, cellRow]:
          # check if tested cell is within grid bounds
          if self.isCoordInGrid(columnNum, rowNum):
            if self.checkIfCellLiving(columnNum, rowNum):
              livingCount += 1
    return livingCount


  def getRuleResults(self, isLiving: bool, liveNeighbourCount: int) -> bool:
    # # Rule 1
    # if isLiving and liveNeighbourCount < 2:
    #   return False
    # # Rule 2
    # if isLiving and liveNeighbourCount in [2, 3]:
    #   return True
    # # Rule 3
    # if isLiving and 3 < liveNeighbourCount:
    #   return False
    # # Rule 4
    # if not isLiving and liveNeighbourCount == 3:
    #   return True

    # Rules 2 and 4
    if liveNeighbourCount == 3:
      return True
    # Rule 2
    if isLiving and liveNeighbourCount == 2:
      return True
    # Rules 1 and 3
    if liveNeighbourCount < 2 or 3 < liveNeighbourCount:
      return False
    
    # Catching dead cell with 2 live neigbours
    if not isLiving and liveNeighbourCount == 2:
      return False
    
    print(f"Warning: Failed to reach a rule result!     Living Neighbour Count: {liveNeighbourCount}     Cell Alive: {isLiving}")
    return False


  def predictNextCellState(self, cellColumn: int, cellRow: int) -> bool:
    # validate cell is in boundary
    if not self.isCoordInGrid(cellColumn, cellRow):
      raise f"Cell located at ({cellColumn}, {cellRow}) is not in bounds of grid with size ({self._columnCount}, {self._rowCount}). [From predictNextCellState]"
    
    liveNeighbourCount: int = self.getLivingNeighbourCount(cellColumn, cellRow)
    # apply rules, and get result
    return self.getRuleResults(self.checkIfCellLiving(cellColumn, cellRow), liveNeighbourCount)


  # makes living and dead cells form a checkerboard pattern
  def DEBUG_checkboardify(self) -> None:
    for row in range(self._rowCount):
      start = row % 2
      for column in range(self._columnCount):
        if start == 0:
          self._grid[row][column] = True
        start = 1 - start


  # Forces a cell to be living
  def forceLiving(self, cellColumn: int, cellRow: int) -> None:
    # validate cell is in boundary
    if not self.isCoordInGrid(cellColumn, cellRow):
      raise f"Cell located at ({cellColumn}, {cellRow}) is not in bounds of grid with size ({self._columnCount}, {self._rowCount}). [From forceLiving]"
    
    print("Logger: forced a cell to be alive at: ", [cellColumn, cellRow])
    self._grid[cellRow][cellColumn] = True


  def DEBUG_print(self) -> None:
    string = ""
    for row in range(self._rowCount):
      for column in range(self._columnCount):
        if self._grid[row][column]:
          string += "#"
        else:
          string += " "
      string += "\n"
    print(string, "-" * self._columnCount)



  # Updates the gamestate to the next frame
  def update(self, debug=False, debugMode=0) -> None:
    if debug:
      match debugMode:
        case 1:
          self.DEBUG_checkboardify()
        case 2:
          self.DEBUG_print()
      return
    
    clonedGrid: list[list[bool]] = [[False for i in range(self._columnCount)] for j in range(self._rowCount)]
    for row in range(self._rowCount):
      for column in range(self._columnCount):
        val = self.predictNextCellState(column, row)
        clonedGrid[row][column] = val
    
    # update the main grid
    self._grid = clonedGrid