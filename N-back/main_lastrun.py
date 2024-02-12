#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 12, 2024, at 12:50
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
    originPath='C:\\Users\\Ryougi mana\\Desktop\\5 心理学工具箱\\psychpyProgram\\cog_effort_discount_paradigm\\N-back\\main_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
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
guide = visual.TextStim(win=win, name='guide',
    text='2-back\nture : m\nfalse: n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_guide = keyboard.Keyboard()

# Initialize components for Routine "newBlock"
newBlockClock = core.Clock()
block_instr = visual.TextStim(win=win, name='block_instr',
    text='block instrution',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_block = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
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
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
resp_Letter = keyboard.Keyboard()

# Initialize components for Routine "feedback2block"
feedback2blockClock = core.Clock()
FB = visual.TextStim(win=win, name='FB',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_feedback = keyboard.Keyboard()

# Initialize components for Routine "Endexp"
EndexpClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thanks for participation!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
resp_guide.keys = []
resp_guide.rt = []
_resp_guide_allKeys = []
# keep track of which components have finished
instrComponents = [guide, resp_guide]
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
    
    # *guide* updates
    if guide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        guide.frameNStart = frameN  # exact frame index
        guide.tStart = t  # local t and not account for scr refresh
        guide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(guide, 'tStartRefresh')  # time at next scr refresh
        guide.setAutoDraw(True)
    
    # *resp_guide* updates
    waitOnFlip = False
    if resp_guide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_guide.frameNStart = frameN  # exact frame index
        resp_guide.tStart = t  # local t and not account for scr refresh
        resp_guide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_guide, 'tStartRefresh')  # time at next scr refresh
        resp_guide.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_guide.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_guide.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_guide.status == STARTED and not waitOnFlip:
        theseKeys = resp_guide.getKeys(keyList=['space'], waitRelease=False)
        _resp_guide_allKeys.extend(theseKeys)
        if len(_resp_guide_allKeys):
            resp_guide.keys = _resp_guide_allKeys[-1].name  # just the last key pressed
            resp_guide.rt = _resp_guide_allKeys[-1].rt
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
thisExp.addData('guide.started', guide.tStartRefresh)
thisExp.addData('guide.stopped', guide.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('con_block.xlsx', selection='5'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "newBlock"-------
    continueRoutine = True
    # update component parameters for each repeat
    n = Lv_Diff # first specify the n condition of the trial/block
    presentedLetters = [0]*n
    
    # 初始化正确计数器
    NumTarget = 0
    NumNonTarget = 0
    
    # 初始化Target/NonTarget计数器
    NumTar = 0
    NumNonTar = 0
    
    
    resp_block.keys = []
    resp_block.rt = []
    _resp_block_allKeys = []
    # keep track of which components have finished
    newBlockComponents = [block_instr, resp_block]
    for thisComponent in newBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    newBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "newBlock"-------
    while continueRoutine:
        # get current time
        t = newBlockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=newBlockClock)
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
        for thisComponent in newBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "newBlock"-------
    for thisComponent in newBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('block_instr.started', block_instr.tStartRefresh)
    blocks.addData('block_instr.stopped', block_instr.tStopRefresh)
    # the Routine "newBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('con_back.xlsx'),
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
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # 初始化target和corrAns
        target = eval("target" + str(n))
        corrAns = eval("corrAns" + str(n))
        
        
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
        letter.setColor(color_Diff, colorSpace='rgb')
        letter.setText(thisLetter)
        resp_Letter.keys = []
        resp_Letter.rt = []
        _resp_Letter_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, letter, resp_Letter]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
                    # was this correct?
                    if (resp_Letter.keys == str(corrAns)) or (resp_Letter.keys == corrAns):
                        resp_Letter.corr = 1
                    else:
                        resp_Letter.corr = 0
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
        thisExp.addData("corrAns", corrAns)
        
        if resp_Letter.corr == 1 and target == 1:
            NumTarget += 1
        
        if resp_Letter.corr == 1 and target == 0:
            NumNonTarget += 1
        
        if target == 1:
            NumTar += 1
        else:
            NumNonTar += 1
        trials.addData('fixation.started', fixation.tStartRefresh)
        trials.addData('fixation.stopped', fixation.tStopRefresh)
        trials.addData('letter.started', letter.tStartRefresh)
        trials.addData('letter.stopped', letter.tStopRefresh)
        # check responses
        if resp_Letter.keys in ['', [], None]:  # No response was made
            resp_Letter.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp_Letter.corr = 1;  # correct non-response
            else:
               resp_Letter.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp_Letter.keys',resp_Letter.keys)
        trials.addData('resp_Letter.corr', resp_Letter.corr)
        if resp_Letter.keys != None:  # we had a response
            trials.addData('resp_Letter.rt', resp_Letter.rt)
        trials.addData('resp_Letter.started', resp_Letter.tStartRefresh)
        trials.addData('resp_Letter.stopped', resp_Letter.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # ------Prepare to start Routine "feedback2block"-------
    continueRoutine = True
    # update component parameters for each repeat
    rate_T = NumTarget / NumTar
    rate_NT = NumNonTarget / NumNonTar
    
    feedback = "你完成靶子任务的正确率为：" + str(round(rate_T*100,2)) + "%\n你完成非靶子任务的正确率为：" + str(round(rate_NT*100,2)) + "%"
    
    
    FB.setText(feedback)
    resp_feedback.keys = []
    resp_feedback.rt = []
    _resp_feedback_allKeys = []
    # keep track of which components have finished
    feedback2blockComponents = [FB, resp_feedback]
    for thisComponent in feedback2blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback2blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback2block"-------
    while continueRoutine:
        # get current time
        t = feedback2blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback2blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FB* updates
        if FB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FB.frameNStart = frameN  # exact frame index
            FB.tStart = t  # local t and not account for scr refresh
            FB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FB, 'tStartRefresh')  # time at next scr refresh
            FB.setAutoDraw(True)
        
        # *resp_feedback* updates
        waitOnFlip = False
        if resp_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_feedback.frameNStart = frameN  # exact frame index
            resp_feedback.tStart = t  # local t and not account for scr refresh
            resp_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_feedback, 'tStartRefresh')  # time at next scr refresh
            resp_feedback.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_feedback.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_feedback.status == STARTED and not waitOnFlip:
            theseKeys = resp_feedback.getKeys(keyList=['space'], waitRelease=False)
            _resp_feedback_allKeys.extend(theseKeys)
            if len(_resp_feedback_allKeys):
                resp_feedback.keys = _resp_feedback_allKeys[-1].name  # just the last key pressed
                resp_feedback.rt = _resp_feedback_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback2block"-------
    for thisComponent in feedback2blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('FB.started', FB.tStartRefresh)
    blocks.addData('FB.stopped', FB.tStopRefresh)
    # the Routine "feedback2block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


# ------Prepare to start Routine "Endexp"-------
continueRoutine = True
# update component parameters for each repeat
resp_end.keys = []
resp_end.rt = []
_resp_end_allKeys = []
# keep track of which components have finished
EndexpComponents = [text, resp_end]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *resp_end* updates
    waitOnFlip = False
    if resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_end.frameNStart = frameN  # exact frame index
        resp_end.tStart = t  # local t and not account for scr refresh
        resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_end, 'tStartRefresh')  # time at next scr refresh
        resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_end.status == STARTED and not waitOnFlip:
        theseKeys = resp_end.getKeys(keyList=['space'], waitRelease=False)
        _resp_end_allKeys.extend(theseKeys)
        if len(_resp_end_allKeys):
            resp_end.keys = _resp_end_allKeys[-1].name  # just the last key pressed
            resp_end.rt = _resp_end_allKeys[-1].rt
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if resp_end.keys in ['', [], None]:  # No response was made
    resp_end.keys = None
thisExp.addData('resp_end.keys',resp_end.keys)
if resp_end.keys != None:  # we had a response
    thisExp.addData('resp_end.rt', resp_end.rt)
thisExp.addData('resp_end.started', resp_end.tStartRefresh)
thisExp.addData('resp_end.stopped', resp_end.tStopRefresh)
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
