#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 18, 2024, at 14:42
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
    originPath='C:\\Users\\Ryougi mana\\Desktop\\5 心理学工具箱\\psychpyProgram\\cog_effort_discount_paradigm\\cog-effort_evaluation\\main.py',
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

# 初始化选项记录
Choices = list()
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

# Initialize components for Routine "mid"
midClock = core.Clock()
text_mid = visual.TextStim(win=win, name='text_mid',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_mid = keyboard.Keyboard()

# Initialize components for Routine "instrNback"
instrNbackClock = core.Clock()
block_instr = visual.TextStim(win=win, name='block_instr',
    text='',
    font='Open Sans',
    units='height', pos=(-0.08, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_block = keyboard.Keyboard()

# Initialize components for Routine "Nback"
NbackClock = core.Clock()
import random

letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
letter = visual.TextStim(win=win, name='letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=color_Diff, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
resp_Letter = keyboard.Keyboard()

# Initialize components for Routine "Endexp"
EndexpClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='感谢参与！',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_End = keyboard.Keyboard()

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
        thisChoice = list(["黑色", thisValue, 1])
    else:
        exec("value4low_" + colorName + "=" + str(thisValue - thisUnit/2))
        thisChoice = list([color, 2, backs])
    
    resultvalue = eval("value4low_" + colorName)
    exec("round_" + colorName + "=" + str("round_" + colorName + " + 1"))
    rounds = eval("round_" + colorName)
    Choices.append(thisChoice)
    
    # 记录信息
    thisExp.addData("preference", preference)
    thisExp.addData("thisvalue", thisValue)
    thisExp.addData("round", rounds)
    thisExp.addData("result", resultvalue)
    thisExp.addData("choice", thisChoice)
    
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


# ------Prepare to start Routine "mid"-------
continueRoutine = True
# update component parameters for each repeat
f_choice = random.sample(Choices,1)

midInstr = "随机抽选的结果为：\n" + "获得" +\
str(round(f_choice[0][1],2)) + "￥的" +\
str(f_choice[0][0]) + "任务"

n = f_choice[0][2]

text_mid.setText(midInstr)
resp_mid.keys = []
resp_mid.rt = []
_resp_mid_allKeys = []
# keep track of which components have finished
midComponents = [text_mid, resp_mid]
for thisComponent in midComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
midClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mid"-------
while continueRoutine:
    # get current time
    t = midClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=midClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_mid* updates
    if text_mid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_mid.frameNStart = frameN  # exact frame index
        text_mid.tStart = t  # local t and not account for scr refresh
        text_mid.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_mid, 'tStartRefresh')  # time at next scr refresh
        text_mid.setAutoDraw(True)
    
    # *resp_mid* updates
    waitOnFlip = False
    if resp_mid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_mid.frameNStart = frameN  # exact frame index
        resp_mid.tStart = t  # local t and not account for scr refresh
        resp_mid.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_mid, 'tStartRefresh')  # time at next scr refresh
        resp_mid.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_mid.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_mid.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_mid.status == STARTED and not waitOnFlip:
        theseKeys = resp_mid.getKeys(keyList=['space'], waitRelease=False)
        _resp_mid_allKeys.extend(theseKeys)
        if len(_resp_mid_allKeys):
            resp_mid.keys = _resp_mid_allKeys[-1].name  # just the last key pressed
            resp_mid.rt = _resp_mid_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in midComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mid"-------
for thisComponent in midComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_mid.started', text_mid.tStartRefresh)
thisExp.addData('text_mid.stopped', text_mid.tStopRefresh)
# the Routine "mid" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
choose = data.TrialHandler(nReps=n, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('con_block.xlsx'),
    seed=None, name='choose')
thisExp.addLoop(choose)  # add the loop to the experiment
thisChoose = choose.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChoose.rgb)
if thisChoose != None:
    for paramName in thisChoose:
        exec('{} = thisChoose[paramName]'.format(paramName))

for thisChoose in choose:
    currentLoop = choose
    # abbreviate parameter names if possible (e.g. rgb = thisChoose.rgb)
    if thisChoose != None:
        for paramName in thisChoose:
            exec('{} = thisChoose[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instrNback"-------
    continueRoutine = True
    # update component parameters for each repeat
    color_instr = str(f_choice[0][0])
    
    
    instrBlock = \
    "你即将完成" + color_instr + "任务。"\
    "该任务为" + str(n) + "-back任务。\n" +\
    "你需要将屏幕上出现的字母与前"+ str(n) +\
    "个字母进行比\n较，如果相同，则按N键，如果不同" +\
    "则按M键。\n\n例如，第1个字母是P，第" + str(n+1) +\
    "个字母也是P，则为\n相同，否则为不同。无法进行" +\
    "比较的默认为不同。\n\n" +\
    "如果理解了实验任务，请按空格进入实验。"
    block_instr.setText(instrBlock)
    resp_block.keys = []
    resp_block.rt = []
    _resp_block_allKeys = []
    # keep track of which components have finished
    instrNbackComponents = [block_instr, resp_block]
    for thisComponent in instrNbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrNbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrNback"-------
    while continueRoutine:
        # get current time
        t = instrNbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrNbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_instr* updates
        if block_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_instr.frameNStart = frameN  # exact frame index
            block_instr.tStart = t  # local t and not account for scr refresh
            block_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_instr, 'tStartRefresh')  # time at next scr refresh
            block_instr.setAutoDraw(True)
        
        # *resp_block* updates
        waitOnFlip = False
        if resp_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_block.frameNStart = frameN  # exact frame index
            resp_block.tStart = t  # local t and not account for scr refresh
            resp_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_block, 'tStartRefresh')  # time at next scr refresh
            resp_block.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_block.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_block.status == STARTED and not waitOnFlip:
            theseKeys = resp_block.getKeys(keyList=['space'], waitRelease=False)
            _resp_block_allKeys.extend(theseKeys)
            if len(_resp_block_allKeys):
                resp_block.keys = _resp_block_allKeys[-1].name  # just the last key pressed
                resp_block.rt = _resp_block_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrNbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrNback"-------
    for thisComponent in instrNbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    choose.addData('block_instr.started', block_instr.tStartRefresh)
    choose.addData('block_instr.stopped', block_instr.tStopRefresh)
    # the Routine "instrNback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('con_back.xlsx'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Nback"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # 初始化target
        target = eval("target" + str(n))
        
        thisLetter = np.random.choice(letters)
        letterSelected = False # a boolean to state a letter has not yet been selected
        if not target: # this is not a target trial
                while not letterSelected: # repeat the content of this loop until a letter is selected
                    thisLetter = np.random.choice(letters)# if this is not a target then randomly choose
                    if len(presentedLetters) < n or thisLetter != presentedLetters[-n]: # if n letters have not yet been presented, or this is not the same as the n-th trial back
                        letterSelected = True # accept this as the chosen letter
        else:
                thisLetter = presentedLetters[-n]# if this was a target choose the n'th back
        presentedLetters.append(thisLetter)
        letter.setText(thisLetter)
        resp_Letter.keys = []
        resp_Letter.rt = []
        _resp_Letter_allKeys = []
        # keep track of which components have finished
        NbackComponents = [fixation, letter, resp_Letter]
        for thisComponent in NbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Nback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = NbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *letter* updates
            if letter.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                letter.frameNStart = frameN  # exact frame index
                letter.tStart = t  # local t and not account for scr refresh
                letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(letter, 'tStartRefresh')  # time at next scr refresh
                letter.setAutoDraw(True)
            if letter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > letter.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    letter.tStop = t  # not accounting for scr refresh
                    letter.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(letter, 'tStopRefresh')  # time at next scr refresh
                    letter.setAutoDraw(False)
            
            # *resp_Letter* updates
            waitOnFlip = False
            if resp_Letter.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                resp_Letter.frameNStart = frameN  # exact frame index
                resp_Letter.tStart = t  # local t and not account for scr refresh
                resp_Letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_Letter, 'tStartRefresh')  # time at next scr refresh
                resp_Letter.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_Letter.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_Letter.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_Letter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp_Letter.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    resp_Letter.tStop = t  # not accounting for scr refresh
                    resp_Letter.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp_Letter, 'tStopRefresh')  # time at next scr refresh
                    resp_Letter.status = FINISHED
            if resp_Letter.status == STARTED and not waitOnFlip:
                theseKeys = resp_Letter.getKeys(keyList=['n', 'm'], waitRelease=False)
                _resp_Letter_allKeys.extend(theseKeys)
                if len(_resp_Letter_allKeys):
                    resp_Letter.keys = _resp_Letter_allKeys[-1].name  # just the last key pressed
                    resp_Letter.rt = _resp_Letter_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Nback"-------
        for thisComponent in NbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('fixation.started', fixation.tStartRefresh)
        trials_2.addData('fixation.stopped', fixation.tStopRefresh)
        trials_2.addData('letter.started', letter.tStartRefresh)
        trials_2.addData('letter.stopped', letter.tStopRefresh)
        # check responses
        if resp_Letter.keys in ['', [], None]:  # No response was made
            resp_Letter.keys = None
        trials_2.addData('resp_Letter.keys',resp_Letter.keys)
        if resp_Letter.keys != None:  # we had a response
            trials_2.addData('resp_Letter.rt', resp_Letter.rt)
        trials_2.addData('resp_Letter.started', resp_Letter.tStartRefresh)
        trials_2.addData('resp_Letter.stopped', resp_Letter.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed n repeats of 'choose'


# ------Prepare to start Routine "Endexp"-------
continueRoutine = True
# update component parameters for each repeat
resp_End.keys = []
resp_End.rt = []
_resp_End_allKeys = []
# keep track of which components have finished
EndexpComponents = [text_2, resp_End]
for thisComponent in EndexpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndexpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Endexp"-------
while continueRoutine:
    # get current time
    t = EndexpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndexpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *resp_End* updates
    waitOnFlip = False
    if resp_End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_End.frameNStart = frameN  # exact frame index
        resp_End.tStart = t  # local t and not account for scr refresh
        resp_End.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_End, 'tStartRefresh')  # time at next scr refresh
        resp_End.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_End.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_End.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_End.status == STARTED and not waitOnFlip:
        theseKeys = resp_End.getKeys(keyList=['space'], waitRelease=False)
        _resp_End_allKeys.extend(theseKeys)
        if len(_resp_End_allKeys):
            resp_End.keys = _resp_End_allKeys[-1].name  # just the last key pressed
            resp_End.rt = _resp_End_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndexpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Endexp"-------
for thisComponent in EndexpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if resp_End.keys in ['', [], None]:  # No response was made
    resp_End.keys = None
thisExp.addData('resp_End.keys',resp_End.keys)
if resp_End.keys != None:  # we had a response
    thisExp.addData('resp_End.rt', resp_End.rt)
thisExp.addData('resp_End.started', resp_End.tStartRefresh)
thisExp.addData('resp_End.stopped', resp_End.tStopRefresh)
thisExp.nextEntry()
# the Routine "Endexp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
