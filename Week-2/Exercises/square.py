from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Square")

# Initialize the experiment
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered
square = stimuli.Rectangle((50,50), colour=(0,0,255))


control.start(subject_id=1)

# Present 
square.present(clear=True, update=False)
fixation.present(clear=False, update=True)

# Leave it on-screen for 1,000 ms
exp.clock.wait(500)

# Remove the square
square.present(clear=True, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()