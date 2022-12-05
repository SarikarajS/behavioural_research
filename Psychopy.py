#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Mon Dec  5 16:40:11 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from pyImports
import math
from numpy.random import random, randint, normal, shuffle, uniform
# Run 'Before Experiment' code from code
questionList = [
    'mathQuestionsA.csv',
    'mathQuestionsB.csv',
    'mathQuestionsC.csv',
    'mathQuestionsD.csv',
    'mathQuestionsE.csv',
    'mathQuestionsF.csv',
    'mathQuestionsG.csv',
    'mathQuestionsH.csv',
    'mathQuestionsI.csv',
    'mathQuestionsJ.csv'
]

shuffle(questionList)
# randomise the order

currQuestion=''

loopNum = 0


# Run 'Before Experiment' code from code_4
beginImg = 'Slide4.PNG'
blockTestTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'musicalMathTest'  # from the Builder filename that created this script
expInfo = {
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sarikaraj/Assessments/PSY asmnt/2204823PSY555Unit1/Appendix B _lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setUpCodeBits" ---
# Run 'Begin Experiment' code from code
playmusic = sound.Sound('music\silence.wav', secs=-1, stereo=True, hamming=True,
    name='playmusic')
playmusic.setVolume(1.0)


musicList = ['blockAmusic.csv','blockBmusic.csv',]

session = int(expInfo['session']) - 1

musicConditions = musicList[session]

# --- Initialize components for Routine "partInfo" ---
partInfoImage = visual.ImageStim(
    win=win,
    name='partInfoImage', 
    image='Slide1.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
partinfomouse = event.Mouse(win=win)
x, y = [None, None]
partinfomouse.mouseClock = core.Clock()

# --- Initialize components for Routine "consent" ---
partInfoImage_2 = visual.ImageStim(
    win=win,
    name='partInfoImage_2', 
    image='Slide3.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
partinfomouse_2 = event.Mouse(win=win)
x, y = [None, None]
partinfomouse_2.mouseClock = core.Clock()
consentBox = visual.Rect(
    win=win, name='consentBox',
    width=(0.19, 0.06)[0], height=(0.19, 0.06)[1],
    ori=0.0, pos=(0.35, -0.45), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=0.5, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "instructions" ---
partInfoImage_3 = visual.ImageStim(
    win=win,
    name='partInfoImage_3', 
    image='Slide2.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
partinfomouse_3 = event.Mouse(win=win)
x, y = [None, None]
partinfomouse_3.mouseClock = core.Clock()

# --- Initialize components for Routine "begin" ---
partInfoImage_4 = visual.ImageStim(
    win=win,
    name='partInfoImage_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
partinfomouse_4 = event.Mouse(win=win)
x, y = [None, None]
partinfomouse_4.mouseClock = core.Clock()

# --- Initialize components for Routine "startMusicBlock" ---

# --- Initialize components for Routine "trial" ---
question = visual.TextStim(win=win, name='question',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ansOne = visual.TextStim(win=win, name='ansOne',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ansTwo = visual.TextStim(win=win, name='ansTwo',
    text='',
    font='Open Sans',
    pos=(-0.1, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ansThree = visual.TextStim(win=win, name='ansThree',
    text='',
    font='Open Sans',
    pos=(0.1, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ansFour = visual.TextStim(win=win, name='ansFour',
    text='',
    font='Open Sans',
    pos=(0.3, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
mouseclickResponse = event.Mouse(win=win)
x, y = [None, None]
mouseclickResponse.mouseClock = core.Clock()
debuginfo = visual.TextStim(win=win, name='debuginfo',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.46), height=0.01, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "stopmusic" ---
text = visual.TextStim(win=win, name='text',
    text='The next block will begin in a moment',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "welldonepage" ---
partInfoImage_5 = visual.ImageStim(
    win=win,
    name='partInfoImage_5', 
    image='Slide6.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
partinfomouse_5 = event.Mouse(win=win)
x, y = [None, None]
partinfomouse_5.mouseClock = core.Clock()

# --- Initialize components for Routine "debrief" ---
partInfoImage_6 = visual.ImageStim(
    win=win,
    name='partInfoImage_6', 
    image='Slide7.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
partinfomouse_6 = event.Mouse(win=win)
x, y = [None, None]
partinfomouse_6.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setUpCodeBits" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setUpCodeBitsComponents = []
for thisComponent in setUpCodeBitsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setUpCodeBits" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setUpCodeBitsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setUpCodeBits" ---
for thisComponent in setUpCodeBitsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setUpCodeBits" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "partInfo" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the partinfomouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
partInfoComponents = [partInfoImage, partinfomouse]
for thisComponent in partInfoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "partInfo" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *partInfoImage* updates
    if partInfoImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partInfoImage.frameNStart = frameN  # exact frame index
        partInfoImage.tStart = t  # local t and not account for scr refresh
        partInfoImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partInfoImage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'partInfoImage.started')
        partInfoImage.setAutoDraw(True)
    # *partinfomouse* updates
    if partinfomouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partinfomouse.frameNStart = frameN  # exact frame index
        partinfomouse.tStart = t  # local t and not account for scr refresh
        partinfomouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partinfomouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('partinfomouse.started', t)
        partinfomouse.status = STARTED
        partinfomouse.mouseClock.reset()
        prevButtonState = partinfomouse.getPressed()  # if button is down already this ISN'T a new click
    if partinfomouse.status == STARTED:  # only update if started and not finished!
        buttons = partinfomouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in partInfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "partInfo" ---
for thisComponent in partInfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = partinfomouse.getPos()
buttons = partinfomouse.getPressed()
thisExp.addData('partinfomouse.x', x)
thisExp.addData('partinfomouse.y', y)
thisExp.addData('partinfomouse.leftButton', buttons[0])
thisExp.addData('partinfomouse.midButton', buttons[1])
thisExp.addData('partinfomouse.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "partInfo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the partinfomouse_2
partinfomouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
consentComponents = [partInfoImage_2, partinfomouse_2, consentBox]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *partInfoImage_2* updates
    if partInfoImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partInfoImage_2.frameNStart = frameN  # exact frame index
        partInfoImage_2.tStart = t  # local t and not account for scr refresh
        partInfoImage_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partInfoImage_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'partInfoImage_2.started')
        partInfoImage_2.setAutoDraw(True)
    # *partinfomouse_2* updates
    if partinfomouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partinfomouse_2.frameNStart = frameN  # exact frame index
        partinfomouse_2.tStart = t  # local t and not account for scr refresh
        partinfomouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partinfomouse_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('partinfomouse_2.started', t)
        partinfomouse_2.status = STARTED
        partinfomouse_2.mouseClock.reset()
        prevButtonState = partinfomouse_2.getPressed()  # if button is down already this ISN'T a new click
    if partinfomouse_2.status == STARTED:  # only update if started and not finished!
        buttons = partinfomouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(consentBox)
                    clickableList = consentBox
                except:
                    clickableList = [consentBox]
                for obj in clickableList:
                    if obj.contains(partinfomouse_2):
                        gotValidClick = True
                        partinfomouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *consentBox* updates
    if consentBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentBox.frameNStart = frameN  # exact frame index
        consentBox.tStart = t  # local t and not account for scr refresh
        consentBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'consentBox.started')
        consentBox.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "consent" ---
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = partinfomouse_2.getPos()
buttons = partinfomouse_2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(consentBox)
        clickableList = consentBox
    except:
        clickableList = [consentBox]
    for obj in clickableList:
        if obj.contains(partinfomouse_2):
            gotValidClick = True
            partinfomouse_2.clicked_name.append(obj.name)
thisExp.addData('partinfomouse_2.x', x)
thisExp.addData('partinfomouse_2.y', y)
thisExp.addData('partinfomouse_2.leftButton', buttons[0])
thisExp.addData('partinfomouse_2.midButton', buttons[1])
thisExp.addData('partinfomouse_2.rightButton', buttons[2])
if len(partinfomouse_2.clicked_name):
    thisExp.addData('partinfomouse_2.clicked_name', partinfomouse_2.clicked_name[0])
thisExp.nextEntry()
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the partinfomouse_3
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [partInfoImage_3, partinfomouse_3]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *partInfoImage_3* updates
    if partInfoImage_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partInfoImage_3.frameNStart = frameN  # exact frame index
        partInfoImage_3.tStart = t  # local t and not account for scr refresh
        partInfoImage_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partInfoImage_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'partInfoImage_3.started')
        partInfoImage_3.setAutoDraw(True)
    # *partinfomouse_3* updates
    if partinfomouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partinfomouse_3.frameNStart = frameN  # exact frame index
        partinfomouse_3.tStart = t  # local t and not account for scr refresh
        partinfomouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partinfomouse_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('partinfomouse_3.started', t)
        partinfomouse_3.status = STARTED
        partinfomouse_3.mouseClock.reset()
        prevButtonState = partinfomouse_3.getPressed()  # if button is down already this ISN'T a new click
    if partinfomouse_3.status == STARTED:  # only update if started and not finished!
        buttons = partinfomouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = partinfomouse_3.getPos()
buttons = partinfomouse_3.getPressed()
thisExp.addData('partinfomouse_3.x', x)
thisExp.addData('partinfomouse_3.y', y)
thisExp.addData('partinfomouse_3.leftButton', buttons[0])
thisExp.addData('partinfomouse_3.midButton', buttons[1])
thisExp.addData('partinfomouse_3.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
musicTypeLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(musicConditions),
    seed=None, name='musicTypeLoop')
thisExp.addLoop(musicTypeLoop)  # add the loop to the experiment
thisMusicTypeLoop = musicTypeLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMusicTypeLoop.rgb)
if thisMusicTypeLoop != None:
    for paramName in thisMusicTypeLoop:
        exec('{} = thisMusicTypeLoop[paramName]'.format(paramName))

for thisMusicTypeLoop in musicTypeLoop:
    currentLoop = musicTypeLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMusicTypeLoop.rgb)
    if thisMusicTypeLoop != None:
        for paramName in thisMusicTypeLoop:
            exec('{} = thisMusicTypeLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "begin" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    partInfoImage_4.setImage(beginImg)
    # setup some python lists for storing info about the partinfomouse_4
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code_4
    
    
    if loopNum==0:
        beginImg = 'Slide4.PNG'
    else:
        beginImg = 'Slide5.PNG'
    
    loopNum = loopNum + 1
    
    
    #blockTestTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    #blockTestTimer.reset()
    #blockTestTimer.add(testdurationsec)
    # keep track of which components have finished
    beginComponents = [partInfoImage_4, partinfomouse_4]
    for thisComponent in beginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "begin" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *partInfoImage_4* updates
        if partInfoImage_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partInfoImage_4.frameNStart = frameN  # exact frame index
            partInfoImage_4.tStart = t  # local t and not account for scr refresh
            partInfoImage_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partInfoImage_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'partInfoImage_4.started')
            partInfoImage_4.setAutoDraw(True)
        # *partinfomouse_4* updates
        if partinfomouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partinfomouse_4.frameNStart = frameN  # exact frame index
            partinfomouse_4.tStart = t  # local t and not account for scr refresh
            partinfomouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partinfomouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('partinfomouse_4.started', t)
            partinfomouse_4.status = STARTED
            partinfomouse_4.mouseClock.reset()
            prevButtonState = partinfomouse_4.getPressed()  # if button is down already this ISN'T a new click
        if partinfomouse_4.status == STARTED:  # only update if started and not finished!
            buttons = partinfomouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # abort routine on response        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in beginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "begin" ---
    for thisComponent in beginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for musicTypeLoop (TrialHandler)
    x, y = partinfomouse_4.getPos()
    buttons = partinfomouse_4.getPressed()
    musicTypeLoop.addData('partinfomouse_4.x', x)
    musicTypeLoop.addData('partinfomouse_4.y', y)
    musicTypeLoop.addData('partinfomouse_4.leftButton', buttons[0])
    musicTypeLoop.addData('partinfomouse_4.midButton', buttons[1])
    musicTypeLoop.addData('partinfomouse_4.rightButton', buttons[2])
    # the Routine "begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "startMusicBlock" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    currQuestionsFile = questionList.pop()
    
    blockTestTimer.reset()
    blockTestTimer.add(testdurationsec)
    
    playmusic.setSound(songfilename, secs=testdurationsec, hamming=True)
    playmusic.setVolume(1, log=False)
    playmusic.play(loops=1000)
    playmusic.play()  # start the sound (it finishes automatically)
    
    debugTxt = songfilename + " " + Speed + " " + Condition
    #debugTxt = musicType + " " + lyrics + " " +  style
    # keep track of which components have finished
    startMusicBlockComponents = []
    for thisComponent in startMusicBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "startMusicBlock" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startMusicBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startMusicBlock" ---
    for thisComponent in startMusicBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "startMusicBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsMath = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('/Users/sarikaraj/Assessments/PSY asmnt/Git/mat_questions/mathQuestionsC.csv'),
        seed=None, name='trialsMath')
    thisExp.addLoop(trialsMath)  # add the loop to the experiment
    thisTrialsMath = trialsMath.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsMath.rgb)
    if thisTrialsMath != None:
        for paramName in thisTrialsMath:
            exec('{} = thisTrialsMath[paramName]'.format(paramName))
    
    for thisTrialsMath in trialsMath:
        currentLoop = trialsMath
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsMath.rgb)
        if thisTrialsMath != None:
            for paramName in thisTrialsMath:
                exec('{} = thisTrialsMath[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        signs = {
            "add": "+",
            "subtract": "-",
            "multiply": "*"
        }
        
        currQuestion = "What is " + str(NumOne) + " " + signs[CategoryType] + " " + str(NumTwo) + "?"
        
        # randomise the answer order making a note of the correct answer
        
        correctLoc = randint(1, 4)
        
        if correctLoc==1:
            correctKey = 'ansOne'
            ansOneStr = Correct
            ansTwoStr = Incorrect1
            ansThreeStr = Incorrect2
            ansFourStr = Incorrect3
            
        if correctLoc==2:
            correctKey = 'ansTwo'
            ansOneStr = Incorrect1
            ansTwoStr = Correct
            ansThreeStr = Incorrect2
            ansFourStr = Incorrect3
        
        if correctLoc==3:
            correctKey = 'ansThree'   
            ansOneStr = Incorrect1
            ansTwoStr = Incorrect2
            ansThreeStr = Correct
            ansFourStr = Incorrect3
        
        if correctLoc==4:
            correctKey = 'ansFour'
            ansOneStr = Incorrect1
            ansTwoStr = Incorrect2
            ansThreeStr = Incorrect3
            ansFourStr = Correct
         
        question.setText(currQuestion)
        ansOne.setText(ansOneStr)
        ansTwo.setText(ansTwoStr)
        ansThree.setText(ansThreeStr)
        ansFour.setText(ansFourStr)
        # Run 'Begin Routine' code from processResponse
        endSoon = False
        # setup some python lists for storing info about the mouseclickResponse
        mouseclickResponse.clicked_name = []
        gotValidClick = False  # until a click is received
        debuginfo.setText(debugTxt)
        # keep track of which components have finished
        trialComponents = [question, ansOne, ansTwo, ansThree, ansFour, mouseclickResponse, debuginfo]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            if question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question.started')
                question.setAutoDraw(True)
            
            # *ansOne* updates
            if ansOne.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ansOne.frameNStart = frameN  # exact frame index
                ansOne.tStart = t  # local t and not account for scr refresh
                ansOne.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ansOne, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ansOne.started')
                ansOne.setAutoDraw(True)
            
            # *ansTwo* updates
            if ansTwo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ansTwo.frameNStart = frameN  # exact frame index
                ansTwo.tStart = t  # local t and not account for scr refresh
                ansTwo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ansTwo, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ansTwo.started')
                ansTwo.setAutoDraw(True)
            
            # *ansThree* updates
            if ansThree.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ansThree.frameNStart = frameN  # exact frame index
                ansThree.tStart = t  # local t and not account for scr refresh
                ansThree.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ansThree, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ansThree.started')
                ansThree.setAutoDraw(True)
            
            # *ansFour* updates
            if ansFour.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ansFour.frameNStart = frameN  # exact frame index
                ansFour.tStart = t  # local t and not account for scr refresh
                ansFour.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ansFour, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ansFour.started')
                ansFour.setAutoDraw(True)
            # *mouseclickResponse* updates
            if mouseclickResponse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseclickResponse.frameNStart = frameN  # exact frame index
                mouseclickResponse.tStart = t  # local t and not account for scr refresh
                mouseclickResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseclickResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouseclickResponse.started', t)
                mouseclickResponse.status = STARTED
                mouseclickResponse.mouseClock.reset()
                prevButtonState = mouseclickResponse.getPressed()  # if button is down already this ISN'T a new click
            if mouseclickResponse.status == STARTED:  # only update if started and not finished!
                buttons = mouseclickResponse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([ansOne, ansTwo, ansThree, ansFour])
                            clickableList = [ansOne, ansTwo, ansThree, ansFour]
                        except:
                            clickableList = [[ansOne, ansTwo, ansThree, ansFour]]
                        for obj in clickableList:
                            if obj.contains(mouseclickResponse):
                                gotValidClick = True
                                mouseclickResponse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *debuginfo* updates
            if debuginfo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debuginfo.frameNStart = frameN  # exact frame index
                debuginfo.tStart = t  # local t and not account for scr refresh
                debuginfo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debuginfo, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debuginfo.started')
                debuginfo.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from processResponse
        correctClick = False
        
        if mouseclickResponse.clicked_name[-1] == correctKey:
            correctClick = True
            
        thisExp.addData('correctClick', correctClick)
        
        if (blockTestTimer.getTime()<0):
            trialsMath.finished=True #or trials.finished=1 if you prefer
        # store data for trialsMath (TrialHandler)
        x, y = mouseclickResponse.getPos()
        buttons = mouseclickResponse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter([ansOne, ansTwo, ansThree, ansFour])
                clickableList = [ansOne, ansTwo, ansThree, ansFour]
            except:
                clickableList = [[ansOne, ansTwo, ansThree, ansFour]]
            for obj in clickableList:
                if obj.contains(mouseclickResponse):
                    gotValidClick = True
                    mouseclickResponse.clicked_name.append(obj.name)
        trialsMath.addData('mouseclickResponse.x', x)
        trialsMath.addData('mouseclickResponse.y', y)
        trialsMath.addData('mouseclickResponse.leftButton', buttons[0])
        trialsMath.addData('mouseclickResponse.midButton', buttons[1])
        trialsMath.addData('mouseclickResponse.rightButton', buttons[2])
        if len(mouseclickResponse.clicked_name):
            trialsMath.addData('mouseclickResponse.clicked_name', mouseclickResponse.clicked_name[0])
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsMath'
    
    
    # --- Prepare to start Routine "stopmusic" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stopmusiccode
    playmusic.stop()
    
    # keep track of which components have finished
    stopmusicComponents = [text]
    for thisComponent in stopmusicComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stopmusic" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stopmusicComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stopmusic" ---
    for thisComponent in stopmusicComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
# completed 1.0 repeats of 'musicTypeLoop'


# --- Prepare to start Routine "welldonepage" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the partinfomouse_5
gotValidClick = False  # until a click is received
# keep track of which components have finished
welldonepageComponents = [partInfoImage_5, partinfomouse_5]
for thisComponent in welldonepageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welldonepage" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *partInfoImage_5* updates
    if partInfoImage_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partInfoImage_5.frameNStart = frameN  # exact frame index
        partInfoImage_5.tStart = t  # local t and not account for scr refresh
        partInfoImage_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partInfoImage_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'partInfoImage_5.started')
        partInfoImage_5.setAutoDraw(True)
    # *partinfomouse_5* updates
    if partinfomouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partinfomouse_5.frameNStart = frameN  # exact frame index
        partinfomouse_5.tStart = t  # local t and not account for scr refresh
        partinfomouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partinfomouse_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('partinfomouse_5.started', t)
        partinfomouse_5.status = STARTED
        partinfomouse_5.mouseClock.reset()
        prevButtonState = partinfomouse_5.getPressed()  # if button is down already this ISN'T a new click
    if partinfomouse_5.status == STARTED:  # only update if started and not finished!
        buttons = partinfomouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welldonepageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welldonepage" ---
for thisComponent in welldonepageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = partinfomouse_5.getPos()
buttons = partinfomouse_5.getPressed()
thisExp.addData('partinfomouse_5.x', x)
thisExp.addData('partinfomouse_5.y', y)
thisExp.addData('partinfomouse_5.leftButton', buttons[0])
thisExp.addData('partinfomouse_5.midButton', buttons[1])
thisExp.addData('partinfomouse_5.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "welldonepage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "debrief" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the partinfomouse_6
gotValidClick = False  # until a click is received
# keep track of which components have finished
debriefComponents = [partInfoImage_6, partinfomouse_6]
for thisComponent in debriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "debrief" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *partInfoImage_6* updates
    if partInfoImage_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partInfoImage_6.frameNStart = frameN  # exact frame index
        partInfoImage_6.tStart = t  # local t and not account for scr refresh
        partInfoImage_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partInfoImage_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'partInfoImage_6.started')
        partInfoImage_6.setAutoDraw(True)
    # *partinfomouse_6* updates
    if partinfomouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        partinfomouse_6.frameNStart = frameN  # exact frame index
        partinfomouse_6.tStart = t  # local t and not account for scr refresh
        partinfomouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(partinfomouse_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('partinfomouse_6.started', t)
        partinfomouse_6.status = STARTED
        partinfomouse_6.mouseClock.reset()
        prevButtonState = partinfomouse_6.getPressed()  # if button is down already this ISN'T a new click
    if partinfomouse_6.status == STARTED:  # only update if started and not finished!
        buttons = partinfomouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "debrief" ---
for thisComponent in debriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = partinfomouse_6.getPos()
buttons = partinfomouse_6.getPressed()
thisExp.addData('partinfomouse_6.x', x)
thisExp.addData('partinfomouse_6.y', y)
thisExp.addData('partinfomouse_6.leftButton', buttons[0])
thisExp.addData('partinfomouse_6.midButton', buttons[1])
thisExp.addData('partinfomouse_6.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "debrief" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
