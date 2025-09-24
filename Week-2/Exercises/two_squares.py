from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Square")

# Initialize the experiment
control.initialize(exp)

# Create 
square1 = stimuli.Rectangle((50,50), colour=(255,0,0))
square2 = stimuli.Rectangle((50,50), colour=(0,255,0))

#Set positions
square1.position=(-100,0)
square2.position=(100,0)


control.start(subject_id=1)

# Present 
square1.present(clear=True, update=False)
square2.present(clear=False, update=True)

# Leave it on-screen for 1,000 ms
exp.clock.wait(500)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()