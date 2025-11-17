from datetime import datetime
from java.io import File
import traceback

sudokuGrid = []
selectedRow = -1
selectedCol = -1
statusMessage = "Status :"
topMargin = 60
menuPosition = "top"

def setup():
    global sudokuGrid
    size(550, 500 + topMargin)
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
    textAlign(CENTER, CENTER)
    loadFile(sudokuGrid, selectedRow, selectedCol, statusMessage)

def draw():
    background(220)
    gameEvent(statusMessage)

    if menuPosition == "top":
        gridX, gridY = 0, topMargin
        gridWidth, gridHeight = width-50, height - topMargin
    elif menuPosition == "bottom":
        gridX, gridY = 0, 0
        gridWidth, gridHeight = width-50, height - topMargin


    highlightSelectedCell(gridX, gridY, gridWidth, gridHeight)
    
    drawNumbers(gridX, gridY, gridWidth, gridHeight)
    
    drawGrid(gridX, gridY, gridWidth, gridHeight)
    
    drawMenu(menuPosition,statusMessage)
    
    drawEmptyInfo(gridX, gridY, gridWidth, gridHeight)

def drawMenu(menuPosition,statusMessage):
    fill(220)
    noStroke()
    
    if menuPosition == "top":
        rect(0, 0, width, topMargin)
        status_y = topMargin*0.75
        mouseY_min = 0
        mouseY_max = topMargin
    elif menuPosition == "bottom":
        rect(0, height - topMargin, width, topMargin)
        status_y = height - topMargin + topMargin*0.25
        mouseY_min = height - topMargin
        mouseY_max = height

    fill(0)
    textAlign(LEFT, CENTER)
    textSize(16)
    text(statusMessage, 10, status_y)

    fill(29,78,216)
    textAlign(RIGHT, CENTER)
    textSize(14)
    saveText = "Save Current State"
    text(saveText, width-10, status_y-10)

    textWidth_save = textWidth(saveText)
    if mouseX > width-10-textWidth_save and mouseX < width-10 and mouseY > mouseY_min and mouseY < mouseY_max:
        stroke(29,78,216)
        strokeWeight(1)
        line(width-10-textWidth_save, status_y-5, width-10, status_y-5)

def highlightSelectedCell(x_start, y_start, grid_width, grid_height):
    if selectedRow >= 0 and selectedCol >= 0:
        fill(150)
        noStroke()
        cellWidth = grid_width / 9.0
        cellHeight = grid_height / 9.0
        rect(x_start + selectedCol*cellWidth, y_start + selectedRow*cellHeight, cellWidth, cellHeight)

def drawNumbers(x_start, y_start, grid_width, grid_height):
    if sudokuGrid and sudokuGrid[0] and sudokuGrid[1]:
        cellWidth = grid_width / 9.0
        cellHeight = grid_height / 9.0
        
        for row in range(9):
            for col in range(9):
                if sudokuGrid[1][row][col]==False:
                    fill(180)
                    noStroke()
                    rect(x_start + col*cellWidth, y_start + row*cellHeight, cellWidth, cellHeight)
                
                val = sudokuGrid[0][row][col]
                
                if val != 0:
                    noStroke()
                    textAlign(CENTER, CENTER)
                    textSize(cellHeight*0.7)
                    
                    if sudokuGrid[1][row][col]==False:
                        fill(0)
                    else:
                        fill(29,78,216)
                    
                    x = x_start + col*cellWidth + cellWidth/2
                    y = y_start + row*cellHeight + cellHeight/2
                    text(str(val), x, y)

def drawGrid(x_start, y_start, grid_width, grid_height):
    stroke(0)
    
    for i in range(1, 9):
        strokeWeight(1)
        line(x_start + i*grid_width/9, y_start, x_start + i*grid_width/9, y_start + grid_height)
        line(x_start, y_start + i*grid_height/9, x_start + grid_width, y_start + i*grid_height/9)
    
    for i in range(1, 3):
        strokeWeight(3)
        line(x_start + i*grid_width/3, y_start, x_start + i*grid_width/3, y_start + grid_height)
        line(x_start, y_start + i*grid_height/3, x_start + grid_width, y_start + i*grid_height/3)
        
    strokeWeight(3.5)
    noFill()
    rect(x_start, y_start, grid_width, grid_height)

def mousePressed():
    global selectedRow, selectedCol, menuPosition

    if menuPosition == "top":
        gridX, gridY = 0, topMargin
        gridWidth, gridHeight = width-50, height - topMargin
    elif menuPosition == "bottom":
        gridX, gridY = 0, 0
        gridWidth, gridHeight = width-50, height - topMargin

    cellWidth = gridWidth / 9.0
    cellHeight = gridHeight / 9.0
    
    selectedCol = int((mouseX - gridX) / cellWidth)
    selectedRow = int((mouseY - gridY) / cellHeight)
    
    if selectedRow < 0 or selectedRow >= 9 or selectedCol < 0 or selectedCol >= 9:
        selectedRow = -1
        selectedCol = -1

    saveText = "Save Current State"
    textWidth_save = textWidth(saveText)
    if (menuPosition == "top" and mouseY < topMargin) or \
       (menuPosition == "bottom" and mouseY > height-topMargin):
        saveFile()

def keyPressed():
    global sudokuGrid, statusMessage
    if selectedRow>=0 and selectedCol>=0:
        if sudokuGrid[1][selectedRow][selectedCol]==True:
            if key>='1' and key<='9':
                if isValidNumber(int(key), selectedRow, selectedCol):
                    sudokuGrid[0][selectedRow][selectedCol]=int(key)
                    statusMessage="Status : Okay :)"
                else:
                    sudokuGrid[0][selectedRow][selectedCol]=int(key)
                    statusMessage="Status : Not Okay :("
            elif key==' ' or keyCode==BACKSPACE or keyCode==DELETE:
                sudokuGrid[0][selectedRow][selectedCol]=0
                statusMessage="Status :"

def isValidNumber(num, row, col):
    for c in range(9):
        if c != col and sudokuGrid[0][row][c] == num:
            return False

    for r in range(9):
        if r != row and sudokuGrid[0][r][col] == num:
            return False

    boxRow = (row // 3) * 3
    boxCol = (col // 3) * 3

    for r in range(boxRow, boxRow + 3):
        for c in range(boxCol, boxCol + 3):
            if (r != row or c != col) and sudokuGrid[0][r][c] == num:
                return False

    return True

def gameEvent(statusMessage):
    
    for r in range(9):
        for c in range(9):
            if sudokuGrid[0][r][c]==0:
                return
    statusMessage="You win!"
    for r in range(9):
        for c in range(9):
            sudokuGrid[1][r][c]=False

def saveFile():
    default_name = datetime.now().strftime("%Y-%m-%d_%H%M%S.sudoku")
    default_file = File(default_name)
    selectOutput("Save Sudoku file:", "saveFileSelected", default_file)

def saveFileSelected(selection):
    global statusMessage
    
    rows = []
    for r in range(9):
        row_str = ",".join(str(sudokuGrid[0][r][c]) for c in range(9))
        rows.append(row_str)
    top = "*".join(rows)

    rows2 = []
    for r in range(9):
        row_str = ",".join("true" if sudokuGrid[1][r][c] else "false" for c in range(9))
        rows2.append(row_str)
    bottom = "*".join(rows2)
    
    try:
        if not selection:
            return
        if hasattr(selection, "getAbsolutePath"):
            path = selection.getAbsolutePath()
        else:
            path = str(selection)
        if not path.lower().endswith(".sudoku"):
            path += ".sudoku"
        content = top + "\n#\n" + bottom
        with open(path, "w") as f:
            f.write(content)
        statusMessage="Save Successful."
    except Exception as e:
        statusMessage="Save Failed."

def loadFile(sudokuGrid, selectedRow, selectedCol, statusMessage):
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
                if cells[c].strip()=="true":
                    sudokuGrid[1][r][c]=True
                else:
                    sudokuGrid[1][r][c]=False
        selectedRow=-1
        selectedCol=-1
        statusMessage="Load Successful."
    except Exception as e:
        statusMessage="Load Failed: "+str(e)
        traceback.print_exc()

def countEmptyCells(row):
    count = 0
    for c in range(9):
        if sudokuGrid[0][row][c] == 0:
            count += 1
    return count

def countEmptyAllRows():
    emptyCounts = []
    for r in range(9):
        emptyCounts.append(countEmptyCells(r))
    return emptyCounts
