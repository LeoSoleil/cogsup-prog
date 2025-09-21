# labeled_shapes_function.py
from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math
#control.set_develop_mode()


WHITE  = (255, 255, 255)
PURPLE = (160, 32, 240)
YELLOW = (255, 255, 0)

LINE_LEN   = 50   # px
LINE_WIDTH = 3    # px
LABEL_GAP  = 20   # px above the line tip

def make_labeled_regular_polygon(n_sides, side_len, colour, position, label_text):
    shape = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(n_sides, side_len),colour=colour)
    shape.position = position
    shape.preload()  

    top_x, top_y = shape.points_on_screen[2]

    line = stimuli.Line(start_point=(top_x, top_y),end_point=(top_x, top_y + LINE_LEN),line_width=LINE_WIDTH, colour=WHITE)

    label = stimuli.TextLine(label_text,position=(top_x, top_y + LINE_LEN + LABEL_GAP),text_colour=WHITE)
    return shape, line, label


if __name__ == "__main__":
    control.set_develop_mode()
    exp = design.Experiment(name="Labeled (function version)")
    control.initialize(exp)

    # Triangle on the left 
    tri_shape, tri_line, tri_label = make_labeled_regular_polygon(n_sides=3, side_len=50, colour=PURPLE,position=(-100, 0), label_text="triangle")

    #Hexagon on the right
    hex_shape, hex_line, hex_label = make_labeled_regular_polygon(n_sides=6, side_len=25, colour=YELLOW,position=(100, 0), label_text="hexagon")

    control.start()

    # Present (
    tri_shape.present(clear=True, update=False)
    hex_shape.present(clear=False, update=False)
    tri_line.present(clear=False, update=False)
    hex_line.present(clear=False, update=False)
    tri_label.present(clear=False, update=False)
    hex_label.present(clear=False, update=True)

    # Until key press
    exp.keyboard.wait()
    control.end()
