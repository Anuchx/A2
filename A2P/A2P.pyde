sudokuGrid = []
selectedRow = -1
selectedCol = -1
statusMessage = "Status :"

def setup():
    global sudokuGrid
    size(500, 600)
    
    sudokuGrid = [
        # grid values
        [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        # editable flags
        [
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True],
            [True,True,True,True,True,True,True,True,True]
        ]
    ]

def draw():
    background(250)
    highlightSelectedCell()
    
    stroke(0)
    strokeWeight(1)
    for i in range(9):
        line((i * width) / 9.0, 0, (i * width) / 9.0, width)
        line(0, (i * width) / 9.0, width, (i * width) / 9.0)

    stroke(0)
    strokeWeight(3)
    line(width / 3.0, 0, width / 3.0, width)
    line((2 * width) / 3.0, 0, (2 * width) / 3.0, width)
    line(0, width / 3.0, width, width / 3.0)
    line(0, (2 * width) / 3.0, width, (2 * width) / 3.0)
    
def mousePressed():
    global selectedRow, selectedCol
    
    cellWidth = width / 9.0
    cellHeight = width / 9.0
    selectedCol = int(mouseX / cellWidth)
    selectedRow = int(mouseY / cellHeight)

    # if the mouse isn't inside the grid, reset the selection
    if selectedRow < 0 or selectedRow >= 9 or selectedCol < 0 or selectedCol >= 9:
        selectedRow = -1
        selectedCol = -1
        
def highlightSelectedCell():
    if selectedRow >= 0 and selectedCol >= 0:
        fill(150)
        noStroke()
        cellWidth = width / 9.0
        cellHeight = width / 9.0
        rect(selectedCol * cellWidth,
             selectedRow * cellHeight,
             cellWidth,
             cellHeight)

def keyPressed():
    global sudokuGrid, selectedRow, selectedCol

    # check if a cell is selected
    if selectedRow >= 0 and selectedCol >= 0:
        # check if the cell is editable
        if sudokuGrid[1][selectedRow][selectedCol] == True:
            if key >= '1' and key <= '9':
                num = int(key)
                sudokuGrid[0][selectedRow][selectedCol] = num
            elif key == ' ' or keyCode == BACKSPACE or keyCode == DELETE:
                sudokuGrid[0][selectedRow][selectedCol] = 0
