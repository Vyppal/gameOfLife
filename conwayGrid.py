



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
    if column < 0 or self._columnCount < column or row < 0 or self._rowCount < row:
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
    # Rules 2 and 4
    if liveNeighbourCount == 3:
      return True
    # Rule 2
    if isLiving and liveNeighbourCount == 2:
      return True
    # Rules 1 and 3
    if liveNeighbourCount < 2 or 3 < liveNeighbourCount:
      return False
    
    print("Warning: Failed to reach a rule result!")
    return False


  def predictNextCellState(self, cellColumn: int, cellRow: int) -> bool:
    # validate cell is in boundary
    if not self.isCoordInGrid(cellColumn, cellRow):
      raise f"Cell located at ({cellColumn}, {cellRow}) is not in bounds of grid with size ({self._columnCount}, {self._rowCount}). [From predictNextCellState]"
    
    liveNeighbourCount: int = self.getLivingNeighbourCount(cellColumn, cellRow)
    # apply rules, and get result
    return self.getRuleResults(self.checkIfCellLiving(cellColumn, cellRow), liveNeighbourCount)


  # Updates the gamestate to the next frame
  def update(self) -> None:
    clonedGrid: list[list[bool]] = [[False for i in range(self._columnCount)] for j in range(self._rowCount)]
    for row in range(self._rowCount):
      for column in range(self._columnCount):
        clonedGrid[row][column] == self.predictNextCellState(column, row)
    
    # update the main grid
    self._grid = clonedGrid