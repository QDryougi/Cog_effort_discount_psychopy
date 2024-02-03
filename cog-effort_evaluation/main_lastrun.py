#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 03, 2024, at 15:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'main'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Ryougi mana\\Desktop\\5 心理学工具箱\\psychpyProgram\\cog-effort_evaluation\\main_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='press sace',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
import random

# 初始化价值
value4low_red = 1
value4low_blue = 1
value4low_brown = 1
value4low_purple = 1
value4low_green = 1

# 初始化价值变化单位
unit_red = 1
unit_blue = 1
unit_brown = 1
unit_purple = 1
unit_green = 1

# 初始化轮次
round_red = 0
round_blue = 0
round_brown = 0
round_purple = 0
round_green = 0

# 初始化按钮
buttonText1 = 0
buttonText2 = 0
positions = [(-0.4, -0.12), (0.4, -0.12)]
question = visual.TextStim(win=win, name='question',
    text='Which one is better?',
    font='Open Sans',
    units='height', pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
button_1 = visual.TextStim(win=win, name='button_1',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
button_2 = visual.TextStim(win=win, name='button_2',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
resp_CEP = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [text, key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
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
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    #设置选项文本
    buttonText1 = str(round(eval("value4low_" + colorName),2)) + "￥来完成\n一个黑色任务"
    
    
    
    buttonText2 = "2￥来完成\n一个" + color + "任务"
    
    # 设定位置，x小于0位于左侧
    random.shuffle(positions)
    position1 = positions[0]
    position2 = positions[1]
    button_1.setPos(position1)
    button_1.setText(buttonText1)
    button_2.setPos(position2)
    button_2.setText(buttonText2)
    resp_CEP.keys = []
    resp_CEP.rt = []
    _resp_CEP_allKeys = []
    # keep track of which components have finished
    trialComponents = [question, button_1, button_2, resp_CEP]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
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
            question.setAutoDraw(True)
        
        # *button_1* updates
        if button_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_1.frameNStart = frameN  # exact frame index
            button_1.tStart = t  # local t and not account for scr refresh
            button_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_1, 'tStartRefresh')  # time at next scr refresh
            button_1.setAutoDraw(True)
        
        # *button_2* updates
        if button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_2.frameNStart = frameN  # exact frame index
            button_2.tStart = t  # local t and not account for scr refresh
            button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
            button_2.setAutoDraw(True)
        
        # *resp_CEP* updates
        waitOnFlip = False
        if resp_CEP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_CEP.frameNStart = frameN  # exact frame index
            resp_CEP.tStart = t  # local t and not account for scr refresh
            resp_CEP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_CEP, 'tStartRefresh')  # time at next scr refresh
            resp_CEP.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_CEP.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_CEP.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_CEP.status == STARTED and not waitOnFlip:
            theseKeys = resp_CEP.getKeys(keyList=['n', 'm'], waitRelease=False)
            _resp_CEP_allKeys.extend(theseKeys)
            if len(_resp_CEP_allKeys):
                resp_CEP.keys = _resp_CEP_allKeys[-1].name  # just the last key pressed
                resp_CEP.rt = _resp_CEP_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # 记录下button1的位置
    thisPosition = position1
    
    #记录下当前的颜色
    thisColor = colorName
    
    # 记录当前试次使用的单位
    thisUnit = eval("unit_" + colorName)
    
    # 设置该颜色下一轮使用的单位
    exec("unit_" + colorName + " = " + str(thisUnit/2))
    
    # 记录当前轮次value
    thisValue = eval("value4low_" + colorName)
    
    # 记录下此时被试选择了 high effort(2) or low effort(1)
    if thisPosition[0] < 0:
        if resp_CEP.keys == "n":
            preference = 1
        else:
            preference = 2
    else:
        if resp_CEP.keys == "m":
            preference = 1
        else:
            preference = 2
    
    #设置下一轮使用的LowEffort值
    if preference == 1:
        exec("value4low_" + colorName + "=" + str(thisValue + thisUnit/2))
    else:
        exec("value4low_" + colorName + "=" + str(thisValue - thisUnit/2))
    
    resultvalue = eval("value4low_" + colorName)
    exec("round_" + colorName + "=" + str("round_" + colorName + " + 1"))
    rounds = eval("round_" + colorName)
    
    # 记录信息
    thisExp.addData("preference", preference)
    thisExp.addData("thisvalue", thisValue)
    thisExp.addData("round", rounds)
    thisExp.addData("result", resultvalue)
    
    trials.addData('question.started', question.tStartRefresh)
    trials.addData('question.stopped', question.tStopRefresh)
    trials.addData('button_1.started', button_1.tStartRefresh)
    trials.addData('button_1.stopped', button_1.tStopRefresh)
    trials.addData('button_2.started', button_2.tStartRefresh)
    trials.addData('button_2.stopped', button_2.tStopRefresh)
    # check responses
    if resp_CEP.keys in ['', [], None]:  # No response was made
        resp_CEP.keys = None
    trials.addData('resp_CEP.keys',resp_CEP.keys)
    if resp_CEP.keys != None:  # we had a response
        trials.addData('resp_CEP.rt', resp_CEP.rt)
    trials.addData('resp_CEP.started', resp_CEP.tStartRefresh)
    trials.addData('resp_CEP.stopped', resp_CEP.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
