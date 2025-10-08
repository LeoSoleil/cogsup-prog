from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import K_1, K_2, K_SPACE,K_LEFT, K_RIGHT,K_UP, K_DOWN
from expyriment.misc.constants import K_l, K_r
""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["Eye", "Key","Radius", "Coordinates-h", "Coordinates-v"])
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

"""Texte"""

def text(i):
    text=""
    heading=""
    if(i==0): #welcome
        heading="Welcome to this blind spot experiment!"
        text="Press space to acess the instructions."
    if(i==1): #circle
        heading="Adjusting size and position of the circle"
        text="Size: \n press 1 to make the circle smaller \n press 2 to make the circle bigger\n\n" \
        "Position: \n you can adjust the placement using the arrows\n\n\n" \
        "Press the space bar to continue onto the experiment and when you are done adjusting the size of the circle."

    if(i==2): #left
        heading="Left Eye"
        text="1. Cover your right eye\n" \
        "2. Fixate the cross with your left eye\n" \
        "3. Adjust the position of the circle as indicated below until you cannot see it\n" \
        "4. Press Space when Done"
    
    if(i==3): #right
        heading="Right Eye"
        text="1. Cover your left eye\n" \
        "2. Fixate the cross with your right eye\n" \
        "3. Adjust the position of the circle as indicated below until you cannot see it\n" \
        "4. Press Space when Done"

    if(i==4): #done
        heading="Done!"
    res=stimuli.TextScreen(heading=heading, text=text)
    return res



""" Experiment """
def run_trial(eye):
    t=text(0)
    t.present(True, True)
    exp.keyboard.wait()

    t=text(1)
    t.present(True, True)
    exp.keyboard.wait()

    if(eye=="left"):
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
        t=text(2)
    elif(eye=="right"):
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[-300, 0])
        t=text(3)

    fixation.preload()
    
    t.present(True,True)
    exp.keyboard.wait()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    key=0
    pos=(0,0)
    while(key!=K_SPACE): #INIT CIRCLE
        key, ti=exp.keyboard.wait(keys=[K_1,K_2,K_SPACE,K_LEFT, K_RIGHT,K_DOWN, K_UP])

        if(key==K_SPACE):
            exit
        elif(key==K_1):
            if(radius-10 > 0):
                radius-=10
        elif(key==K_2):
            if(radius+10 < 300):
                radius+=10

        a,b=pos
        if(key==K_LEFT):
            #add frame restriction
            a-=15
        elif(key==K_RIGHT):
            #add frame restriction
            a+=15
        elif(key==K_UP):
            b+=10
        elif(key==K_DOWN):
            b-=10

        pos=(a,b)
        
        circle=make_circle(radius, pos)
        fixation.present(True, False)
        circle.present(False, True)

        exp.data.add([eye,key, radius, a, b])

    #SUITE DE L'EXPERIENCE 
    
    t=text(4)
    t.present(True, True)

    exp.keyboard.wait()

control.start(subject_id=1)

run_trial("left")
run_trial("right")
    
control.end()