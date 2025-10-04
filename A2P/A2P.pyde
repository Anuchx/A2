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
