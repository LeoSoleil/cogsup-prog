from expyriment import design, control, stimuli
import random
control.set_develop_mode()

'''Second version because i realised i was doing unnecessary repositions because of my own perception
of what was going on. Since I initially thought that they were moving together when I saw the example I coded that way.
When I added the colour element I realised that it was only necessary to move one of the circles'''

exp = design.Experiment(name = "Display Edges")
control.initialize(exp)

def run_trial(cr, isi, tag=False):
    t=int(cr*1.5)
    
    #INIT
    if(tag):
        c1 = stimuli.Circle(cr, position=((-3*t), 0), colour=(255,0,0))
        c2 = stimuli.Circle(cr, position=(-t, 0),colour=(255,0,255))
        c3 = stimuli.Circle(cr, position=(+t, 0),colour=(255,255,0))
    else:
        c1 = stimuli.Circle(cr, position=((-3*t), 0))
        c2 = stimuli.Circle(cr, position=(-t, 0))
        c3 = stimuli.Circle(cr, position=(+t, 0))

    c1.present(clear=True, update=False)
    c2.present(clear=False, update=False)
    c3.present(clear=False, update=True)

    for i in range(6):
        exp.clock.wait(isi)
        c1.reposition(((3*t),0))
        c1.present(clear=True, update=False)
        c2.present(clear=False, update=False)
        c3.present(clear=False, update=True)
        
        exp.clock.wait(isi)

        c1.reposition(((-3*t),0))
        c1.present(clear=True, update=False)
        c2.present(clear=False, update=False)
        c3.present(clear=False, update=True)

t1 = stimuli.TextLine("High SIS")
t1.present()
exp.clock.wait(1000)
run_trial(50, 400)

t2 = stimuli.TextLine("Low SIS")
t2.present()
exp.clock.wait(1000)
run_trial(50, 1000)


t3 = stimuli.TextLine("High SIS + Colour")
t3.present()
exp.clock.wait(1000)
run_trial(50, 400,True)

t3 = stimuli.TextLine("Low SIS + Colour")
t3.present()
exp.clock.wait(1000)
run_trial(50, 1000,True)

control.end()