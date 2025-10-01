from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

fixation.present()
t0 = exp.clock.time

exp.clock.wait(1000)

t1 = exp.clock.time #we stop the clock right after the clock so we don't have the processing time of the text presentation
text.present()
fix_duration = (t1 - t0)/1000

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()