#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on October 29, 2019, at 14:33
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'PrisonersdilemmaToneRillingTrialRun'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\khali\\Documents\\GitHub\\Prisoners-Dilemma\\Prisoners-Dilemma\\prisonersdilemmatask\\PrisonersdilemmaToneRillingTrialRun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "gamevariables"
gamevariablesClock = core.Clock()
#Python Modules
import random, time, math


#set the seed for the experiment
newSeed = int(math.modf(time.time())[1])
random.seed(newSeed)


# decision list
decision = ["c","d"]

#outcomes list (should be 20 for each game)
outcomes = []

#rounds
rounds = 1

#player earnings
player1_earnings = 0
player2_earnings = 0

#number of cooperation and defections for player 1
num_coop_player1 = 0
num_def_player1 = 0

#Phase Contingency loops
doAntiCoop1 = 0
doAntiCoop2 = 0
doAntiCoop3 = 0
doAntiCoop4 = 0
doAntiCoop5 = 0
doAntiDef1 = 0
doAntiDef2 = 0
doAntiDef3 = 0
doAntiDef4 = 0
doAntiDef5 = 0
doFeedCC = 0
doFeedCD = 0
doFeedDC = 0
doFeedDD = 0

#Anticipation Contigency loop list options
anticoop = ["AntiCoop1","AntiCoop2","AntiCoop3","AntiCoop4","AntiCoop5"]
antidef = ["AntiDef1","AntiDef2","AntiDef3","AntiDef4","AntiDef5"]

#Seed number
thisExp.addData("seed_number",newSeed)

# Initialize components for Routine "WelcomeScreen1"
WelcomeScreen1Clock = core.Clock()
background1 = visual.Rect(
    win=win, name='background1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instructions1 = visual.TextStim(win=win, name='instructions1',
    text='\nWelcome to the Prisoners Dilemma Game!\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp1 = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen2"
WelcomeScreen2Clock = core.Clock()
background2 = visual.Rect(
    win=win, name='background2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='\n\n\nYou must decide whether you want to cooperate or not cooperate with your partner.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp2 = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen3"
WelcomeScreen3Clock = core.Clock()
background3 = visual.Rect(
    win=win, name='background3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instructions3 = visual.TextStim(win=win, name='instructions3',
    text='\nDuring gameplay, you will press C to cooperate and D to not cooperate.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp3 = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen4"
WelcomeScreen4Clock = core.Clock()
background4 = visual.Rect(
    win=win, name='background4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instructions4 = visual.TextStim(win=win, name='instructions4',
    text="The combination of your and the other player's decisions will determine how much money you get after each round.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp4 = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen5"
WelcomeScreen5Clock = core.Clock()
background5 = visual.Rect(
    win=win, name='background5',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instructions5 = visual.TextStim(win=win, name='instructions5',
    text='\n\nYou will now play 5 practice rounds with the computer so you can learn how the game works.\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp5 = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen6"
WelcomeScreen6Clock = core.Clock()
background6 = visual.Rect(
    win=win, name='background6',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instructions6 = visual.TextStim(win=win, name='instructions6',
    text="Let's Begin!",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp6 = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
wait1 = visual.Rect(
    win=win, name='wait1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "WaitforPartner"
WaitforPartnerClock = core.Clock()
partnerbackground = visual.Rect(
    win=win, name='partnerbackground',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
partnerassign = visual.TextStim(win=win, name='partnerassign',
    text='Wait for your partner!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
wait1 = visual.Rect(
    win=win, name='wait1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Decision"
DecisionClock = core.Clock()
Decision_Screen1 = visual.ImageStim(
    win=win,
    name='Decision_Screen1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
currentround = visual.TextStim(win=win, name='currentround',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player1_earningsdec = visual.TextStim(win=win, name='player1_earningsdec',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
player2_earningsdec = visual.TextStim(win=win, name='player2_earningsdec',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
phaseinstruct = visual.TextStim(win=win, name='phaseinstruct',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
phaseinstruct1_2 = visual.TextStim(win=win, name='phaseinstruct1_2',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_decision = keyboard.Keyboard()

# Initialize components for Routine "AntiCoop1"
AntiCoop1Clock = core.Clock()
AntiCoopImage = visual.ImageStim(
    win=win,
    name='AntiCoopImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround1 = visual.TextStim(win=win, name='currentround1',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsanticoop = visual.TextStim(win=win, name='player1_earningsanticoop',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsanticoop = visual.TextStim(win=win, name='player2_earningsanticoop',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct2 = visual.TextStim(win=win, name='phaseinstruct2',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiCoop2"
AntiCoop2Clock = core.Clock()
AntiCoopImage_2 = visual.ImageStim(
    win=win,
    name='AntiCoopImage_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround_2 = visual.TextStim(win=win, name='currentround_2',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsanticoop_2 = visual.TextStim(win=win, name='player1_earningsanticoop_2',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsanticoop_2 = visual.TextStim(win=win, name='player2_earningsanticoop_2',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct3 = visual.TextStim(win=win, name='phaseinstruct3',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiCoop3"
AntiCoop3Clock = core.Clock()
AntiCoopImage_3 = visual.ImageStim(
    win=win,
    name='AntiCoopImage_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround_3 = visual.TextStim(win=win, name='currentround_3',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsanticoop_3 = visual.TextStim(win=win, name='player1_earningsanticoop_3',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsanticoop_3 = visual.TextStim(win=win, name='player2_earningsanticoop_3',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct4 = visual.TextStim(win=win, name='phaseinstruct4',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiCoop4"
AntiCoop4Clock = core.Clock()
AntiCoopImage_4 = visual.ImageStim(
    win=win,
    name='AntiCoopImage_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround_4 = visual.TextStim(win=win, name='currentround_4',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsanticoop_4 = visual.TextStim(win=win, name='player1_earningsanticoop_4',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsanticoop_4 = visual.TextStim(win=win, name='player2_earningsanticoop_4',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct5 = visual.TextStim(win=win, name='phaseinstruct5',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiCoop5"
AntiCoop5Clock = core.Clock()
AntiCoopImage_5 = visual.ImageStim(
    win=win,
    name='AntiCoopImage_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround_5 = visual.TextStim(win=win, name='currentround_5',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsanticoop_5 = visual.TextStim(win=win, name='player1_earningsanticoop_5',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsanticoop_5 = visual.TextStim(win=win, name='player2_earningsanticoop_5',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct6 = visual.TextStim(win=win, name='phaseinstruct6',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiDef1"
AntiDef1Clock = core.Clock()
AntiDefImage = visual.ImageStim(
    win=win,
    name='AntiDefImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround3 = visual.TextStim(win=win, name='currentround3',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsantidef = visual.TextStim(win=win, name='player1_earningsantidef',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsantidef = visual.TextStim(win=win, name='player2_earningsantidef',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct7 = visual.TextStim(win=win, name='phaseinstruct7',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiDef2"
AntiDef2Clock = core.Clock()
AntiDefImage_2 = visual.ImageStim(
    win=win,
    name='AntiDefImage_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround3_2 = visual.TextStim(win=win, name='currentround3_2',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsantidef_2 = visual.TextStim(win=win, name='player1_earningsantidef_2',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsantidef_2 = visual.TextStim(win=win, name='player2_earningsantidef_2',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct8 = visual.TextStim(win=win, name='phaseinstruct8',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiDef3"
AntiDef3Clock = core.Clock()
AntiDefImage_3 = visual.ImageStim(
    win=win,
    name='AntiDefImage_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround3_3 = visual.TextStim(win=win, name='currentround3_3',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsantidef_3 = visual.TextStim(win=win, name='player1_earningsantidef_3',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsantidef_3 = visual.TextStim(win=win, name='player2_earningsantidef_3',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct9 = visual.TextStim(win=win, name='phaseinstruct9',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiDef4"
AntiDef4Clock = core.Clock()
AntiDefImage_4 = visual.ImageStim(
    win=win,
    name='AntiDefImage_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround3_4 = visual.TextStim(win=win, name='currentround3_4',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsantidef_4 = visual.TextStim(win=win, name='player1_earningsantidef_4',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsantidef_4 = visual.TextStim(win=win, name='player2_earningsantidef_4',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct10 = visual.TextStim(win=win, name='phaseinstruct10',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "AntiDef5"
AntiDef5Clock = core.Clock()
AntiDefImage_5 = visual.ImageStim(
    win=win,
    name='AntiDefImage_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
currentround3_5 = visual.TextStim(win=win, name='currentround3_5',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
player1_earningsantidef_5 = visual.TextStim(win=win, name='player1_earningsantidef_5',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player2_earningsantidef_5 = visual.TextStim(win=win, name='player2_earningsantidef_5',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
phaseinstruct11 = visual.TextStim(win=win, name='phaseinstruct11',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "FeedCC"
FeedCCClock = core.Clock()
FeedCCimage = visual.ImageStim(
    win=win,
    name='FeedCCimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
currentround4 = visual.TextStim(win=win, name='currentround4',
    text='default text',
    font='Arial',
    pos=(0,.4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player1_earningsfeedCC = visual.TextStim(win=win, name='player1_earningsfeedCC',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
player2_earningsfeedCC = visual.TextStim(win=win, name='player2_earningsfeedCC',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
phaseinstruct12 = visual.TextStim(win=win, name='phaseinstruct12',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "FeedCD"
FeedCDClock = core.Clock()
FeedCDimage = visual.ImageStim(
    win=win,
    name='FeedCDimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
currentround5 = visual.TextStim(win=win, name='currentround5',
    text='default text',
    font='Arial',
    pos=(0,.4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player1_earningsfeedCD = visual.TextStim(win=win, name='player1_earningsfeedCD',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
player2_earningsfeedCD = visual.TextStim(win=win, name='player2_earningsfeedCD',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
phaseinstruct13 = visual.TextStim(win=win, name='phaseinstruct13',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "FeedDC"
FeedDCClock = core.Clock()
FeedDCimage = visual.ImageStim(
    win=win,
    name='FeedDCimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
currentround6 = visual.TextStim(win=win, name='currentround6',
    text='default text',
    font='Arial',
    pos=(0,.4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player1_earningsfeedDC = visual.TextStim(win=win, name='player1_earningsfeedDC',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
player2_earningsfeedDC = visual.TextStim(win=win, name='player2_earningsfeedDC',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
phaseinstruct14 = visual.TextStim(win=win, name='phaseinstruct14',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "FeedDD"
FeedDDClock = core.Clock()
FeedDDimage = visual.ImageStim(
    win=win,
    name='FeedDDimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
currentround7 = visual.TextStim(win=win, name='currentround7',
    text='default text',
    font='Arial',
    pos=(0,.4), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
player1_earningsfeedDD = visual.TextStim(win=win, name='player1_earningsfeedDD',
    text='default text',
    font='Arial',
    pos=(-.55,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
player2_earningsfeedDD = visual.TextStim(win=win, name='player2_earningsfeedDD',
    text='default text',
    font='Arial',
    pos=(.64,.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
phaseinstruct15 = visual.TextStim(win=win, name='phaseinstruct15',
    text='default text',
    font='Arial',
    pos=(0.025,.3), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "roundcount"
roundcountClock = core.Clock()

# Initialize components for Routine "blank"
blankClock = core.Clock()
wait1 = visual.Rect(
    win=win, name='wait1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "blank"
blankClock = core.Clock()
wait1 = visual.Rect(
    win=win, name='wait1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "CompleteScreen"
CompleteScreenClock = core.Clock()
background7 = visual.Rect(
    win=win, name='background7',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
playagain = visual.TextStim(win=win, name='playagain',
    text='Thank you for your participation! \n\nPlease see the researcher for debriefing.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "gamevariables"-------
# update component parameters for each repeat
# keep track of which components have finished
gamevariablesComponents = []
for thisComponent in gamevariablesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gamevariablesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "gamevariables"-------
while continueRoutine:
    # get current time
    t = gamevariablesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gamevariablesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gamevariablesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "gamevariables"-------
for thisComponent in gamevariablesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "gamevariables" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen1"-------
# update component parameters for each repeat
key_resp1.keys = []
key_resp1.rt = []
# keep track of which components have finished
WelcomeScreen1Components = [background1, instructions1, key_resp1]
for thisComponent in WelcomeScreen1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreen1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen1"-------
while continueRoutine:
    # get current time
    t = WelcomeScreen1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreen1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background1* updates
    if background1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background1.frameNStart = frameN  # exact frame index
        background1.tStart = t  # local t and not account for scr refresh
        background1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background1, 'tStartRefresh')  # time at next scr refresh
        background1.setAutoDraw(True)
    
    # *instructions1* updates
    if instructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions1.frameNStart = frameN  # exact frame index
        instructions1.tStart = t  # local t and not account for scr refresh
        instructions1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1, 'tStartRefresh')  # time at next scr refresh
        instructions1.setAutoDraw(True)
    
    # *key_resp1* updates
    waitOnFlip = False
    if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp1.frameNStart = frameN  # exact frame index
        key_resp1.tStart = t  # local t and not account for scr refresh
        key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
        key_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp1.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp1.keys = theseKeys.name  # just the last key pressed
            key_resp1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen1"-------
for thisComponent in WelcomeScreen1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions1.started', instructions1.tStartRefresh)
thisExp.addData('instructions1.stopped', instructions1.tStopRefresh)
# check responses
if key_resp1.keys in ['', [], None]:  # No response was made
    key_resp1.keys = None
thisExp.addData('key_resp1.keys',key_resp1.keys)
if key_resp1.keys != None:  # we had a response
    thisExp.addData('key_resp1.rt', key_resp1.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen2"-------
# update component parameters for each repeat
key_resp2.keys = []
key_resp2.rt = []
# keep track of which components have finished
WelcomeScreen2Components = [background2, instructions2, key_resp2]
for thisComponent in WelcomeScreen2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreen2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen2"-------
while continueRoutine:
    # get current time
    t = WelcomeScreen2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreen2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background2* updates
    if background2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background2.frameNStart = frameN  # exact frame index
        background2.tStart = t  # local t and not account for scr refresh
        background2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background2, 'tStartRefresh')  # time at next scr refresh
        background2.setAutoDraw(True)
    
    # *instructions2* updates
    if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.tStart = t  # local t and not account for scr refresh
        instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2, 'tStartRefresh')  # time at next scr refresh
        instructions2.setAutoDraw(True)
    
    # *key_resp2* updates
    waitOnFlip = False
    if key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp2.frameNStart = frameN  # exact frame index
        key_resp2.tStart = t  # local t and not account for scr refresh
        key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
        key_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp2.keys = theseKeys.name  # just the last key pressed
            key_resp2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen2"-------
for thisComponent in WelcomeScreen2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp2.keys in ['', [], None]:  # No response was made
    key_resp2.keys = None
thisExp.addData('key_resp2.keys',key_resp2.keys)
if key_resp2.keys != None:  # we had a response
    thisExp.addData('key_resp2.rt', key_resp2.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen3"-------
# update component parameters for each repeat
key_resp3.keys = []
key_resp3.rt = []
# keep track of which components have finished
WelcomeScreen3Components = [background3, instructions3, key_resp3]
for thisComponent in WelcomeScreen3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreen3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen3"-------
while continueRoutine:
    # get current time
    t = WelcomeScreen3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreen3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background3* updates
    if background3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background3.frameNStart = frameN  # exact frame index
        background3.tStart = t  # local t and not account for scr refresh
        background3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background3, 'tStartRefresh')  # time at next scr refresh
        background3.setAutoDraw(True)
    
    # *instructions3* updates
    if instructions3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3.frameNStart = frameN  # exact frame index
        instructions3.tStart = t  # local t and not account for scr refresh
        instructions3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3, 'tStartRefresh')  # time at next scr refresh
        instructions3.setAutoDraw(True)
    
    # *key_resp3* updates
    waitOnFlip = False
    if key_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp3.frameNStart = frameN  # exact frame index
        key_resp3.tStart = t  # local t and not account for scr refresh
        key_resp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp3, 'tStartRefresh')  # time at next scr refresh
        key_resp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp3.keys = theseKeys.name  # just the last key pressed
            key_resp3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen3"-------
for thisComponent in WelcomeScreen3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp3.keys in ['', [], None]:  # No response was made
    key_resp3.keys = None
thisExp.addData('key_resp3.keys',key_resp3.keys)
if key_resp3.keys != None:  # we had a response
    thisExp.addData('key_resp3.rt', key_resp3.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen4"-------
# update component parameters for each repeat
key_resp4.keys = []
key_resp4.rt = []
# keep track of which components have finished
WelcomeScreen4Components = [background4, instructions4, key_resp4]
for thisComponent in WelcomeScreen4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreen4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen4"-------
while continueRoutine:
    # get current time
    t = WelcomeScreen4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreen4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background4* updates
    if background4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background4.frameNStart = frameN  # exact frame index
        background4.tStart = t  # local t and not account for scr refresh
        background4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background4, 'tStartRefresh')  # time at next scr refresh
        background4.setAutoDraw(True)
    
    # *instructions4* updates
    if instructions4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions4.frameNStart = frameN  # exact frame index
        instructions4.tStart = t  # local t and not account for scr refresh
        instructions4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions4, 'tStartRefresh')  # time at next scr refresh
        instructions4.setAutoDraw(True)
    
    # *key_resp4* updates
    waitOnFlip = False
    if key_resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp4.frameNStart = frameN  # exact frame index
        key_resp4.tStart = t  # local t and not account for scr refresh
        key_resp4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp4, 'tStartRefresh')  # time at next scr refresh
        key_resp4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp4.keys = theseKeys.name  # just the last key pressed
            key_resp4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen4"-------
for thisComponent in WelcomeScreen4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp4.keys in ['', [], None]:  # No response was made
    key_resp4.keys = None
thisExp.addData('key_resp4.keys',key_resp4.keys)
if key_resp4.keys != None:  # we had a response
    thisExp.addData('key_resp4.rt', key_resp4.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen5"-------
# update component parameters for each repeat
key_resp5.keys = []
key_resp5.rt = []
# keep track of which components have finished
WelcomeScreen5Components = [background5, instructions5, key_resp5]
for thisComponent in WelcomeScreen5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreen5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen5"-------
while continueRoutine:
    # get current time
    t = WelcomeScreen5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreen5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background5* updates
    if background5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background5.frameNStart = frameN  # exact frame index
        background5.tStart = t  # local t and not account for scr refresh
        background5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background5, 'tStartRefresh')  # time at next scr refresh
        background5.setAutoDraw(True)
    
    # *instructions5* updates
    if instructions5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions5.frameNStart = frameN  # exact frame index
        instructions5.tStart = t  # local t and not account for scr refresh
        instructions5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions5, 'tStartRefresh')  # time at next scr refresh
        instructions5.setAutoDraw(True)
    
    # *key_resp5* updates
    waitOnFlip = False
    if key_resp5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp5.frameNStart = frameN  # exact frame index
        key_resp5.tStart = t  # local t and not account for scr refresh
        key_resp5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp5, 'tStartRefresh')  # time at next scr refresh
        key_resp5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp5.keys = theseKeys.name  # just the last key pressed
            key_resp5.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen5"-------
for thisComponent in WelcomeScreen5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp5.keys in ['', [], None]:  # No response was made
    key_resp5.keys = None
thisExp.addData('key_resp5.keys',key_resp5.keys)
if key_resp5.keys != None:  # we had a response
    thisExp.addData('key_resp5.rt', key_resp5.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen6"-------
# update component parameters for each repeat
key_resp6.keys = []
key_resp6.rt = []
# keep track of which components have finished
WelcomeScreen6Components = [background6, instructions6, key_resp6]
for thisComponent in WelcomeScreen6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreen6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen6"-------
while continueRoutine:
    # get current time
    t = WelcomeScreen6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreen6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background6* updates
    if background6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background6.frameNStart = frameN  # exact frame index
        background6.tStart = t  # local t and not account for scr refresh
        background6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background6, 'tStartRefresh')  # time at next scr refresh
        background6.setAutoDraw(True)
    
    # *instructions6* updates
    if instructions6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions6.frameNStart = frameN  # exact frame index
        instructions6.tStart = t  # local t and not account for scr refresh
        instructions6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions6, 'tStartRefresh')  # time at next scr refresh
        instructions6.setAutoDraw(True)
    
    # *key_resp6* updates
    waitOnFlip = False
    if key_resp6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp6.frameNStart = frameN  # exact frame index
        key_resp6.tStart = t  # local t and not account for scr refresh
        key_resp6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp6, 'tStartRefresh')  # time at next scr refresh
        key_resp6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp6.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp6.keys = theseKeys.name  # just the last key pressed
            key_resp6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen6"-------
for thisComponent in WelcomeScreen6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions6.started', instructions6.tStartRefresh)
thisExp.addData('instructions6.stopped', instructions6.tStopRefresh)
# check responses
if key_resp6.keys in ['', [], None]:  # No response was made
    key_resp6.keys = None
thisExp.addData('key_resp6.keys',key_resp6.keys)
if key_resp6.keys != None:  # we had a response
    thisExp.addData('key_resp6.rt', key_resp6.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [wait1]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait1* updates
    if wait1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait1.frameNStart = frameN  # exact frame index
        wait1.tStart = t  # local t and not account for scr refresh
        wait1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait1, 'tStartRefresh')  # time at next scr refresh
        wait1.setAutoDraw(True)
    if wait1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait1.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            wait1.tStop = t  # not accounting for scr refresh
            wait1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(wait1, 'tStopRefresh')  # time at next scr refresh
            wait1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "WaitforPartner"-------
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
WaitforPartnerComponents = [partnerbackground, partnerassign]
for thisComponent in WaitforPartnerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitforPartnerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WaitforPartner"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WaitforPartnerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitforPartnerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *partnerbackground* updates
    if partnerbackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partnerbackground.frameNStart = frameN  # exact frame index
        partnerbackground.tStart = t  # local t and not account for scr refresh
        partnerbackground.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partnerbackground, 'tStartRefresh')  # time at next scr refresh
        partnerbackground.setAutoDraw(True)
    if partnerbackground.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > partnerbackground.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            partnerbackground.tStop = t  # not accounting for scr refresh
            partnerbackground.frameNStop = frameN  # exact frame index
            win.timeOnFlip(partnerbackground, 'tStopRefresh')  # time at next scr refresh
            partnerbackground.setAutoDraw(False)
    
    # *partnerassign* updates
    if partnerassign.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partnerassign.frameNStart = frameN  # exact frame index
        partnerassign.tStart = t  # local t and not account for scr refresh
        partnerassign.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partnerassign, 'tStartRefresh')  # time at next scr refresh
        partnerassign.setAutoDraw(True)
    if partnerassign.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > partnerassign.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            partnerassign.tStop = t  # not accounting for scr refresh
            partnerassign.frameNStop = frameN  # exact frame index
            win.timeOnFlip(partnerassign, 'tStopRefresh')  # time at next scr refresh
            partnerassign.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitforPartnerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitforPartner"-------
for thisComponent in WaitforPartnerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('partnerbackground.started', partnerbackground.tStartRefresh)
thisExp.addData('partnerbackground.stopped', partnerbackground.tStopRefresh)
thisExp.addData('partnerassign.started', partnerassign.tStartRefresh)
thisExp.addData('partnerassign.stopped', partnerassign.tStopRefresh)

# ------Prepare to start Routine "blank"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [wait1]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait1* updates
    if wait1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait1.frameNStart = frameN  # exact frame index
        wait1.tStart = t  # local t and not account for scr refresh
        wait1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait1, 'tStartRefresh')  # time at next scr refresh
        wait1.setAutoDraw(True)
    if wait1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait1.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            wait1.tStop = t  # not accounting for scr refresh
            wait1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(wait1, 'tStopRefresh')  # time at next scr refresh
            wait1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
gameloop = data.TrialHandler(nReps=9999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='0'),
    seed=None, name='gameloop')
thisExp.addLoop(gameloop)  # add the loop to the experiment
thisGameloop = gameloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGameloop.rgb)
if thisGameloop != None:
    for paramName in thisGameloop:
        exec('{} = thisGameloop[paramName]'.format(paramName))

for thisGameloop in gameloop:
    currentLoop = gameloop
    # abbreviate parameter names if possible (e.g. rgb = thisGameloop.rgb)
    if thisGameloop != None:
        for paramName in thisGameloop:
            exec('{} = thisGameloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Decision"-------
    # update component parameters for each repeat
    #round check
    if rounds == 5:
        gameloop.finished = True
    
    
    #players
    player1 = " "
    player2 = " "
    outcomesExc = " "
    
    #number assignment for computer cooperation probablility
    compcoop = round(random.uniform(0,100))
    
    #data to be added to excel sheet
    thisExp.addData("round_number",rounds)
    
    
    
    
    Decision_Screen1.setImage(PhaseContingency)
    currentround.setColor('black', colorSpace='rgb')
    currentround.setText(rounds)
    player1_earningsdec.setColor('black', colorSpace='rgb')
    player1_earningsdec.setText(player1_earnings)
    player2_earningsdec.setColor('black', colorSpace='rgb')
    player2_earningsdec.setText(player2_earnings)
    phaseinstruct.setColor('black', colorSpace='rgb')
    phaseinstruct.setText('Choose cooperate (C) or not cooperate (D)')
    phaseinstruct1_2.setColor('red', colorSpace='rgb')
    phaseinstruct1_2.setText('Please make your decision (C or D)')
    key_decision.keys = []
    key_decision.rt = []
    # keep track of which components have finished
    DecisionComponents = [Decision_Screen1, currentround, player1_earningsdec, player2_earningsdec, phaseinstruct, phaseinstruct1_2, key_decision]
    for thisComponent in DecisionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DecisionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Decision"-------
    while continueRoutine:
        # get current time
        t = DecisionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DecisionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Decision_Screen1* updates
        if Decision_Screen1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Decision_Screen1.frameNStart = frameN  # exact frame index
            Decision_Screen1.tStart = t  # local t and not account for scr refresh
            Decision_Screen1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Decision_Screen1, 'tStartRefresh')  # time at next scr refresh
            Decision_Screen1.setAutoDraw(True)
        
        # *currentround* updates
        if currentround.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            currentround.frameNStart = frameN  # exact frame index
            currentround.tStart = t  # local t and not account for scr refresh
            currentround.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(currentround, 'tStartRefresh')  # time at next scr refresh
            currentround.setAutoDraw(True)
        
        # *player1_earningsdec* updates
        if player1_earningsdec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player1_earningsdec.frameNStart = frameN  # exact frame index
            player1_earningsdec.tStart = t  # local t and not account for scr refresh
            player1_earningsdec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player1_earningsdec, 'tStartRefresh')  # time at next scr refresh
            player1_earningsdec.setAutoDraw(True)
        
        # *player2_earningsdec* updates
        if player2_earningsdec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            player2_earningsdec.frameNStart = frameN  # exact frame index
            player2_earningsdec.tStart = t  # local t and not account for scr refresh
            player2_earningsdec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(player2_earningsdec, 'tStartRefresh')  # time at next scr refresh
            player2_earningsdec.setAutoDraw(True)
        
        # *phaseinstruct* updates
        if phaseinstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            phaseinstruct.frameNStart = frameN  # exact frame index
            phaseinstruct.tStart = t  # local t and not account for scr refresh
            phaseinstruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(phaseinstruct, 'tStartRefresh')  # time at next scr refresh
            phaseinstruct.setAutoDraw(True)
        if phaseinstruct.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > phaseinstruct.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                phaseinstruct.tStop = t  # not accounting for scr refresh
                phaseinstruct.frameNStop = frameN  # exact frame index
                win.timeOnFlip(phaseinstruct, 'tStopRefresh')  # time at next scr refresh
                phaseinstruct.setAutoDraw(False)
        
        # *phaseinstruct1_2* updates
        if phaseinstruct1_2.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            phaseinstruct1_2.frameNStart = frameN  # exact frame index
            phaseinstruct1_2.tStart = t  # local t and not account for scr refresh
            phaseinstruct1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(phaseinstruct1_2, 'tStartRefresh')  # time at next scr refresh
            phaseinstruct1_2.setAutoDraw(True)
        
        # *key_decision* updates
        waitOnFlip = False
        if key_decision.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_decision.frameNStart = frameN  # exact frame index
            key_decision.tStart = t  # local t and not account for scr refresh
            key_decision.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_decision, 'tStartRefresh')  # time at next scr refresh
            key_decision.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_decision.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_decision.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_decision.status == STARTED and not waitOnFlip:
            theseKeys = key_decision.getKeys(keyList=['c', 'd'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_decision.keys = theseKeys.name  # just the last key pressed
                key_decision.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DecisionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Decision"-------
    for thisComponent in DecisionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if rounds == 1:
        player2 = "c"
    if rounds == 2:
        if outcomes == ["cc"]:
            if compcoop <= 93:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes == ["dc"]:
            if compcoop <= 36:
                player2 = "c"
            else:
                player2 = "d"
    if 3 <= rounds <= 10:
        if outcomes[-2:] == ["cc","cc"]:
            if compcoop <= 92:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","cc"]:
            if compcoop <= 86:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","cc"]:
            if compcoop <= 78:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","cc"]:
            if compcoop <= 50:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cc","cd"]:
            if compcoop <= 58:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","cd"]:
            if compcoop <= 0:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","cd"]:
            if compcoop <= 33:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","cd"]:
            if compcoop <= 33:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cc","dc"]:
            if compcoop <= 86:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","dc"]:
            if compcoop <= 80:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","dc"]:
            if compcoop <= 33:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","dc"]:
            if compcoop <= 20:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cc","dd"]:
            if compcoop <= 50:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","dd"]:
            if compcoop <= 38:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","dd"]:
            if compcoop <= 50:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","dd"]:
            if compcoop <= 43:
                player2 = "c"
            else:
                player2 = "d"
    if 11 <= rounds <= 18:
        if outcomes[-2:] == ["cc","cc"]:
            if compcoop <= 92:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","cc"]:
            if compcoop <= 90:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","cc"]:
            if compcoop <= 100:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","cc"]:
            if compcoop <= 60:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cc","cd"]:
            if compcoop <= 13:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","cd"]:
            if compcoop <= 20:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","cd"]:
            if compcoop <= 67:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","cd"]:
            if compcoop <= 33:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cc","dc"]:
            if compcoop <= 83:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","dc"]:
            if compcoop <= 63:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","dc"]:
            if compcoop <= 0:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","dc"]:
            if compcoop <= 33:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cc","dd"]:
            if compcoop <= 33:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["cd","dd"]:
            if compcoop <= 8:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dc","dd"]:
            if compcoop <= 50:
                player2 = "c"
            else:
                player2 = "d"
        elif outcomes[-2:] == ["dd","dd"]:
            if compcoop <= 25:
                player2 = "c"
            else:
                player2 = "d"
    if 5 <= rounds <= 18:
        if outcomes[-4:] == ["cc","cc","cc","cc"]:
            player2 = "d"
    if rounds > 18:
        player2 = "d"
    
    if key_decision.keys == 'c':
        player1 = 'c'
        anti1 = random.choice(anticoop)
        if anti1 == "AntiCoop1":
            doAntiCoop1 = 1
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti1 == "AntiCoop2":
            doAntiCoop1 = 0
            doAntiCoop2 = 1
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti1 == "AntiCoop3":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 1
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti1 == "AntiCoop4":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 1
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti1 == "AntiCoop5":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 1
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
    
        if player1 == "c" and player2 == "c":
            doFeedCC = 1
            doFeedCD = 0
            doFeedDC = 0
            doFeedDD = 0
            num_coop_player1 += 1
            outcomes += ["cc"]
            outcomesExc = "cc"
        if player1 == "c" and player2 == "d":
            doFeedCC = 0
            doFeedCD = 1
            doFeedDC = 0
            doFeedDD = 0
            num_coop_player1 += 1
            outcomes += ["cd"]
            outcomesExc = "cd"
    
    elif key_decision.keys == 'd':
        player1 = 'd'
        anti2 = random.choice(antidef)
        if anti2 == "AntiDef1":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 1
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti2 == "AntiDef2":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 1
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti2 == "AntiDef3":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 1
            doAntiDef4 = 0
            doAntiDef5 = 0
        if anti2 == "AntiDef4":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 1
            doAntiDef5 = 0
        if anti2 == "AntiDef5":
            doAntiCoop1 = 0
            doAntiCoop2 = 0
            doAntiCoop3 = 0
            doAntiCoop4 = 0
            doAntiCoop5 = 0
            doAntiDef1 = 0
            doAntiDef2 = 0
            doAntiDef3 = 0
            doAntiDef4 = 0
            doAntiDef5 = 1
    
        if player1 == "d" and player2 == "c":
            doFeedCC = 0
            doFeedCD = 0
            doFeedDC = 1
            doFeedDD = 0
            num_def_player1 += 1
            outcomes += ["dc"]
            outcomesExc = "dc"
        if player1 == "d" and player2 == "d":
            doFeedCC = 0
            doFeedCD = 0
            doFeedDC = 0
            doFeedDD = 1
            num_def_player1 += 1
            outcomes += ["dd"]
            outcomesExc = "dd"
        
    #data to be added to Excel
    thisExp.addData("computer_decision",player2)
    thisExp.addData("outcomes",outcomesExc)
    
    gameloop.addData('Decision_Screen1.started', Decision_Screen1.tStartRefresh)
    gameloop.addData('Decision_Screen1.stopped', Decision_Screen1.tStopRefresh)
    # check responses
    if key_decision.keys in ['', [], None]:  # No response was made
        key_decision.keys = None
    gameloop.addData('key_decision.keys',key_decision.keys)
    if key_decision.keys != None:  # we had a response
        gameloop.addData('key_decision.rt', key_decision.rt)
    gameloop.addData('key_decision.started', key_decision.tStartRefresh)
    gameloop.addData('key_decision.stopped', key_decision.tStopRefresh)
    # the Routine "Decision" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    anticoop1loop = data.TrialHandler(nReps=doAntiCoop1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='2'),
        seed=None, name='anticoop1loop')
    thisExp.addLoop(anticoop1loop)  # add the loop to the experiment
    thisAnticoop1loop = anticoop1loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnticoop1loop.rgb)
    if thisAnticoop1loop != None:
        for paramName in thisAnticoop1loop:
            exec('{} = thisAnticoop1loop[paramName]'.format(paramName))
    
    for thisAnticoop1loop in anticoop1loop:
        currentLoop = anticoop1loop
        # abbreviate parameter names if possible (e.g. rgb = thisAnticoop1loop.rgb)
        if thisAnticoop1loop != None:
            for paramName in thisAnticoop1loop:
                exec('{} = thisAnticoop1loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiCoop1"-------
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        AntiCoopImage.setImage(PhaseContingency)
        currentround1.setColor('black', colorSpace='rgb')
        currentround1.setText(rounds)
        player1_earningsanticoop.setColor('black', colorSpace='rgb')
        player1_earningsanticoop.setText(player1_earnings)
        player2_earningsanticoop.setColor('black', colorSpace='rgb')
        player2_earningsanticoop.setText(player2_earnings)
        phaseinstruct2.setColor('black', colorSpace='rgb')
        phaseinstruct2.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiCoop1Components = [AntiCoopImage, currentround1, player1_earningsanticoop, player2_earningsanticoop, phaseinstruct2]
        for thisComponent in AntiCoop1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiCoop1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiCoop1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiCoop1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiCoop1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiCoopImage* updates
            if AntiCoopImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiCoopImage.frameNStart = frameN  # exact frame index
                AntiCoopImage.tStart = t  # local t and not account for scr refresh
                AntiCoopImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiCoopImage, 'tStartRefresh')  # time at next scr refresh
                AntiCoopImage.setAutoDraw(True)
            if AntiCoopImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiCoopImage.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiCoopImage.tStop = t  # not accounting for scr refresh
                    AntiCoopImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiCoopImage, 'tStopRefresh')  # time at next scr refresh
                    AntiCoopImage.setAutoDraw(False)
            
            # *currentround1* updates
            if currentround1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround1.frameNStart = frameN  # exact frame index
                currentround1.tStart = t  # local t and not account for scr refresh
                currentround1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround1, 'tStartRefresh')  # time at next scr refresh
                currentround1.setAutoDraw(True)
            if currentround1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround1.tStop = t  # not accounting for scr refresh
                    currentround1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround1, 'tStopRefresh')  # time at next scr refresh
                    currentround1.setAutoDraw(False)
            
            # *player1_earningsanticoop* updates
            if player1_earningsanticoop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsanticoop.frameNStart = frameN  # exact frame index
                player1_earningsanticoop.tStart = t  # local t and not account for scr refresh
                player1_earningsanticoop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsanticoop, 'tStartRefresh')  # time at next scr refresh
                player1_earningsanticoop.setAutoDraw(True)
            if player1_earningsanticoop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsanticoop.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsanticoop.tStop = t  # not accounting for scr refresh
                    player1_earningsanticoop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsanticoop, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsanticoop.setAutoDraw(False)
            
            # *player2_earningsanticoop* updates
            if player2_earningsanticoop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsanticoop.frameNStart = frameN  # exact frame index
                player2_earningsanticoop.tStart = t  # local t and not account for scr refresh
                player2_earningsanticoop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsanticoop, 'tStartRefresh')  # time at next scr refresh
                player2_earningsanticoop.setAutoDraw(True)
            if player2_earningsanticoop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsanticoop.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsanticoop.tStop = t  # not accounting for scr refresh
                    player2_earningsanticoop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsanticoop, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsanticoop.setAutoDraw(False)
            
            # *phaseinstruct2* updates
            if phaseinstruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct2.frameNStart = frameN  # exact frame index
                phaseinstruct2.tStart = t  # local t and not account for scr refresh
                phaseinstruct2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct2, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct2.setAutoDraw(True)
            if phaseinstruct2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct2.tStop = t  # not accounting for scr refresh
                    phaseinstruct2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct2, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiCoop1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiCoop1"-------
        for thisComponent in AntiCoop1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        anticoop1loop.addData('AntiCoopImage.started', AntiCoopImage.tStartRefresh)
        anticoop1loop.addData('AntiCoopImage.stopped', AntiCoopImage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiCoop1 repeats of 'anticoop1loop'
    
    
    # set up handler to look after randomisation of conditions etc
    anticoop2loop = data.TrialHandler(nReps=doAntiCoop2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='2'),
        seed=None, name='anticoop2loop')
    thisExp.addLoop(anticoop2loop)  # add the loop to the experiment
    thisAnticoop2loop = anticoop2loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnticoop2loop.rgb)
    if thisAnticoop2loop != None:
        for paramName in thisAnticoop2loop:
            exec('{} = thisAnticoop2loop[paramName]'.format(paramName))
    
    for thisAnticoop2loop in anticoop2loop:
        currentLoop = anticoop2loop
        # abbreviate parameter names if possible (e.g. rgb = thisAnticoop2loop.rgb)
        if thisAnticoop2loop != None:
            for paramName in thisAnticoop2loop:
                exec('{} = thisAnticoop2loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiCoop2"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        AntiCoopImage_2.setImage(PhaseContingency)
        currentround_2.setColor('black', colorSpace='rgb')
        currentround_2.setText(rounds)
        player1_earningsanticoop_2.setColor('black', colorSpace='rgb')
        player1_earningsanticoop_2.setText(player1_earnings)
        player2_earningsanticoop_2.setColor('black', colorSpace='rgb')
        player2_earningsanticoop_2.setText(player2_earnings)
        phaseinstruct3.setColor('black', colorSpace='rgb')
        phaseinstruct3.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiCoop2Components = [AntiCoopImage_2, currentround_2, player1_earningsanticoop_2, player2_earningsanticoop_2, phaseinstruct3]
        for thisComponent in AntiCoop2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiCoop2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiCoop2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiCoop2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiCoop2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiCoopImage_2* updates
            if AntiCoopImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiCoopImage_2.frameNStart = frameN  # exact frame index
                AntiCoopImage_2.tStart = t  # local t and not account for scr refresh
                AntiCoopImage_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiCoopImage_2, 'tStartRefresh')  # time at next scr refresh
                AntiCoopImage_2.setAutoDraw(True)
            if AntiCoopImage_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiCoopImage_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiCoopImage_2.tStop = t  # not accounting for scr refresh
                    AntiCoopImage_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiCoopImage_2, 'tStopRefresh')  # time at next scr refresh
                    AntiCoopImage_2.setAutoDraw(False)
            
            # *currentround_2* updates
            if currentround_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround_2.frameNStart = frameN  # exact frame index
                currentround_2.tStart = t  # local t and not account for scr refresh
                currentround_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround_2, 'tStartRefresh')  # time at next scr refresh
                currentround_2.setAutoDraw(True)
            if currentround_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround_2.tStop = t  # not accounting for scr refresh
                    currentround_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround_2, 'tStopRefresh')  # time at next scr refresh
                    currentround_2.setAutoDraw(False)
            
            # *player1_earningsanticoop_2* updates
            if player1_earningsanticoop_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsanticoop_2.frameNStart = frameN  # exact frame index
                player1_earningsanticoop_2.tStart = t  # local t and not account for scr refresh
                player1_earningsanticoop_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsanticoop_2, 'tStartRefresh')  # time at next scr refresh
                player1_earningsanticoop_2.setAutoDraw(True)
            if player1_earningsanticoop_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsanticoop_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsanticoop_2.tStop = t  # not accounting for scr refresh
                    player1_earningsanticoop_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsanticoop_2, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsanticoop_2.setAutoDraw(False)
            
            # *player2_earningsanticoop_2* updates
            if player2_earningsanticoop_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsanticoop_2.frameNStart = frameN  # exact frame index
                player2_earningsanticoop_2.tStart = t  # local t and not account for scr refresh
                player2_earningsanticoop_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsanticoop_2, 'tStartRefresh')  # time at next scr refresh
                player2_earningsanticoop_2.setAutoDraw(True)
            if player2_earningsanticoop_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsanticoop_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsanticoop_2.tStop = t  # not accounting for scr refresh
                    player2_earningsanticoop_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsanticoop_2, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsanticoop_2.setAutoDraw(False)
            
            # *phaseinstruct3* updates
            if phaseinstruct3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct3.frameNStart = frameN  # exact frame index
                phaseinstruct3.tStart = t  # local t and not account for scr refresh
                phaseinstruct3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct3, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct3.setAutoDraw(True)
            if phaseinstruct3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct3.tStop = t  # not accounting for scr refresh
                    phaseinstruct3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct3, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiCoop2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiCoop2"-------
        for thisComponent in AntiCoop2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        anticoop2loop.addData('AntiCoopImage_2.started', AntiCoopImage_2.tStartRefresh)
        anticoop2loop.addData('AntiCoopImage_2.stopped', AntiCoopImage_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiCoop2 repeats of 'anticoop2loop'
    
    
    # set up handler to look after randomisation of conditions etc
    anticoop3loop = data.TrialHandler(nReps=doAntiCoop3, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='2'),
        seed=None, name='anticoop3loop')
    thisExp.addLoop(anticoop3loop)  # add the loop to the experiment
    thisAnticoop3loop = anticoop3loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnticoop3loop.rgb)
    if thisAnticoop3loop != None:
        for paramName in thisAnticoop3loop:
            exec('{} = thisAnticoop3loop[paramName]'.format(paramName))
    
    for thisAnticoop3loop in anticoop3loop:
        currentLoop = anticoop3loop
        # abbreviate parameter names if possible (e.g. rgb = thisAnticoop3loop.rgb)
        if thisAnticoop3loop != None:
            for paramName in thisAnticoop3loop:
                exec('{} = thisAnticoop3loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiCoop3"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        AntiCoopImage_3.setImage(PhaseContingency)
        currentround_3.setColor('black', colorSpace='rgb')
        currentround_3.setText(rounds)
        player1_earningsanticoop_3.setColor('black', colorSpace='rgb')
        player1_earningsanticoop_3.setText(player1_earnings)
        player2_earningsanticoop_3.setColor('black', colorSpace='rgb')
        player2_earningsanticoop_3.setText(player2_earnings)
        phaseinstruct4.setColor('black', colorSpace='rgb')
        phaseinstruct4.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiCoop3Components = [AntiCoopImage_3, currentround_3, player1_earningsanticoop_3, player2_earningsanticoop_3, phaseinstruct4]
        for thisComponent in AntiCoop3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiCoop3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiCoop3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiCoop3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiCoop3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiCoopImage_3* updates
            if AntiCoopImage_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiCoopImage_3.frameNStart = frameN  # exact frame index
                AntiCoopImage_3.tStart = t  # local t and not account for scr refresh
                AntiCoopImage_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiCoopImage_3, 'tStartRefresh')  # time at next scr refresh
                AntiCoopImage_3.setAutoDraw(True)
            if AntiCoopImage_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiCoopImage_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiCoopImage_3.tStop = t  # not accounting for scr refresh
                    AntiCoopImage_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiCoopImage_3, 'tStopRefresh')  # time at next scr refresh
                    AntiCoopImage_3.setAutoDraw(False)
            
            # *currentround_3* updates
            if currentround_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround_3.frameNStart = frameN  # exact frame index
                currentround_3.tStart = t  # local t and not account for scr refresh
                currentround_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround_3, 'tStartRefresh')  # time at next scr refresh
                currentround_3.setAutoDraw(True)
            if currentround_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround_3.tStop = t  # not accounting for scr refresh
                    currentround_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround_3, 'tStopRefresh')  # time at next scr refresh
                    currentround_3.setAutoDraw(False)
            
            # *player1_earningsanticoop_3* updates
            if player1_earningsanticoop_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsanticoop_3.frameNStart = frameN  # exact frame index
                player1_earningsanticoop_3.tStart = t  # local t and not account for scr refresh
                player1_earningsanticoop_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsanticoop_3, 'tStartRefresh')  # time at next scr refresh
                player1_earningsanticoop_3.setAutoDraw(True)
            if player1_earningsanticoop_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsanticoop_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsanticoop_3.tStop = t  # not accounting for scr refresh
                    player1_earningsanticoop_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsanticoop_3, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsanticoop_3.setAutoDraw(False)
            
            # *player2_earningsanticoop_3* updates
            if player2_earningsanticoop_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsanticoop_3.frameNStart = frameN  # exact frame index
                player2_earningsanticoop_3.tStart = t  # local t and not account for scr refresh
                player2_earningsanticoop_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsanticoop_3, 'tStartRefresh')  # time at next scr refresh
                player2_earningsanticoop_3.setAutoDraw(True)
            if player2_earningsanticoop_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsanticoop_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsanticoop_3.tStop = t  # not accounting for scr refresh
                    player2_earningsanticoop_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsanticoop_3, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsanticoop_3.setAutoDraw(False)
            
            # *phaseinstruct4* updates
            if phaseinstruct4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct4.frameNStart = frameN  # exact frame index
                phaseinstruct4.tStart = t  # local t and not account for scr refresh
                phaseinstruct4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct4, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct4.setAutoDraw(True)
            if phaseinstruct4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct4.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct4.tStop = t  # not accounting for scr refresh
                    phaseinstruct4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct4, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiCoop3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiCoop3"-------
        for thisComponent in AntiCoop3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        anticoop3loop.addData('AntiCoopImage_3.started', AntiCoopImage_3.tStartRefresh)
        anticoop3loop.addData('AntiCoopImage_3.stopped', AntiCoopImage_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiCoop3 repeats of 'anticoop3loop'
    
    
    # set up handler to look after randomisation of conditions etc
    anticoop4loop = data.TrialHandler(nReps=doAntiCoop4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='2'),
        seed=None, name='anticoop4loop')
    thisExp.addLoop(anticoop4loop)  # add the loop to the experiment
    thisAnticoop4loop = anticoop4loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnticoop4loop.rgb)
    if thisAnticoop4loop != None:
        for paramName in thisAnticoop4loop:
            exec('{} = thisAnticoop4loop[paramName]'.format(paramName))
    
    for thisAnticoop4loop in anticoop4loop:
        currentLoop = anticoop4loop
        # abbreviate parameter names if possible (e.g. rgb = thisAnticoop4loop.rgb)
        if thisAnticoop4loop != None:
            for paramName in thisAnticoop4loop:
                exec('{} = thisAnticoop4loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiCoop4"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        AntiCoopImage_4.setImage(PhaseContingency)
        currentround_4.setColor('black', colorSpace='rgb')
        currentround_4.setText(rounds)
        player1_earningsanticoop_4.setColor('black', colorSpace='rgb')
        player1_earningsanticoop_4.setText(player1_earnings)
        player2_earningsanticoop_4.setColor('black', colorSpace='rgb')
        player2_earningsanticoop_4.setText(player2_earnings)
        phaseinstruct5.setColor('black', colorSpace='rgb')
        phaseinstruct5.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiCoop4Components = [AntiCoopImage_4, currentround_4, player1_earningsanticoop_4, player2_earningsanticoop_4, phaseinstruct5]
        for thisComponent in AntiCoop4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiCoop4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiCoop4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiCoop4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiCoop4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiCoopImage_4* updates
            if AntiCoopImage_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiCoopImage_4.frameNStart = frameN  # exact frame index
                AntiCoopImage_4.tStart = t  # local t and not account for scr refresh
                AntiCoopImage_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiCoopImage_4, 'tStartRefresh')  # time at next scr refresh
                AntiCoopImage_4.setAutoDraw(True)
            if AntiCoopImage_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiCoopImage_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiCoopImage_4.tStop = t  # not accounting for scr refresh
                    AntiCoopImage_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiCoopImage_4, 'tStopRefresh')  # time at next scr refresh
                    AntiCoopImage_4.setAutoDraw(False)
            
            # *currentround_4* updates
            if currentround_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround_4.frameNStart = frameN  # exact frame index
                currentround_4.tStart = t  # local t and not account for scr refresh
                currentround_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround_4, 'tStartRefresh')  # time at next scr refresh
                currentround_4.setAutoDraw(True)
            if currentround_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround_4.tStop = t  # not accounting for scr refresh
                    currentround_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround_4, 'tStopRefresh')  # time at next scr refresh
                    currentround_4.setAutoDraw(False)
            
            # *player1_earningsanticoop_4* updates
            if player1_earningsanticoop_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsanticoop_4.frameNStart = frameN  # exact frame index
                player1_earningsanticoop_4.tStart = t  # local t and not account for scr refresh
                player1_earningsanticoop_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsanticoop_4, 'tStartRefresh')  # time at next scr refresh
                player1_earningsanticoop_4.setAutoDraw(True)
            if player1_earningsanticoop_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsanticoop_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsanticoop_4.tStop = t  # not accounting for scr refresh
                    player1_earningsanticoop_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsanticoop_4, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsanticoop_4.setAutoDraw(False)
            
            # *player2_earningsanticoop_4* updates
            if player2_earningsanticoop_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsanticoop_4.frameNStart = frameN  # exact frame index
                player2_earningsanticoop_4.tStart = t  # local t and not account for scr refresh
                player2_earningsanticoop_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsanticoop_4, 'tStartRefresh')  # time at next scr refresh
                player2_earningsanticoop_4.setAutoDraw(True)
            if player2_earningsanticoop_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsanticoop_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsanticoop_4.tStop = t  # not accounting for scr refresh
                    player2_earningsanticoop_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsanticoop_4, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsanticoop_4.setAutoDraw(False)
            
            # *phaseinstruct5* updates
            if phaseinstruct5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct5.frameNStart = frameN  # exact frame index
                phaseinstruct5.tStart = t  # local t and not account for scr refresh
                phaseinstruct5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct5, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct5.setAutoDraw(True)
            if phaseinstruct5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct5.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct5.tStop = t  # not accounting for scr refresh
                    phaseinstruct5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct5, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiCoop4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiCoop4"-------
        for thisComponent in AntiCoop4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        anticoop4loop.addData('AntiCoopImage_4.started', AntiCoopImage_4.tStartRefresh)
        anticoop4loop.addData('AntiCoopImage_4.stopped', AntiCoopImage_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiCoop4 repeats of 'anticoop4loop'
    
    
    # set up handler to look after randomisation of conditions etc
    anticoop5loop = data.TrialHandler(nReps=doAntiCoop5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='2'),
        seed=None, name='anticoop5loop')
    thisExp.addLoop(anticoop5loop)  # add the loop to the experiment
    thisAnticoop5loop = anticoop5loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnticoop5loop.rgb)
    if thisAnticoop5loop != None:
        for paramName in thisAnticoop5loop:
            exec('{} = thisAnticoop5loop[paramName]'.format(paramName))
    
    for thisAnticoop5loop in anticoop5loop:
        currentLoop = anticoop5loop
        # abbreviate parameter names if possible (e.g. rgb = thisAnticoop5loop.rgb)
        if thisAnticoop5loop != None:
            for paramName in thisAnticoop5loop:
                exec('{} = thisAnticoop5loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiCoop5"-------
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        AntiCoopImage_5.setImage(PhaseContingency)
        currentround_5.setColor('black', colorSpace='rgb')
        currentround_5.setText(rounds)
        player1_earningsanticoop_5.setColor('black', colorSpace='rgb')
        player1_earningsanticoop_5.setText(player1_earnings)
        player2_earningsanticoop_5.setColor('black', colorSpace='rgb')
        player2_earningsanticoop_5.setText(player2_earnings)
        phaseinstruct6.setColor('black', colorSpace='rgb')
        phaseinstruct6.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiCoop5Components = [AntiCoopImage_5, currentround_5, player1_earningsanticoop_5, player2_earningsanticoop_5, phaseinstruct6]
        for thisComponent in AntiCoop5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiCoop5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiCoop5"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiCoop5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiCoop5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiCoopImage_5* updates
            if AntiCoopImage_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiCoopImage_5.frameNStart = frameN  # exact frame index
                AntiCoopImage_5.tStart = t  # local t and not account for scr refresh
                AntiCoopImage_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiCoopImage_5, 'tStartRefresh')  # time at next scr refresh
                AntiCoopImage_5.setAutoDraw(True)
            if AntiCoopImage_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiCoopImage_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiCoopImage_5.tStop = t  # not accounting for scr refresh
                    AntiCoopImage_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiCoopImage_5, 'tStopRefresh')  # time at next scr refresh
                    AntiCoopImage_5.setAutoDraw(False)
            
            # *currentround_5* updates
            if currentround_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround_5.frameNStart = frameN  # exact frame index
                currentround_5.tStart = t  # local t and not account for scr refresh
                currentround_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround_5, 'tStartRefresh')  # time at next scr refresh
                currentround_5.setAutoDraw(True)
            if currentround_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround_5.tStop = t  # not accounting for scr refresh
                    currentround_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround_5, 'tStopRefresh')  # time at next scr refresh
                    currentround_5.setAutoDraw(False)
            
            # *player1_earningsanticoop_5* updates
            if player1_earningsanticoop_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsanticoop_5.frameNStart = frameN  # exact frame index
                player1_earningsanticoop_5.tStart = t  # local t and not account for scr refresh
                player1_earningsanticoop_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsanticoop_5, 'tStartRefresh')  # time at next scr refresh
                player1_earningsanticoop_5.setAutoDraw(True)
            if player1_earningsanticoop_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsanticoop_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsanticoop_5.tStop = t  # not accounting for scr refresh
                    player1_earningsanticoop_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsanticoop_5, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsanticoop_5.setAutoDraw(False)
            
            # *player2_earningsanticoop_5* updates
            if player2_earningsanticoop_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsanticoop_5.frameNStart = frameN  # exact frame index
                player2_earningsanticoop_5.tStart = t  # local t and not account for scr refresh
                player2_earningsanticoop_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsanticoop_5, 'tStartRefresh')  # time at next scr refresh
                player2_earningsanticoop_5.setAutoDraw(True)
            if player2_earningsanticoop_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsanticoop_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsanticoop_5.tStop = t  # not accounting for scr refresh
                    player2_earningsanticoop_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsanticoop_5, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsanticoop_5.setAutoDraw(False)
            
            # *phaseinstruct6* updates
            if phaseinstruct6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct6.frameNStart = frameN  # exact frame index
                phaseinstruct6.tStart = t  # local t and not account for scr refresh
                phaseinstruct6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct6, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct6.setAutoDraw(True)
            if phaseinstruct6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct6.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct6.tStop = t  # not accounting for scr refresh
                    phaseinstruct6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct6, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiCoop5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiCoop5"-------
        for thisComponent in AntiCoop5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        anticoop5loop.addData('AntiCoopImage_5.started', AntiCoopImage_5.tStartRefresh)
        anticoop5loop.addData('AntiCoopImage_5.stopped', AntiCoopImage_5.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiCoop5 repeats of 'anticoop5loop'
    
    
    # set up handler to look after randomisation of conditions etc
    antidef1loop = data.TrialHandler(nReps=doAntiDef1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='3'),
        seed=None, name='antidef1loop')
    thisExp.addLoop(antidef1loop)  # add the loop to the experiment
    thisAntidef1loop = antidef1loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAntidef1loop.rgb)
    if thisAntidef1loop != None:
        for paramName in thisAntidef1loop:
            exec('{} = thisAntidef1loop[paramName]'.format(paramName))
    
    for thisAntidef1loop in antidef1loop:
        currentLoop = antidef1loop
        # abbreviate parameter names if possible (e.g. rgb = thisAntidef1loop.rgb)
        if thisAntidef1loop != None:
            for paramName in thisAntidef1loop:
                exec('{} = thisAntidef1loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiDef1"-------
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        AntiDefImage.setImage(PhaseContingency)
        currentround3.setColor('black', colorSpace='rgb')
        currentround3.setText(rounds)
        player1_earningsantidef.setColor('black', colorSpace='rgb')
        player1_earningsantidef.setText(player1_earnings)
        player2_earningsantidef.setColor('black', colorSpace='rgb')
        player2_earningsantidef.setText(player2_earnings)
        phaseinstruct7.setColor('black', colorSpace='rgb')
        phaseinstruct7.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiDef1Components = [AntiDefImage, currentround3, player1_earningsantidef, player2_earningsantidef, phaseinstruct7]
        for thisComponent in AntiDef1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiDef1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiDef1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiDef1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiDef1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiDefImage* updates
            if AntiDefImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiDefImage.frameNStart = frameN  # exact frame index
                AntiDefImage.tStart = t  # local t and not account for scr refresh
                AntiDefImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiDefImage, 'tStartRefresh')  # time at next scr refresh
                AntiDefImage.setAutoDraw(True)
            if AntiDefImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiDefImage.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiDefImage.tStop = t  # not accounting for scr refresh
                    AntiDefImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiDefImage, 'tStopRefresh')  # time at next scr refresh
                    AntiDefImage.setAutoDraw(False)
            
            # *currentround3* updates
            if currentround3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround3.frameNStart = frameN  # exact frame index
                currentround3.tStart = t  # local t and not account for scr refresh
                currentround3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround3, 'tStartRefresh')  # time at next scr refresh
                currentround3.setAutoDraw(True)
            if currentround3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround3.tStop = t  # not accounting for scr refresh
                    currentround3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround3, 'tStopRefresh')  # time at next scr refresh
                    currentround3.setAutoDraw(False)
            
            # *player1_earningsantidef* updates
            if player1_earningsantidef.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsantidef.frameNStart = frameN  # exact frame index
                player1_earningsantidef.tStart = t  # local t and not account for scr refresh
                player1_earningsantidef.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsantidef, 'tStartRefresh')  # time at next scr refresh
                player1_earningsantidef.setAutoDraw(True)
            if player1_earningsantidef.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsantidef.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsantidef.tStop = t  # not accounting for scr refresh
                    player1_earningsantidef.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsantidef, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsantidef.setAutoDraw(False)
            
            # *player2_earningsantidef* updates
            if player2_earningsantidef.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsantidef.frameNStart = frameN  # exact frame index
                player2_earningsantidef.tStart = t  # local t and not account for scr refresh
                player2_earningsantidef.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsantidef, 'tStartRefresh')  # time at next scr refresh
                player2_earningsantidef.setAutoDraw(True)
            if player2_earningsantidef.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsantidef.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsantidef.tStop = t  # not accounting for scr refresh
                    player2_earningsantidef.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsantidef, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsantidef.setAutoDraw(False)
            
            # *phaseinstruct7* updates
            if phaseinstruct7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct7.frameNStart = frameN  # exact frame index
                phaseinstruct7.tStart = t  # local t and not account for scr refresh
                phaseinstruct7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct7, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct7.setAutoDraw(True)
            if phaseinstruct7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct7.tStop = t  # not accounting for scr refresh
                    phaseinstruct7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct7, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiDef1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiDef1"-------
        for thisComponent in AntiDef1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        antidef1loop.addData('AntiDefImage.started', AntiDefImage.tStartRefresh)
        antidef1loop.addData('AntiDefImage.stopped', AntiDefImage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiDef1 repeats of 'antidef1loop'
    
    
    # set up handler to look after randomisation of conditions etc
    antidef2loop = data.TrialHandler(nReps=doAntiDef2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='3'),
        seed=None, name='antidef2loop')
    thisExp.addLoop(antidef2loop)  # add the loop to the experiment
    thisAntidef2loop = antidef2loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAntidef2loop.rgb)
    if thisAntidef2loop != None:
        for paramName in thisAntidef2loop:
            exec('{} = thisAntidef2loop[paramName]'.format(paramName))
    
    for thisAntidef2loop in antidef2loop:
        currentLoop = antidef2loop
        # abbreviate parameter names if possible (e.g. rgb = thisAntidef2loop.rgb)
        if thisAntidef2loop != None:
            for paramName in thisAntidef2loop:
                exec('{} = thisAntidef2loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiDef2"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        AntiDefImage_2.setImage(PhaseContingency)
        currentround3_2.setColor('black', colorSpace='rgb')
        currentround3_2.setText(rounds)
        player1_earningsantidef_2.setColor('black', colorSpace='rgb')
        player1_earningsantidef_2.setText(player1_earnings)
        player2_earningsantidef_2.setColor('black', colorSpace='rgb')
        player2_earningsantidef_2.setText(player2_earnings)
        phaseinstruct8.setColor('black', colorSpace='rgb')
        phaseinstruct8.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiDef2Components = [AntiDefImage_2, currentround3_2, player1_earningsantidef_2, player2_earningsantidef_2, phaseinstruct8]
        for thisComponent in AntiDef2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiDef2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiDef2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiDef2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiDef2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiDefImage_2* updates
            if AntiDefImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiDefImage_2.frameNStart = frameN  # exact frame index
                AntiDefImage_2.tStart = t  # local t and not account for scr refresh
                AntiDefImage_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiDefImage_2, 'tStartRefresh')  # time at next scr refresh
                AntiDefImage_2.setAutoDraw(True)
            if AntiDefImage_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiDefImage_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiDefImage_2.tStop = t  # not accounting for scr refresh
                    AntiDefImage_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiDefImage_2, 'tStopRefresh')  # time at next scr refresh
                    AntiDefImage_2.setAutoDraw(False)
            
            # *currentround3_2* updates
            if currentround3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround3_2.frameNStart = frameN  # exact frame index
                currentround3_2.tStart = t  # local t and not account for scr refresh
                currentround3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround3_2, 'tStartRefresh')  # time at next scr refresh
                currentround3_2.setAutoDraw(True)
            if currentround3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround3_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround3_2.tStop = t  # not accounting for scr refresh
                    currentround3_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround3_2, 'tStopRefresh')  # time at next scr refresh
                    currentround3_2.setAutoDraw(False)
            
            # *player1_earningsantidef_2* updates
            if player1_earningsantidef_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsantidef_2.frameNStart = frameN  # exact frame index
                player1_earningsantidef_2.tStart = t  # local t and not account for scr refresh
                player1_earningsantidef_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsantidef_2, 'tStartRefresh')  # time at next scr refresh
                player1_earningsantidef_2.setAutoDraw(True)
            if player1_earningsantidef_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsantidef_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsantidef_2.tStop = t  # not accounting for scr refresh
                    player1_earningsantidef_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsantidef_2, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsantidef_2.setAutoDraw(False)
            
            # *player2_earningsantidef_2* updates
            if player2_earningsantidef_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsantidef_2.frameNStart = frameN  # exact frame index
                player2_earningsantidef_2.tStart = t  # local t and not account for scr refresh
                player2_earningsantidef_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsantidef_2, 'tStartRefresh')  # time at next scr refresh
                player2_earningsantidef_2.setAutoDraw(True)
            if player2_earningsantidef_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsantidef_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsantidef_2.tStop = t  # not accounting for scr refresh
                    player2_earningsantidef_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsantidef_2, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsantidef_2.setAutoDraw(False)
            
            # *phaseinstruct8* updates
            if phaseinstruct8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct8.frameNStart = frameN  # exact frame index
                phaseinstruct8.tStart = t  # local t and not account for scr refresh
                phaseinstruct8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct8, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct8.setAutoDraw(True)
            if phaseinstruct8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct8.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct8.tStop = t  # not accounting for scr refresh
                    phaseinstruct8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct8, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiDef2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiDef2"-------
        for thisComponent in AntiDef2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        antidef2loop.addData('AntiDefImage_2.started', AntiDefImage_2.tStartRefresh)
        antidef2loop.addData('AntiDefImage_2.stopped', AntiDefImage_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiDef2 repeats of 'antidef2loop'
    
    
    # set up handler to look after randomisation of conditions etc
    antidef3loop = data.TrialHandler(nReps=doAntiDef3, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='3'),
        seed=None, name='antidef3loop')
    thisExp.addLoop(antidef3loop)  # add the loop to the experiment
    thisAntidef3loop = antidef3loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAntidef3loop.rgb)
    if thisAntidef3loop != None:
        for paramName in thisAntidef3loop:
            exec('{} = thisAntidef3loop[paramName]'.format(paramName))
    
    for thisAntidef3loop in antidef3loop:
        currentLoop = antidef3loop
        # abbreviate parameter names if possible (e.g. rgb = thisAntidef3loop.rgb)
        if thisAntidef3loop != None:
            for paramName in thisAntidef3loop:
                exec('{} = thisAntidef3loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiDef3"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        AntiDefImage_3.setImage(PhaseContingency)
        currentround3_3.setColor('black', colorSpace='rgb')
        currentround3_3.setText(rounds)
        player1_earningsantidef_3.setColor('black', colorSpace='rgb')
        player1_earningsantidef_3.setText(player1_earnings)
        player2_earningsantidef_3.setColor('black', colorSpace='rgb')
        player2_earningsantidef_3.setText(player2_earnings)
        phaseinstruct9.setColor('black', colorSpace='rgb')
        phaseinstruct9.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiDef3Components = [AntiDefImage_3, currentround3_3, player1_earningsantidef_3, player2_earningsantidef_3, phaseinstruct9]
        for thisComponent in AntiDef3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiDef3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiDef3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiDef3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiDef3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiDefImage_3* updates
            if AntiDefImage_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiDefImage_3.frameNStart = frameN  # exact frame index
                AntiDefImage_3.tStart = t  # local t and not account for scr refresh
                AntiDefImage_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiDefImage_3, 'tStartRefresh')  # time at next scr refresh
                AntiDefImage_3.setAutoDraw(True)
            if AntiDefImage_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiDefImage_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiDefImage_3.tStop = t  # not accounting for scr refresh
                    AntiDefImage_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiDefImage_3, 'tStopRefresh')  # time at next scr refresh
                    AntiDefImage_3.setAutoDraw(False)
            
            # *currentround3_3* updates
            if currentround3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround3_3.frameNStart = frameN  # exact frame index
                currentround3_3.tStart = t  # local t and not account for scr refresh
                currentround3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround3_3, 'tStartRefresh')  # time at next scr refresh
                currentround3_3.setAutoDraw(True)
            if currentround3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround3_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround3_3.tStop = t  # not accounting for scr refresh
                    currentround3_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround3_3, 'tStopRefresh')  # time at next scr refresh
                    currentround3_3.setAutoDraw(False)
            
            # *player1_earningsantidef_3* updates
            if player1_earningsantidef_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsantidef_3.frameNStart = frameN  # exact frame index
                player1_earningsantidef_3.tStart = t  # local t and not account for scr refresh
                player1_earningsantidef_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsantidef_3, 'tStartRefresh')  # time at next scr refresh
                player1_earningsantidef_3.setAutoDraw(True)
            if player1_earningsantidef_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsantidef_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsantidef_3.tStop = t  # not accounting for scr refresh
                    player1_earningsantidef_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsantidef_3, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsantidef_3.setAutoDraw(False)
            
            # *player2_earningsantidef_3* updates
            if player2_earningsantidef_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsantidef_3.frameNStart = frameN  # exact frame index
                player2_earningsantidef_3.tStart = t  # local t and not account for scr refresh
                player2_earningsantidef_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsantidef_3, 'tStartRefresh')  # time at next scr refresh
                player2_earningsantidef_3.setAutoDraw(True)
            if player2_earningsantidef_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsantidef_3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsantidef_3.tStop = t  # not accounting for scr refresh
                    player2_earningsantidef_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsantidef_3, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsantidef_3.setAutoDraw(False)
            
            # *phaseinstruct9* updates
            if phaseinstruct9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct9.frameNStart = frameN  # exact frame index
                phaseinstruct9.tStart = t  # local t and not account for scr refresh
                phaseinstruct9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct9, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct9.setAutoDraw(True)
            if phaseinstruct9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct9.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct9.tStop = t  # not accounting for scr refresh
                    phaseinstruct9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct9, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct9.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiDef3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiDef3"-------
        for thisComponent in AntiDef3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        antidef3loop.addData('AntiDefImage_3.started', AntiDefImage_3.tStartRefresh)
        antidef3loop.addData('AntiDefImage_3.stopped', AntiDefImage_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiDef3 repeats of 'antidef3loop'
    
    
    # set up handler to look after randomisation of conditions etc
    antidef4loop = data.TrialHandler(nReps=doAntiDef4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='3'),
        seed=None, name='antidef4loop')
    thisExp.addLoop(antidef4loop)  # add the loop to the experiment
    thisAntidef4loop = antidef4loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAntidef4loop.rgb)
    if thisAntidef4loop != None:
        for paramName in thisAntidef4loop:
            exec('{} = thisAntidef4loop[paramName]'.format(paramName))
    
    for thisAntidef4loop in antidef4loop:
        currentLoop = antidef4loop
        # abbreviate parameter names if possible (e.g. rgb = thisAntidef4loop.rgb)
        if thisAntidef4loop != None:
            for paramName in thisAntidef4loop:
                exec('{} = thisAntidef4loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiDef4"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        AntiDefImage_4.setImage(PhaseContingency)
        currentround3_4.setColor('black', colorSpace='rgb')
        currentround3_4.setText(rounds)
        player1_earningsantidef_4.setColor('black', colorSpace='rgb')
        player1_earningsantidef_4.setText(player1_earnings)
        player2_earningsantidef_4.setColor('black', colorSpace='rgb')
        player2_earningsantidef_4.setText(player2_earnings)
        phaseinstruct10.setColor('black', colorSpace='rgb')
        phaseinstruct10.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiDef4Components = [AntiDefImage_4, currentround3_4, player1_earningsantidef_4, player2_earningsantidef_4, phaseinstruct10]
        for thisComponent in AntiDef4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiDef4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiDef4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiDef4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiDef4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiDefImage_4* updates
            if AntiDefImage_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiDefImage_4.frameNStart = frameN  # exact frame index
                AntiDefImage_4.tStart = t  # local t and not account for scr refresh
                AntiDefImage_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiDefImage_4, 'tStartRefresh')  # time at next scr refresh
                AntiDefImage_4.setAutoDraw(True)
            if AntiDefImage_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiDefImage_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiDefImage_4.tStop = t  # not accounting for scr refresh
                    AntiDefImage_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiDefImage_4, 'tStopRefresh')  # time at next scr refresh
                    AntiDefImage_4.setAutoDraw(False)
            
            # *currentround3_4* updates
            if currentround3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround3_4.frameNStart = frameN  # exact frame index
                currentround3_4.tStart = t  # local t and not account for scr refresh
                currentround3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround3_4, 'tStartRefresh')  # time at next scr refresh
                currentround3_4.setAutoDraw(True)
            if currentround3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround3_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround3_4.tStop = t  # not accounting for scr refresh
                    currentround3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround3_4, 'tStopRefresh')  # time at next scr refresh
                    currentround3_4.setAutoDraw(False)
            
            # *player1_earningsantidef_4* updates
            if player1_earningsantidef_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsantidef_4.frameNStart = frameN  # exact frame index
                player1_earningsantidef_4.tStart = t  # local t and not account for scr refresh
                player1_earningsantidef_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsantidef_4, 'tStartRefresh')  # time at next scr refresh
                player1_earningsantidef_4.setAutoDraw(True)
            if player1_earningsantidef_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsantidef_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsantidef_4.tStop = t  # not accounting for scr refresh
                    player1_earningsantidef_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsantidef_4, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsantidef_4.setAutoDraw(False)
            
            # *player2_earningsantidef_4* updates
            if player2_earningsantidef_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsantidef_4.frameNStart = frameN  # exact frame index
                player2_earningsantidef_4.tStart = t  # local t and not account for scr refresh
                player2_earningsantidef_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsantidef_4, 'tStartRefresh')  # time at next scr refresh
                player2_earningsantidef_4.setAutoDraw(True)
            if player2_earningsantidef_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsantidef_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsantidef_4.tStop = t  # not accounting for scr refresh
                    player2_earningsantidef_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsantidef_4, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsantidef_4.setAutoDraw(False)
            
            # *phaseinstruct10* updates
            if phaseinstruct10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct10.frameNStart = frameN  # exact frame index
                phaseinstruct10.tStart = t  # local t and not account for scr refresh
                phaseinstruct10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct10, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct10.setAutoDraw(True)
            if phaseinstruct10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct10.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct10.tStop = t  # not accounting for scr refresh
                    phaseinstruct10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct10, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiDef4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiDef4"-------
        for thisComponent in AntiDef4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        antidef4loop.addData('AntiDefImage_4.started', AntiDefImage_4.tStartRefresh)
        antidef4loop.addData('AntiDefImage_4.stopped', AntiDefImage_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiDef4 repeats of 'antidef4loop'
    
    
    # set up handler to look after randomisation of conditions etc
    antidef5loop = data.TrialHandler(nReps=doAntiDef5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='3'),
        seed=None, name='antidef5loop')
    thisExp.addLoop(antidef5loop)  # add the loop to the experiment
    thisAntidef5loop = antidef5loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAntidef5loop.rgb)
    if thisAntidef5loop != None:
        for paramName in thisAntidef5loop:
            exec('{} = thisAntidef5loop[paramName]'.format(paramName))
    
    for thisAntidef5loop in antidef5loop:
        currentLoop = antidef5loop
        # abbreviate parameter names if possible (e.g. rgb = thisAntidef5loop.rgb)
        if thisAntidef5loop != None:
            for paramName in thisAntidef5loop:
                exec('{} = thisAntidef5loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AntiDef5"-------
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        AntiDefImage_5.setImage(PhaseContingency)
        currentround3_5.setColor('black', colorSpace='rgb')
        currentround3_5.setText(rounds)
        player1_earningsantidef_5.setColor('black', colorSpace='rgb')
        player1_earningsantidef_5.setText(player1_earnings)
        player2_earningsantidef_5.setColor('black', colorSpace='rgb')
        player2_earningsantidef_5.setText(player2_earnings)
        phaseinstruct11.setColor('black', colorSpace='rgb')
        phaseinstruct11.setText('Waiting for partner response')
        # keep track of which components have finished
        AntiDef5Components = [AntiDefImage_5, currentround3_5, player1_earningsantidef_5, player2_earningsantidef_5, phaseinstruct11]
        for thisComponent in AntiDef5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AntiDef5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AntiDef5"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AntiDef5Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AntiDef5Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AntiDefImage_5* updates
            if AntiDefImage_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AntiDefImage_5.frameNStart = frameN  # exact frame index
                AntiDefImage_5.tStart = t  # local t and not account for scr refresh
                AntiDefImage_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AntiDefImage_5, 'tStartRefresh')  # time at next scr refresh
                AntiDefImage_5.setAutoDraw(True)
            if AntiDefImage_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AntiDefImage_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    AntiDefImage_5.tStop = t  # not accounting for scr refresh
                    AntiDefImage_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AntiDefImage_5, 'tStopRefresh')  # time at next scr refresh
                    AntiDefImage_5.setAutoDraw(False)
            
            # *currentround3_5* updates
            if currentround3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround3_5.frameNStart = frameN  # exact frame index
                currentround3_5.tStart = t  # local t and not account for scr refresh
                currentround3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround3_5, 'tStartRefresh')  # time at next scr refresh
                currentround3_5.setAutoDraw(True)
            if currentround3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround3_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround3_5.tStop = t  # not accounting for scr refresh
                    currentround3_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround3_5, 'tStopRefresh')  # time at next scr refresh
                    currentround3_5.setAutoDraw(False)
            
            # *player1_earningsantidef_5* updates
            if player1_earningsantidef_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsantidef_5.frameNStart = frameN  # exact frame index
                player1_earningsantidef_5.tStart = t  # local t and not account for scr refresh
                player1_earningsantidef_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsantidef_5, 'tStartRefresh')  # time at next scr refresh
                player1_earningsantidef_5.setAutoDraw(True)
            if player1_earningsantidef_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsantidef_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsantidef_5.tStop = t  # not accounting for scr refresh
                    player1_earningsantidef_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsantidef_5, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsantidef_5.setAutoDraw(False)
            
            # *player2_earningsantidef_5* updates
            if player2_earningsantidef_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsantidef_5.frameNStart = frameN  # exact frame index
                player2_earningsantidef_5.tStart = t  # local t and not account for scr refresh
                player2_earningsantidef_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsantidef_5, 'tStartRefresh')  # time at next scr refresh
                player2_earningsantidef_5.setAutoDraw(True)
            if player2_earningsantidef_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsantidef_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsantidef_5.tStop = t  # not accounting for scr refresh
                    player2_earningsantidef_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsantidef_5, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsantidef_5.setAutoDraw(False)
            
            # *phaseinstruct11* updates
            if phaseinstruct11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct11.frameNStart = frameN  # exact frame index
                phaseinstruct11.tStart = t  # local t and not account for scr refresh
                phaseinstruct11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct11, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct11.setAutoDraw(True)
            if phaseinstruct11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct11.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct11.tStop = t  # not accounting for scr refresh
                    phaseinstruct11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct11, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AntiDef5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AntiDef5"-------
        for thisComponent in AntiDef5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        antidef5loop.addData('AntiDefImage_5.started', AntiDefImage_5.tStartRefresh)
        antidef5loop.addData('AntiDefImage_5.stopped', AntiDefImage_5.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doAntiDef5 repeats of 'antidef5loop'
    
    
    # set up handler to look after randomisation of conditions etc
    feedCCloop = data.TrialHandler(nReps=doFeedCC, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='4'),
        seed=None, name='feedCCloop')
    thisExp.addLoop(feedCCloop)  # add the loop to the experiment
    thisFeedCCloop = feedCCloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedCCloop.rgb)
    if thisFeedCCloop != None:
        for paramName in thisFeedCCloop:
            exec('{} = thisFeedCCloop[paramName]'.format(paramName))
    
    for thisFeedCCloop in feedCCloop:
        currentLoop = feedCCloop
        # abbreviate parameter names if possible (e.g. rgb = thisFeedCCloop.rgb)
        if thisFeedCCloop != None:
            for paramName in thisFeedCCloop:
                exec('{} = thisFeedCCloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FeedCC"-------
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        #Earnings
        player1_earnings += 2
        player2_earnings += 2
        FeedCCimage.setImage(PhaseContingency)
        currentround4.setColor('black', colorSpace='rgb')
        currentround4.setText(rounds)
        player1_earningsfeedCC.setColor('black', colorSpace='rgb')
        player1_earningsfeedCC.setText(player1_earnings)
        player2_earningsfeedCC.setColor('black', colorSpace='rgb')
        player2_earningsfeedCC.setText(player2_earnings)
        phaseinstruct12.setColor('black', colorSpace='rgb')
        phaseinstruct12.setText('Both players cooperated!')
        # keep track of which components have finished
        FeedCCComponents = [FeedCCimage, currentround4, player1_earningsfeedCC, player2_earningsfeedCC, phaseinstruct12]
        for thisComponent in FeedCCComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedCCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "FeedCC"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedCCClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedCCClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FeedCCimage* updates
            if FeedCCimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedCCimage.frameNStart = frameN  # exact frame index
                FeedCCimage.tStart = t  # local t and not account for scr refresh
                FeedCCimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedCCimage, 'tStartRefresh')  # time at next scr refresh
                FeedCCimage.setAutoDraw(True)
            if FeedCCimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedCCimage.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedCCimage.tStop = t  # not accounting for scr refresh
                    FeedCCimage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FeedCCimage, 'tStopRefresh')  # time at next scr refresh
                    FeedCCimage.setAutoDraw(False)
            
            # *currentround4* updates
            if currentround4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround4.frameNStart = frameN  # exact frame index
                currentround4.tStart = t  # local t and not account for scr refresh
                currentround4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround4, 'tStartRefresh')  # time at next scr refresh
                currentround4.setAutoDraw(True)
            if currentround4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround4.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround4.tStop = t  # not accounting for scr refresh
                    currentround4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround4, 'tStopRefresh')  # time at next scr refresh
                    currentround4.setAutoDraw(False)
            
            # *player1_earningsfeedCC* updates
            if player1_earningsfeedCC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsfeedCC.frameNStart = frameN  # exact frame index
                player1_earningsfeedCC.tStart = t  # local t and not account for scr refresh
                player1_earningsfeedCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsfeedCC, 'tStartRefresh')  # time at next scr refresh
                player1_earningsfeedCC.setAutoDraw(True)
            if player1_earningsfeedCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsfeedCC.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsfeedCC.tStop = t  # not accounting for scr refresh
                    player1_earningsfeedCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsfeedCC, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsfeedCC.setAutoDraw(False)
            
            # *player2_earningsfeedCC* updates
            if player2_earningsfeedCC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsfeedCC.frameNStart = frameN  # exact frame index
                player2_earningsfeedCC.tStart = t  # local t and not account for scr refresh
                player2_earningsfeedCC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsfeedCC, 'tStartRefresh')  # time at next scr refresh
                player2_earningsfeedCC.setAutoDraw(True)
            if player2_earningsfeedCC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsfeedCC.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsfeedCC.tStop = t  # not accounting for scr refresh
                    player2_earningsfeedCC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsfeedCC, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsfeedCC.setAutoDraw(False)
            
            # *phaseinstruct12* updates
            if phaseinstruct12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct12.frameNStart = frameN  # exact frame index
                phaseinstruct12.tStart = t  # local t and not account for scr refresh
                phaseinstruct12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct12, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct12.setAutoDraw(True)
            if phaseinstruct12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct12.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct12.tStop = t  # not accounting for scr refresh
                    phaseinstruct12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct12, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedCCComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FeedCC"-------
        for thisComponent in FeedCCComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedCCloop.addData('FeedCCimage.started', FeedCCimage.tStartRefresh)
        feedCCloop.addData('FeedCCimage.stopped', FeedCCimage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doFeedCC repeats of 'feedCCloop'
    
    
    # set up handler to look after randomisation of conditions etc
    feedCDloop = data.TrialHandler(nReps=doFeedCD, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='5'),
        seed=None, name='feedCDloop')
    thisExp.addLoop(feedCDloop)  # add the loop to the experiment
    thisFeedCDloop = feedCDloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedCDloop.rgb)
    if thisFeedCDloop != None:
        for paramName in thisFeedCDloop:
            exec('{} = thisFeedCDloop[paramName]'.format(paramName))
    
    for thisFeedCDloop in feedCDloop:
        currentLoop = feedCDloop
        # abbreviate parameter names if possible (e.g. rgb = thisFeedCDloop.rgb)
        if thisFeedCDloop != None:
            for paramName in thisFeedCDloop:
                exec('{} = thisFeedCDloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FeedCD"-------
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # Earnings
        player1_earnings += 0
        player2_earnings += 3
        FeedCDimage.setImage(PhaseContingency)
        currentround5.setColor('black', colorSpace='rgb')
        currentround5.setText(rounds)
        player1_earningsfeedCD.setColor('black', colorSpace='rgb')
        player1_earningsfeedCD.setText(player1_earnings)
        player2_earningsfeedCD.setColor('black', colorSpace='rgb')
        player2_earningsfeedCD.setText(player2_earnings)
        phaseinstruct13.setColor('black', colorSpace='rgb')
        phaseinstruct13.setText('Player 1 cooperated, Player 2 defected!')
        # keep track of which components have finished
        FeedCDComponents = [FeedCDimage, currentround5, player1_earningsfeedCD, player2_earningsfeedCD, phaseinstruct13]
        for thisComponent in FeedCDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedCDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "FeedCD"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedCDClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedCDClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FeedCDimage* updates
            if FeedCDimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedCDimage.frameNStart = frameN  # exact frame index
                FeedCDimage.tStart = t  # local t and not account for scr refresh
                FeedCDimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedCDimage, 'tStartRefresh')  # time at next scr refresh
                FeedCDimage.setAutoDraw(True)
            if FeedCDimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedCDimage.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedCDimage.tStop = t  # not accounting for scr refresh
                    FeedCDimage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FeedCDimage, 'tStopRefresh')  # time at next scr refresh
                    FeedCDimage.setAutoDraw(False)
            
            # *currentround5* updates
            if currentround5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround5.frameNStart = frameN  # exact frame index
                currentround5.tStart = t  # local t and not account for scr refresh
                currentround5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround5, 'tStartRefresh')  # time at next scr refresh
                currentround5.setAutoDraw(True)
            if currentround5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround5.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround5.tStop = t  # not accounting for scr refresh
                    currentround5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround5, 'tStopRefresh')  # time at next scr refresh
                    currentround5.setAutoDraw(False)
            
            # *player1_earningsfeedCD* updates
            if player1_earningsfeedCD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsfeedCD.frameNStart = frameN  # exact frame index
                player1_earningsfeedCD.tStart = t  # local t and not account for scr refresh
                player1_earningsfeedCD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsfeedCD, 'tStartRefresh')  # time at next scr refresh
                player1_earningsfeedCD.setAutoDraw(True)
            if player1_earningsfeedCD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsfeedCD.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsfeedCD.tStop = t  # not accounting for scr refresh
                    player1_earningsfeedCD.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsfeedCD, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsfeedCD.setAutoDraw(False)
            
            # *player2_earningsfeedCD* updates
            if player2_earningsfeedCD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsfeedCD.frameNStart = frameN  # exact frame index
                player2_earningsfeedCD.tStart = t  # local t and not account for scr refresh
                player2_earningsfeedCD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsfeedCD, 'tStartRefresh')  # time at next scr refresh
                player2_earningsfeedCD.setAutoDraw(True)
            if player2_earningsfeedCD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsfeedCD.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsfeedCD.tStop = t  # not accounting for scr refresh
                    player2_earningsfeedCD.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsfeedCD, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsfeedCD.setAutoDraw(False)
            
            # *phaseinstruct13* updates
            if phaseinstruct13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct13.frameNStart = frameN  # exact frame index
                phaseinstruct13.tStart = t  # local t and not account for scr refresh
                phaseinstruct13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct13, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct13.setAutoDraw(True)
            if phaseinstruct13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct13.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct13.tStop = t  # not accounting for scr refresh
                    phaseinstruct13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct13, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct13.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedCDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FeedCD"-------
        for thisComponent in FeedCDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedCDloop.addData('FeedCDimage.started', FeedCDimage.tStartRefresh)
        feedCDloop.addData('FeedCDimage.stopped', FeedCDimage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doFeedCD repeats of 'feedCDloop'
    
    
    # set up handler to look after randomisation of conditions etc
    feedDCloop = data.TrialHandler(nReps=doFeedDC, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='6'),
        seed=None, name='feedDCloop')
    thisExp.addLoop(feedDCloop)  # add the loop to the experiment
    thisFeedDCloop = feedDCloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedDCloop.rgb)
    if thisFeedDCloop != None:
        for paramName in thisFeedDCloop:
            exec('{} = thisFeedDCloop[paramName]'.format(paramName))
    
    for thisFeedDCloop in feedDCloop:
        currentLoop = feedDCloop
        # abbreviate parameter names if possible (e.g. rgb = thisFeedDCloop.rgb)
        if thisFeedDCloop != None:
            for paramName in thisFeedDCloop:
                exec('{} = thisFeedDCloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FeedDC"-------
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # Earnings
        player1_earnings += 3
        player2_earnings += 0
        FeedDCimage.setImage(PhaseContingency)
        currentround6.setColor('black', colorSpace='rgb')
        currentround6.setText(rounds)
        player1_earningsfeedDC.setColor('black', colorSpace='rgb')
        player1_earningsfeedDC.setText(player1_earnings)
        player2_earningsfeedDC.setColor('black', colorSpace='rgb')
        player2_earningsfeedDC.setText(player2_earnings)
        phaseinstruct14.setColor('black', colorSpace='rgb')
        phaseinstruct14.setText('Player 1 defected, Player 2 cooperated!')
        # keep track of which components have finished
        FeedDCComponents = [FeedDCimage, currentround6, player1_earningsfeedDC, player2_earningsfeedDC, phaseinstruct14]
        for thisComponent in FeedDCComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedDCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "FeedDC"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedDCClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedDCClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FeedDCimage* updates
            if FeedDCimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedDCimage.frameNStart = frameN  # exact frame index
                FeedDCimage.tStart = t  # local t and not account for scr refresh
                FeedDCimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedDCimage, 'tStartRefresh')  # time at next scr refresh
                FeedDCimage.setAutoDraw(True)
            if FeedDCimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedDCimage.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedDCimage.tStop = t  # not accounting for scr refresh
                    FeedDCimage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FeedDCimage, 'tStopRefresh')  # time at next scr refresh
                    FeedDCimage.setAutoDraw(False)
            
            # *currentround6* updates
            if currentround6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround6.frameNStart = frameN  # exact frame index
                currentround6.tStart = t  # local t and not account for scr refresh
                currentround6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround6, 'tStartRefresh')  # time at next scr refresh
                currentround6.setAutoDraw(True)
            if currentround6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround6.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround6.tStop = t  # not accounting for scr refresh
                    currentround6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround6, 'tStopRefresh')  # time at next scr refresh
                    currentround6.setAutoDraw(False)
            
            # *player1_earningsfeedDC* updates
            if player1_earningsfeedDC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsfeedDC.frameNStart = frameN  # exact frame index
                player1_earningsfeedDC.tStart = t  # local t and not account for scr refresh
                player1_earningsfeedDC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsfeedDC, 'tStartRefresh')  # time at next scr refresh
                player1_earningsfeedDC.setAutoDraw(True)
            if player1_earningsfeedDC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsfeedDC.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsfeedDC.tStop = t  # not accounting for scr refresh
                    player1_earningsfeedDC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsfeedDC, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsfeedDC.setAutoDraw(False)
            
            # *player2_earningsfeedDC* updates
            if player2_earningsfeedDC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsfeedDC.frameNStart = frameN  # exact frame index
                player2_earningsfeedDC.tStart = t  # local t and not account for scr refresh
                player2_earningsfeedDC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsfeedDC, 'tStartRefresh')  # time at next scr refresh
                player2_earningsfeedDC.setAutoDraw(True)
            if player2_earningsfeedDC.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsfeedDC.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsfeedDC.tStop = t  # not accounting for scr refresh
                    player2_earningsfeedDC.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsfeedDC, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsfeedDC.setAutoDraw(False)
            
            # *phaseinstruct14* updates
            if phaseinstruct14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct14.frameNStart = frameN  # exact frame index
                phaseinstruct14.tStart = t  # local t and not account for scr refresh
                phaseinstruct14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct14, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct14.setAutoDraw(True)
            if phaseinstruct14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct14.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct14.tStop = t  # not accounting for scr refresh
                    phaseinstruct14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct14, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedDCComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FeedDC"-------
        for thisComponent in FeedDCComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedDCloop.addData('FeedDCimage.started', FeedDCimage.tStartRefresh)
        feedDCloop.addData('FeedDCimage.stopped', FeedDCimage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doFeedDC repeats of 'feedDCloop'
    
    
    # set up handler to look after randomisation of conditions etc
    feedDDloop = data.TrialHandler(nReps=doFeedDD, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli\\PDstimuli.xlsx', selection='7'),
        seed=None, name='feedDDloop')
    thisExp.addLoop(feedDDloop)  # add the loop to the experiment
    thisFeedDDloop = feedDDloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedDDloop.rgb)
    if thisFeedDDloop != None:
        for paramName in thisFeedDDloop:
            exec('{} = thisFeedDDloop[paramName]'.format(paramName))
    
    for thisFeedDDloop in feedDDloop:
        currentLoop = feedDDloop
        # abbreviate parameter names if possible (e.g. rgb = thisFeedDDloop.rgb)
        if thisFeedDDloop != None:
            for paramName in thisFeedDDloop:
                exec('{} = thisFeedDDloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FeedDD"-------
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        #Earnings
        player1_earnings += 1
        player2_earnings += 1
        FeedDDimage.setImage(PhaseContingency)
        currentround7.setColor('black', colorSpace='rgb')
        currentround7.setText(rounds)
        player1_earningsfeedDD.setColor('black', colorSpace='rgb')
        player1_earningsfeedDD.setText(player1_earnings)
        player2_earningsfeedDD.setColor('black', colorSpace='rgb')
        player2_earningsfeedDD.setText(player2_earnings)
        phaseinstruct15.setColor('black', colorSpace='rgb')
        phaseinstruct15.setText('Both players defected!')
        # keep track of which components have finished
        FeedDDComponents = [FeedDDimage, currentround7, player1_earningsfeedDD, player2_earningsfeedDD, phaseinstruct15]
        for thisComponent in FeedDDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedDDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "FeedDD"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedDDClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedDDClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FeedDDimage* updates
            if FeedDDimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedDDimage.frameNStart = frameN  # exact frame index
                FeedDDimage.tStart = t  # local t and not account for scr refresh
                FeedDDimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedDDimage, 'tStartRefresh')  # time at next scr refresh
                FeedDDimage.setAutoDraw(True)
            if FeedDDimage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedDDimage.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedDDimage.tStop = t  # not accounting for scr refresh
                    FeedDDimage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FeedDDimage, 'tStopRefresh')  # time at next scr refresh
                    FeedDDimage.setAutoDraw(False)
            
            # *currentround7* updates
            if currentround7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                currentround7.frameNStart = frameN  # exact frame index
                currentround7.tStart = t  # local t and not account for scr refresh
                currentround7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(currentround7, 'tStartRefresh')  # time at next scr refresh
                currentround7.setAutoDraw(True)
            if currentround7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > currentround7.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    currentround7.tStop = t  # not accounting for scr refresh
                    currentround7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(currentround7, 'tStopRefresh')  # time at next scr refresh
                    currentround7.setAutoDraw(False)
            
            # *player1_earningsfeedDD* updates
            if player1_earningsfeedDD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player1_earningsfeedDD.frameNStart = frameN  # exact frame index
                player1_earningsfeedDD.tStart = t  # local t and not account for scr refresh
                player1_earningsfeedDD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player1_earningsfeedDD, 'tStartRefresh')  # time at next scr refresh
                player1_earningsfeedDD.setAutoDraw(True)
            if player1_earningsfeedDD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player1_earningsfeedDD.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player1_earningsfeedDD.tStop = t  # not accounting for scr refresh
                    player1_earningsfeedDD.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player1_earningsfeedDD, 'tStopRefresh')  # time at next scr refresh
                    player1_earningsfeedDD.setAutoDraw(False)
            
            # *player2_earningsfeedDD* updates
            if player2_earningsfeedDD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                player2_earningsfeedDD.frameNStart = frameN  # exact frame index
                player2_earningsfeedDD.tStart = t  # local t and not account for scr refresh
                player2_earningsfeedDD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(player2_earningsfeedDD, 'tStartRefresh')  # time at next scr refresh
                player2_earningsfeedDD.setAutoDraw(True)
            if player2_earningsfeedDD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > player2_earningsfeedDD.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    player2_earningsfeedDD.tStop = t  # not accounting for scr refresh
                    player2_earningsfeedDD.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(player2_earningsfeedDD, 'tStopRefresh')  # time at next scr refresh
                    player2_earningsfeedDD.setAutoDraw(False)
            
            # *phaseinstruct15* updates
            if phaseinstruct15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                phaseinstruct15.frameNStart = frameN  # exact frame index
                phaseinstruct15.tStart = t  # local t and not account for scr refresh
                phaseinstruct15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(phaseinstruct15, 'tStartRefresh')  # time at next scr refresh
                phaseinstruct15.setAutoDraw(True)
            if phaseinstruct15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > phaseinstruct15.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    phaseinstruct15.tStop = t  # not accounting for scr refresh
                    phaseinstruct15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(phaseinstruct15, 'tStopRefresh')  # time at next scr refresh
                    phaseinstruct15.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedDDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FeedDD"-------
        for thisComponent in FeedDDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedDDloop.addData('FeedDDimage.started', FeedDDimage.tStartRefresh)
        feedDDloop.addData('FeedDDimage.stopped', FeedDDimage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doFeedDD repeats of 'feedDDloop'
    
    
    # ------Prepare to start Routine "roundcount"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    roundcountComponents = []
    for thisComponent in roundcountComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    roundcountClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "roundcount"-------
    while continueRoutine:
        # get current time
        t = roundcountClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=roundcountClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in roundcountComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "roundcount"-------
    for thisComponent in roundcountComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rounds += 1
    # the Routine "roundcount" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [wait1]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait1* updates
        if wait1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait1.frameNStart = frameN  # exact frame index
            wait1.tStart = t  # local t and not account for scr refresh
            wait1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait1, 'tStartRefresh')  # time at next scr refresh
            wait1.setAutoDraw(True)
        if wait1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                wait1.tStop = t  # not accounting for scr refresh
                wait1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait1, 'tStopRefresh')  # time at next scr refresh
                wait1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 9999 repeats of 'gameloop'


# ------Prepare to start Routine "blank"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [wait1]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait1* updates
    if wait1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait1.frameNStart = frameN  # exact frame index
        wait1.tStart = t  # local t and not account for scr refresh
        wait1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait1, 'tStartRefresh')  # time at next scr refresh
        wait1.setAutoDraw(True)
    if wait1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait1.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            wait1.tStop = t  # not accounting for scr refresh
            wait1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(wait1, 'tStopRefresh')  # time at next scr refresh
            wait1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "CompleteScreen"-------
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
CompleteScreenComponents = [background7, playagain]
for thisComponent in CompleteScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CompleteScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "CompleteScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = CompleteScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CompleteScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *background7* updates
    if background7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background7.frameNStart = frameN  # exact frame index
        background7.tStart = t  # local t and not account for scr refresh
        background7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background7, 'tStartRefresh')  # time at next scr refresh
        background7.setAutoDraw(True)
    if background7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > background7.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            background7.tStop = t  # not accounting for scr refresh
            background7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(background7, 'tStopRefresh')  # time at next scr refresh
            background7.setAutoDraw(False)
    
    # *playagain* updates
    if playagain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        playagain.frameNStart = frameN  # exact frame index
        playagain.tStart = t  # local t and not account for scr refresh
        playagain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(playagain, 'tStartRefresh')  # time at next scr refresh
        playagain.setAutoDraw(True)
    if playagain.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > playagain.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            playagain.tStop = t  # not accounting for scr refresh
            playagain.frameNStop = frameN  # exact frame index
            win.timeOnFlip(playagain, 'tStopRefresh')  # time at next scr refresh
            playagain.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CompleteScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CompleteScreen"-------
for thisComponent in CompleteScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('playagain.started', playagain.tStartRefresh)
thisExp.addData('playagain.stopped', playagain.tStopRefresh)
#data to be added to Excel
thisExp.addData("player1_earnings",player1_earnings)
thisExp.addData("player2_earnings",player2_earnings)
thisExp.addData("number of participant cooperations",num_coop_player1)
thisExp.addData("number of participant defections",num_def_player1)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
