def setup():
    size(800,800)
    draw_sudoku_board(400, 400, 600)


def draw_sudoku_board(x, y, w):
    draw_grid(x,y,w)
    frame(x, y, w)


def frame(x, y, w):
    stroke(0)
    strokeWeight(3)
    line(x - w/2, y - w/2, x + w/2, y - w/2)  #up
    line(x - w/2, y + w/2, x + w/2, y + w/2)  #down
    line(x - w/2, y - w/2, x - w/2, y + w/2)  #left
    line(x + w/2, y - w/2, x + w/2, y + w/2)  #right
    

def draw_grid(x, y, w):
    cell = w/9.0
    i = 1
    while i < 9:
        if i % 3 == 0:
            strokeWeight(3) 
        else:
            strokeWeight(1) 

        line(x - w/2 + i*cell, y - w/2, x - w/2 + i*cell, y + w/2) #vertical 
        line(x - w/2, y - w/2 + i*cell, x + w/2, y - w/2 + i*cell) #horizontal

        i += 1
