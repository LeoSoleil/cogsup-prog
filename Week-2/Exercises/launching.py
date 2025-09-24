from expyriment import design, control, stimuli
control.set_develop_mode()

# Initialize the experiment
exp = design.Experiment(name = "Launch")
control.initialize(exp)

# Create Stimulis
square1 = stimuli.Rectangle((50,50), colour=(255,0,0), position=(-400,0))
square2 = stimuli.Rectangle((50,50), colour=(0,255,0))

control.start(subject_id=1)

# Present Stimuli at "starting point"
square1.present(clear=True, update=False)
square2.present(clear=False, update=True)

# Move Red square
for i in range(35):
    square1.move((10,0))
    exp.clock.wait(20)
    square1.present(clear=True, update=False)
    square2.present(clear=False, update=True)

# Move Green square
for i in range(30):
    square2.move((10,0))
    exp.clock.wait(20)
    square2.present(clear=True, update=False)
    square1.present(clear=False, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()