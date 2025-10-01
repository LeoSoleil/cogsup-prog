from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

fixation.present(clear=True, update=True)
#exp.clock.wait(500)
#If we update the presence of the fixation point then wait it's not the same as what we want.
#It gives the impression that the square appears on top of the fixation point and not the fixation point inside the square like we wanted to.  

square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()