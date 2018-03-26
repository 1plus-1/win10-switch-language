#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keyboard import on_press, on_release, send, wait

def KeyPressed(event):
	global bCtrlDown, bSpaceDown, bSwitchLan
	if event.name == 'space':
		bSpaceDown = True
	if(event.name == 'left ctrl' or event.name == 'right ctrl'):
		bCtrlDown = True;
	if event.name == 'space' and bCtrlDown:	#space press during ctrl down
		bSwitchLan = True

def KeyReleased(event):
	global bCtrlDown, bSpaceDown, bSwitchLan
	if event.name == 'space':
		bSpaceDown = False
		if bSwitchLan and not bCtrlDown:
			bSwitchLan = False
			send('left windows+space')
	elif(event.name == 'left ctrl' or event.name == 'right ctrl'):
		bCtrlDown = False
		if bSwitchLan and not bSpaceDown:
			bSwitchLan = False
			send('left windows+space')

bCtrlDown = bSpaceDown = bSwitchLan = False
on_press(KeyPressed)
on_release(KeyReleased)
wait()
