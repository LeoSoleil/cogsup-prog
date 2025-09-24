from expyriment import design, control, stimuli
control.set_develop_mode()

# Initialize the experiment
exp = design.Experiment(name = "Launch_function")
control.initialize(exp)

# Create Stimulis
square1 = stimuli.Rectangle((50,50), colour=(255,0,0), position=(-400,0))
square2 = stimuli.Rectangle((50,50), colour=(0,255,0))

control.start(subject_id=1)

def launch(square1, square2, space=False, time=False, faster=False):
    square1.reposition((-400,0))
    square2.reposition((0,0))
    square1.present(clear=True, update=False)
    square2.present(clear=False, update=True)

    for i in range(30):
        square1.move((10,0))
        exp.clock.wait(20)
        square1.present(clear=True, update=False)
        square2.present(clear=False, update=True)

    if not space:
        square1.move((50,0))
        exp.clock.wait(20)
        square1.present(clear=True, update=False)
        square2.present(clear=False, update=True)
    
    if time:
        exp.clock.wait(2000)

    for i in range(30):
        square2.move((10,0))
        if faster:
            exp.clock.wait(7)
        else:
            exp.clock.wait(20)
        square2.present(clear=True, update=False)
        square1.present(clear=False, update=True)

    exp.keyboard.wait()

launch(square1, square2)
launch(square1, square2, space=True)
launch(square1, square2, time=True)
launch(square1, square2, faster=True)

# End the current session and quit expyriment
control.end()