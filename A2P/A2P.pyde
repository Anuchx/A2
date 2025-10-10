import traceback

sudokuGrid = []
selectedRow = -1
selectedCol = -1
statusMessage = "Status :"
topMargin = 60

def setup():
    global sudokuGrid
    size(500, 600)
    
    sudokuGrid = [
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

    loadFile()

def draw():
    background(250)
    fill(0)
    textAlign(LEFT, CENTER)
    textSize(16)
    text(statusMessage, 10, topMargin / 2)
    pushMatrix()
    translate(0, topMargin)
    highlightSelectedCell()
    drawNumbers()
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
    popMatrix()

def mousePressed():
    global selectedRow, selectedCol
    cellWidth = width / 9.0
    cellHeight = width / 9.0
    if mouseY > topMargin and mouseY < topMargin + width:
        selectedCol = int(mouseX / cellWidth)
        selectedRow = int((mouseY - topMargin) / cellHeight)
        if selectedRow < 0 or selectedRow >= 9 or selectedCol < 0 or selectedCol >= 9:
            selectedRow = -1
            selectedCol = -1
    else:
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
    if selectedRow >= 0 and selectedCol >= 0:
        if sudokuGrid[1][selectedRow][selectedCol] == True:
            if key >= '1' and key <= '9':
                num = int(key)
                sudokuGrid[0][selectedRow][selectedCol] = num
            elif key == ' ' or keyCode == BACKSPACE or keyCode == DELETE:
                sudokuGrid[0][selectedRow][selectedCol] = 0

def drawNumbers():
    global sudokuGrid
    if sudokuGrid and sudokuGrid[0] and sudokuGrid[1]:
        cellWidth = width / 9.0
        cellHeight = width / 9.0
        for row in range(9):
            for col in range(9):
                if sudokuGrid[1][row][col] == False:
                    fill(180)
                    noStroke()
                    rect(col * cellWidth,
                         row * cellHeight,
                         cellWidth,
                         cellHeight)
                val = sudokuGrid[0][row][col]
                if val != 0:
                    noStroke()
                    textAlign(CENTER, CENTER)
                    textSize(20)
                    if sudokuGrid[1][row][col] == False:
                        fill(0)
                    else:
                        fill(29, 78, 216)
                    x = (col * width) / 9.0 + width / 18.0
                    y = (row * width) / 9.0 + width / 18.0
                    text(str(val), x, y)

def loadFile():
    global sudokuGrid, selectedRow, selectedCol, statusMessage
    try:
        lines = loadStrings("ex1.sudoku")
        text = "\n".join(lines)
        parts = text.strip().split("\n#\n")
        rows_data = parts[0].strip().split("*")
        for r in range(9):
            cells = rows_data[r].split(",")
            for c in range(9):
                sudokuGrid[0][r][c] = int(cells[c])
        rows_bool = parts[1].strip().split("*")
        for r in range(9):
            cells = rows_bool[r].split(",")
            for c in range(9):
                if cells[c].strip() == "true":
                    sudokuGrid[1][r][c] = True
                else:
                    sudokuGrid[1][r][c] = False
        selectedRow = -1
        selectedCol = -1
        statusMessage = "Load Successful."
    except Exception as e:
        statusMessage = "Load Failed: " + str(e)
        traceback.print_exc()
