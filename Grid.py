class Grid:
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize

        self.row = []
        for x in range(0, xSize):
            col = []
            for y in range(0, ySize):
                col.append(Cell(x, y, False))
            self.row.append(col)

    def GetCellAtPos(self, x, y):
        return self.row[x][y]

    # Returns a list of all the neighbours of Cell
    def GetNeighbours(self, cell):
        neighbours = []

        for i in range(-1, 2): 
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                elif 0 < cell.x + i < self.xSize and 0 < cell.y + j < self.ySize:
                    neighbours.append(self.GetCellAtPos(cell.x + i, cell.y + j))
        return neighbours

    # Get the amount of alive neighbours of Cell
    def AliveNeighbours(self, cell):
        aliveNeighbours = 0
        for n in self.GetNeighbours(cell):
            if n.isAlive:
                aliveNeighbours +=1
        return aliveNeighbours
    
    # Flip state of Cell
    def ToggleCell(self, cell):
        cell.isAlive = not cell.isAlive
    
    def __str__(self):
        display = ""

        for x in range(0, self.xSize):
            for y in range(0, self.ySize):
                display += str(self.GetCellAtPos(x,y)) + " "
            display += "\n"
            
        return display
    
    # Calculate next iteration of the grid
    def NextIteration(self):

        changeingCells = []
        for x in range(0, self.xSize):
            for y in range(0, self.ySize):

                cell = self.GetCellAtPos(x,y)

                if cell.isAlive:
                    num_alive_neighbors = self.AliveNeighbours(cell)
                    if num_alive_neighbors < 2 or num_alive_neighbors > 3:
                        changeingCells.append(cell)

                else: # cell is dead
                    if self.AliveNeighbours(cell) == 3:
                        changeingCells.append(cell)

        newGrid = self
        for cell in changeingCells:
            self.ToggleCell(cell)


        return newGrid
    
    # returns a list with the alive status of each cell
    def GetGrid(self):
        list = []

        for x in range(0, self.xSize):
            for y in range(0, self.ySize):
                list.append(self.GetCellAtPos(x,y).isAlive)
            
        return list
        


class Cell:
    def __init__(self, x, y, isAlive):
        self.x = x
        self.y = y
        self.isAlive = isAlive

    def __str__(self):
        if(self.isAlive):
            return "1"
        else:
            return "0"



