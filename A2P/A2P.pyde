board = [
    ['5','3','0','0','7','0','0','0','0'],
    ['6','0','0','1','9','5','0','0','0'],
    ['0','9','8','0','0','0','0','6','0'],
    ['8','0','0','0','6','0','0','0','3'],
    ['4','0','0','8','0','3','0','0','1'],
    ['7','0','0','0','2','0','0','0','6'],
    ['0','6','0','0','0','0','2','8','0'],
    ['0','0','0','4','1','9','0','0','5'],
    ['0','0','0','0','8','0','0','7','9']
]

original_board = []
for i in range(9):
    original_board.append([])
    for j in range(9):
        original_board[i].append(board[i][j])
        
selectedRow = -1
selectedCol = -1


def setup():
    size(500,500)
    textAlign(CENTER, CENTER)
def draw():
    background(255)
    draw_sudoku_grid()
    highlightSelectedCell()
    drawNum()              
    
def draw_sudoku_grid():
    stroke(0)
    strokeWeight(1)
    for i in range(1, 9):
        line((i * width) / 9, 0, (i * width) / 9, height)
        line(0, (i * height) / 9, width, (i * height) / 9)

    stroke(0)
    strokeWeight(3)
    line(width / 3, 0, width / 3, height)
    line((2 * width) / 3, 0, (2 * width) / 3, height)
    line(0, height / 3, width, height / 3)
    line(0, (2 * height) / 3, width, (2 * height) / 3)

def drawNum():
    cellWidth = width / 9
    cellHeight = height / 9
    textSize(cellHeight * 0.65)

    for i in range(9):
        for j in range(9):
            if board[i][j] != '0':
                if original_board[i][j] != '0':
                    fill(0)
                else:
                    fill(0, 0, 255)

                x = j * cellWidth + cellWidth / 2
                y = i * cellHeight + cellHeight / 2
                text(board[i][j], x, y)
                
def highlightSelectedCell():
    if selectedRow >= 0 and selectedCol >= 0:
        fill(173, 216, 230) 
        noStroke()
        cellWidth = width / 9
        cellHeight = height / 9

        hlWidth = cellWidth * 0.75
        hlHeight = cellHeight * 0.75

        x = selectedCol * cellWidth + (cellWidth - hlWidth) / 2
        y = selectedRow * cellHeight + (cellHeight - hlHeight) / 2
        rect(x, y, hlWidth, hlHeight)


def mousePressed():
    global selectedRow, selectedCol
    cellWidth = width / 9
    cellHeight = height / 9
    selectedCol = int(mouseX / cellWidth)
    selectedRow = int(mouseY / cellHeight)
    if selectedCol < 0 or selectedCol >= 9 or selectedRow < 0 or selectedRow >= 9:
        selectedCol = -1
        selectedRow = -1
