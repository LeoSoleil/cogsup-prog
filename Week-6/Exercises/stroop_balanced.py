from expyriment import design, control, stimuli
from expyriment.misc.constants import (
    C_WHITE, C_BLACK,
    C_RED, C_BLUE, C_GREEN,
    K_r, K_b, K_g, K_o, K_SPACE
)
import random
control.set_develop_mode()

C_ORANGE = (255, 165, 0)

""" Task settings """
N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16  # 4 words × 4 color= 16 combos in each block

# Color names and their display colors (corr. ink)
COLOR_CONSTANTS = {
    "red": C_RED,
    "blue": C_BLUE,
    "green": C_GREEN,
    "orange": C_ORANGE,
}

# initials - colors
KEY_TO_COLOR = {
    K_r: "red",
    K_b: "blue",
    K_g: "green",
    K_o: "orange",
}
RESPONSE_KEYS = list(KEY_TO_COLOR.keys())
COLOR_TO_KEY = {v: k for k, v in KEY_TO_COLOR.items()}

""" Instructions """
INSTR_START = """
In this task, decide the COLOR of the word on screen (ignore the meaning of the word).

Press the initial of the ink color:
  R = RED   |   B = BLUE   |   G = GREEN   |   O = ORANGE

Press SPACE to start.
"""

INSTR_MID = """Halfway! Take a short break if needed.
Press SPACE to continue with the next blocks."""

INSTR_END = """All done. Thanks for participating!
Press SPACE to quit."""

FEEDBACK_CORRECT = " Correct "
FEEDBACK_INCORRECT = " Incorrect "

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(max(0, t - dt))

def wait_space_with_legend(text):
    screen = stimuli.TextScreen(heading="Instructions", text=text, text_justification=0)
    screen.present()
    exp.keyboard.wait([K_SPACE])

def present_response_legend():
    legend = stimuli.TextScreen(
        heading="Response Keys",
        text=("Press the initial of the INK COLOR (ignore the word):\n\n"
              "R = RED      B = BLUE      G = GREEN      O = ORANGE"),
        text_justification=0
    )
    legend.present()
    exp.keyboard.wait([K_SPACE])

""" Experiment setup """
exp = design.Experiment(
    name="Stroop (Balanced Color Identification, Initials R/B/G/O)",
    background_colour=C_WHITE,
    foreground_colour=C_BLACK
)
exp.add_data_variable_names([
    'block', 'trial_in_block', 'word', 'ink_color', 'congruency', 'key', 'RT', 'correct'
])

control.set_develop_mode()  # comment out for real data collection
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

WORDS = list(COLOR_CONSTANTS.keys())
INKS = list(COLOR_CONSTANTS.keys())

TEXT_STIMS = {
    w: {c: stimuli.TextLine(w, text_colour=COLOR_CONSTANTS[c]) for c in INKS}
    for w in WORDS
}
load([TEXT_STIMS[w][c] for w in WORDS for c in INKS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Trial logic """
def run_trial(block_id, trial_id, word, ink_color):
    congruent = int(word == ink_color)

    present_for(fixation, t=500)
    TEXT_STIMS[word][ink_color].present()

    key, rt = exp.keyboard.wait(RESPONSE_KEYS)
    pressed_color = KEY_TO_COLOR[key]
    correct = int(pressed_color == ink_color)

    exp.data.add([
        block_id, trial_id, word, ink_color,
        ("congruent" if congruent else "incongruent"),
        key, rt, correct
    ])

    present_for(feedback_correct if correct else feedback_incorrect, t=600)

def make_block_trials():
    # balanced: all 16 word-ink combinations appear 1 time in the block
    trials = [(w, c) for w in WORDS for c in INKS]
    random.shuffle(trials)
    return trials

""" Run """
control.start(subject_id=1)

wait_space_with_legend(INSTR_START)

for block_id in range(1, N_BLOCKS + 1):
    #Reminder
    present_response_legend()

    trials = make_block_trials()  # remake balanced block
    for trial_id, (word, ink_color) in enumerate(trials, start=1):
        run_trial(block_id, trial_id, word, ink_color)

    if block_id == (N_BLOCKS // 2):
        wait_space_with_legend(INSTR_MID)

wait_space_with_legend(INSTR_END)
control.end()
