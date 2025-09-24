from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math
control.set_develop_mode()

def hermanngrid(row, col, gap, size_s, col_s=(0, 0, 0), col_bg=(255, 255, 255)):
    exp = design.Experiment(name="Hermann-grid", background_colour=col_bg)
    control.initialize(exp)

    total_w=col*size_s+(col-1)*gap
    total_h=row*size_s+(row-1)*gap

    squares = []

    for i in range(row):
        for j in range(col):
            x = j * (size_s + gap) - total_w//2 + size_s//2
            y = i * (size_s + gap) - total_h//2 + size_s//2  
            rect = stimuli.Rectangle((size_s, size_s), colour=col_s, position=(x, y))
            squares.append(rect)

    # present all rectangles
    for a,b in enumerate(squares):
        b.present(clear=(a==0), update=(a==len(squares)-1))

        
    exp.keyboard.wait()
    control.end()

hermanngrid(5, 3, 10, 50)