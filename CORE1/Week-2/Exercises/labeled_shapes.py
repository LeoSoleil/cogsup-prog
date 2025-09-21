from expyriment import design, control, stimuli
from expyriment.misc import geometry
control.set_develop_mode()

exp = design.Experiment(name = "Labeled")

# Initialize the experiment
control.initialize(exp)

# Create Shapes
t = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(3, 50), colour=(160,32,240))
h= stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(6, 25), colour=(255, 255, 0))
l1=stimuli.Line((-100,20),(-100,70),3,colour=(255,255,255))
l2=stimuli.Line((100,20),(100,70),3,colour=(255,255,255))
t1=stimuli.TextLine("triangle",(-100,90), text_colour=(255,255,255))
t2=stimuli.TextLine("hexagon",(100,90), text_colour=(255,255,255))

#Set positions
t.position=(-100,0)
h.position=(100,0)


control.start(subject_id=1)

# Present 
t.present(clear=True, update=False)
h.present(clear=False, update=False)
l1.present(clear=False,update=False)
l2.present(clear=False,update=False)
t2.present(clear=False,update=False)
t1.present(clear=False,update=True)

# Leave it on-screen for 1,000 ms
exp.clock.wait(500)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()


