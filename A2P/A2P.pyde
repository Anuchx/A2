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

def setup():
    size(800,800)
    draw_sudoku_board(400, 400, 600)
    drawNum(400, 400, 600)  

def draw_sudoku_board(x, y, w):
    draw_grid(x, y, w)
    frame(x, y, w)

def frame(x, y, w):
    stroke(0)
    strokeWeight(3)
    line(x - w/2, y - w/2, x + w/2, y - w/2)  # up
    line(x - w/2, y + w/2, x + w/2, y + w/2)  # down
    line(x - w/2, y - w/2, x - w/2, y + w/2)  # left
    line(x + w/2, y - w/2, x + w/2, y + w/2)  # right

def draw_grid(x, y, w):
    cell = w / 9.0
    i = 1
    while i < 9:
        if i % 3 == 0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(x - w/2 + i*cell, y - w/2, x - w/2 + i*cell, y + w/2)
        line(x - w/2, y - w/2 + i*cell, x + w/2, y - w/2 + i*cell)

        i += 1

def drawNum(x, y, s):
    cell = s / 9.0
    fill(0)
    textSize(cell * 0.6)  
    textAlign(CENTER, CENTER)
    for i in range(9):
        for j in range(9):
            if board[i][j] != '0':
                text(board[i][j], x - s/2 + s/18 + (j*s/9), y - s/2 + s/18 + (i*s/9))
