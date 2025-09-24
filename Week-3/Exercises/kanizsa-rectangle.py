from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math
control.set_develop_mode()

exp = design.Experiment(name = "Kanizsa Rectangle", background_colour=(255, 182, 193))
control.initialize(exp)


def kanizsa(ar, scale_r, scale_c):
    
    l,h=ar
    rl=l*scale_r
    rh=h*scale_r

    s1 = stimuli.Rectangle((rl,rh), colour=(255, 182, 193))

    rl2=rl/2
    rh2=rh/2
    c_pos_1=(rl2,rh2)
    c_pos_2=(-rl2,rh2)
    c_pos_3=(rl2,-rh2)
    c_pos_4=(-rl2,-rh2)

    t3=rh*scale_c
    c1 = stimuli.Circle(t3, colour=(0,0,0), position=c_pos_1)
    c2 = stimuli.Circle(t3, colour=(0,0,0), position=c_pos_2)
    c3 = stimuli.Circle(t3, colour=(255,255,255), position=c_pos_3)
    c4 = stimuli.Circle(t3, colour=(255,255,255), position=c_pos_4)

    c1.present(clear=True, update=False)
    c2.present(clear=False, update=False)
    c3.present(clear=False, update=False)
    c4.present(clear=False, update=False)
    s1.present(clear=False, update=True)

#kanizsa(exp.screen.size, 0.5, 0.5)
#kanizsa(exp.screen.size, 0.3, 0.3)
kanizsa(exp.screen.size, 0.25, 0.5)

exp.keyboard.wait()
control.end()