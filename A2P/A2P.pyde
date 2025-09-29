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
    size(500,500)
    draw_sudoku_grid()
    drawNum(width/2, height/2, 500)
    
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

def drawNum(x, y, s):
    for i in range(9):
        for j in range(9):
            if board[i][j] != '0':
                text(
                    board[i][j],
                    x - s/2 + s/18 + (j * s/9) - 12,
                    y - s/2 + s/18 + (i * s/9) + 17
                )
