from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import K_1, K_2, K_SPACE,K_LEFT, K_RIGHT,K_UP, K_DOWN
from expyriment.misc.constants import K_l, K_r
import random
control.set_develop_mode()

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["Block", "Trial num","Trial type", "word", "color", "RT", "Accuracy"])
control.initialize(exp)


""" Word """
def make_word(w,c):
    word=stimuli.TextScreen(heading="",text=w, text_colour=c, position=(0,-125), text_size=30)
    word.preload()
    return word

"""Text"""
def text(i):
    text=""
    heading=""
    if(i==0): #welcome
        heading="Welcome to the Stroop experiment!"
        text="Press any key to acess the instructions."
    if(i==1):
        heading="Instructions"
        text="1. Fix the cross\n" \
        "2. If the word matches its color press the right arrow, if not press the left arrow \n\n " \
        "This will repeat 10 times in 2 Blocks\n\n" \
        "Press any key to continue."
    if(i==2):
        heading="Start of block 1 "
        text="Press any key to start."
    if(i==3):
        heading="Start of block 2 \n\n Press any key to start."
        text="Press any key to start."
    if(i==4): #done
        heading="Done!"
    res=stimuli.TextScreen(heading=heading, text=text, heading_bold=True)
    return res

"""Randomiser"""
words=["blue", "red", "green", "magenta"]
colors=[(33, 27, 172),(210, 1, 3),(42, 91, 23),(200, 30, 175)]
def randomiser():
    type=random.randint(0,1)
    #0 match
    #1 mismatch
    if(type==0):
        i = random.randint(0,3)
        w=words[i]
        c=colors[i]
        match=True
    else:
        wi=0
        ci=0
        while(wi==ci):
            wi = random.randint(0,3)
            ci = random.randint(0,3)
        w=words[wi]
        c=colors[ci]
        match=False
    return w,c,match


"""Experiment"""

def run_trial():
    t=text(0)
    t.present(True,True)
    exp.keyboard.wait()

    t=text(1)
    t.present(True, True)
    exp.keyboard.wait()

    #Stimuli
    fixation = stimuli.FixCross(size=(50, 50), line_width=10, position=[0, 0])
    fixation.preload()
    
    
    for i in range(1,3):
        if(i==1):
            t=text(2)
        elif(i==2):
            t=text(3)
        t.present(True, True)
        exp.keyboard.wait()

        for y in range(10):
            print(y)
            fixation.present(True,True)
            exp.clock.wait(500)

            w,c,m=randomiser()
            word=make_word(w,c)

            word.present(True, True)
            key, time=exp.keyboard.wait(keys=[K_LEFT,K_RIGHT])

            corect=False
            if(m==True and key==K_RIGHT): corect=True
            elif(m==False and key==K_LEFT): corect=True
            elif(m==True and key==K_LEFT): corect=False
            elif(m==False and key==K_RIGHT): corect=False

            exp.data.add([i,y,m,w,c,time,corect])
            
    t=text(4)
    t.present(True, True)
    exp.keyboard.wait()
    


control.start()
run_trial()
control.end()
