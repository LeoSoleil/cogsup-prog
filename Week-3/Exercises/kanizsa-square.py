from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math
control.set_develop_mode()

exp = design.Experiment(name = "Kanizsa Square", background_colour=(255, 182, 193))
control.initialize(exp)

size=exp.screen.size
l,h=size
t=l*0.25

s1 = stimuli.Rectangle((t,t), colour=(255, 182, 193))

t2=t/2
c_pos_1=(t2,t2)
c_pos_2=(-t2,t2)
c_pos_3=(t2,-t2)
c_pos_4=(-t2,-t2)

t3=t*0.25
c1 = stimuli.Circle(t3, colour=(0,0,0), position=c_pos_1)
c2 = stimuli.Circle(t3, colour=(0,0,0), position=c_pos_2)
c3 = stimuli.Circle(t3, colour=(255,255,255), position=c_pos_3)
c4 = stimuli.Circle(t3, colour=(255,255,255), position=c_pos_4)

c1.present(clear=True, update=False)
c2.present(clear=False, update=False)
c3.present(clear=False, update=False)
c4.present(clear=False, update=False)
s1.present(clear=False, update=True)











# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
