from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math
#control.set_develop_mode()

exp = design.Experiment(name = "Display Edges")
control.initialize(exp)

size=exp.screen.size
l,h=size
t=l/20

s1 = stimuli.Rectangle((t,t), line_width=1,colour=(255,0,0), position=(-(l/2),-(h/2)))
s2 = stimuli.Rectangle((t,t), line_width=1,colour=(255,0,0), position=(-(l/2),(h/2)))
s3 = stimuli.Rectangle((t,t), line_width=1,colour=(255,0,0), position=((l/2),-(h/2)))
s4 = stimuli.Rectangle((t,t), line_width=1, colour=(255,0,0), position=((l/2),(h/2)))

s1.present(clear=True, update=False)
s2.present(clear=False, update=False)
s3.present(clear=False, update=False)
s4.present(clear=False, update=True)

exp.keyboard.wait()
control.end()