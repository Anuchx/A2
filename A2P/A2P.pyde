from datetime import datetime
from java.io import File
import traceback

sudokuGrid = []
selectedRow = -1
selectedCol = -1
statusMessage = "Status :"
topMargin = 60

def setup():
    global sudokuGrid
    size(500, 500 + topMargin)
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
    loadFile()

def draw():
    background(220)
    
    gameEvent()
    
    drawMenu()
    
    pushMatrix()
    translate(0, topMargin)
    
    highlightSelectedCell()
    
    drawNumbers()
    
    stroke(0)
    strokeWeight(1)
    for i in range(1, 9):
        x_pos = i * width / 9.0
        line(x_pos, 0, x_pos, width)
        line(0, x_pos, width, x_pos)
        
    stroke(0)
    strokeWeight(3)
    for i in range(1, 3):
        pos = i * width / 3.0
        line(pos, 0, pos, width)
        line(0, pos, width, pos)
        
    popMatrix()

def drawMenu():
    global statusMessage
    fill(220)
    noStroke()
    rect(0, 0, width, topMargin)
    
    fill(0)
    textAlign(LEFT, CENTER)
    textSize(16)
    text(statusMessage, 10, topMargin / 2)
    
    fill(29,78,216)
    textAlign(RIGHT, CENTER)
    textSize(14)
    saveText = "Save Current State"
    text(saveText, width-10, topMargin/2-10)
    
    textWidth_save = textWidth(saveText)
    if (mouseX > width-10-textWidth_save and mouseX < width-10 and
        mouseY > topMargin/2-20 and mouseY < topMargin/2):
        stroke(29,78,216)
        strokeWeight(1)
        line(width-10-textWidth_save, topMargin/2-5, width-10, topMargin/2-5)

def highlightSelectedCell():
    if selectedRow >= 0 and selectedCol >= 0:
        fill(150)
        noStroke()
        cellWidth = width / 9.0
        cellHeight = width / 9.0
        rect(selectedCol*cellWidth, selectedRow*cellHeight, cellWidth, cellHeight)

def drawNumbers():
    if sudokuGrid and sudokuGrid[0] and sudokuGrid[1]:
        cellWidth = width / 9.0
        cellHeight = width / 9.0
        for row in range(9):
            for col in range(9):
                if sudokuGrid[1][row][col]==False:
                    fill(180)
                    noStroke()
                    rect(col*cellWidth,row*cellHeight,cellWidth,cellHeight)
                val = sudokuGrid[0][row][col]
                if val != 0:
                    noStroke()
                    textAlign(CENTER,CENTER)
                    textSize(20)
                    if sudokuGrid[1][row][col]==False:
                        fill(0)
                    else:
                        fill(29,78,216)
                    x = col*cellWidth+cellWidth/2
                    y = row*cellHeight+cellHeight/2
                    text(str(val),x,y)

def mousePressed():
    global selectedRow, selectedCol
    cellWidth = width / 9.0
    cellHeight = width / 9.0
    selectedCol = int(mouseX / cellWidth)
    selectedRow = int((mouseY-topMargin)/cellHeight)
    if selectedRow<0 or selectedRow>=9 or selectedCol<0 or selectedCol>=9:
        selectedRow=-1
        selectedCol=-1
    saveText="Save Current State"
    textWidth_save=textWidth(saveText)
    if (mouseX>width-10-textWidth_save and mouseX<width-10 and
        mouseY>topMargin/2-20 and mouseY<topMargin/2):
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

def gameEvent():
    global statusMessage
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
