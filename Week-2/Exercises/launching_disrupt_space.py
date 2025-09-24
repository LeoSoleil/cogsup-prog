from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Launch_space")
control.initialize(exp)

square1 = stimuli.Rectangle((50,50), colour=(255,0,0), position=(-400,0))
square2 = stimuli.Rectangle((50,50), colour=(0,255,0))

control.start(subject_id=1)

square1.present(clear=True, update=False)
square2.present(clear=False, update=True)

# Move Red square
for i in range(30):
    square1.move((10,0))
    exp.clock.wait(20)
    square1.present(clear=True, update=False)
    square2.present(clear=False, update=True)

#Introduced a gap the size of 1 square (50px) that still maintains the impression of causality
#Done by going from 35 iterations to 30 in the loop above

# Move Green square
for i in range(30):
    square2.move((10,0))
    exp.clock.wait(20)
    square2.present(clear=True, update=False)
    square1.present(clear=False, update=True)

exp.keyboard.wait()
control.end()