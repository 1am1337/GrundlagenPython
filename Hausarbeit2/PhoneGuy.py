import dearpygui.dearpygui as dpg
import dearpygui_grid as dpgGrid
import numpy as np
import pyaudio
import time

p = pyaudio.PyAudio()

WindowSize = [480, 600]
sr = 48000
freq1 = [1209, 1336, 1477, 1633]
freq2 = [697, 770, 852, 941]
dur = 0.07
vol = 0.8

dpg.create_context()
dpg.setup_dearpygui()
dpg.create_viewport(width=WindowSize[0], height=WindowSize[1], title="CALL THE FIREFIGHTERS!!")
dpg.show_viewport()

def GenerateSine(FreqPos):
    data1 = np.sin(2 * np.pi * np.arange(sr*dur)* freq1[FreqPos[0]]/sr).astype(np.float32)
    data2 = np.sin(2 * np.pi * np.arange(sr*dur)* freq2[FreqPos[1]]/sr).astype(np.float32)
    data = data1 + data2
    data = data / np.max(np.abs(data)) #normalisierung
    print(freq1[FreqPos[0]], freq2[FreqPos[1]])
    return data

def PlayAudio(output_bytes):
	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sr, output=True)
	start_time = time.time()
	stream.write(output_bytes)

def ButtonPress(sender, app_data, user_data): # sender und app_data sind benötigt, dass user_data richtig funktioniert/zugeordnet wird
	output = (vol * GenerateSine(user_data)).tobytes()
	PlayAudio(output)

def AddButtons():
	grid.push(dpg.add_button(parent=MainWindow,label="1", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [0,0]), 0, 0)
	grid.push(dpg.add_button(parent=MainWindow,label="2", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [1,0]), 1, 0)
	grid.push(dpg.add_button(parent=MainWindow,label="3", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [2,0]), 2, 0)
	grid.push(dpg.add_button(parent=MainWindow,label="A", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [3,0]), 3, 0)

	grid.push(dpg.add_button(parent=MainWindow,label="4", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [0,1]), 0, 1)
	grid.push(dpg.add_button(parent=MainWindow,label="5", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [1,1]), 1, 1)
	grid.push(dpg.add_button(parent=MainWindow,label="6", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [2,1]), 2, 1)
	grid.push(dpg.add_button(parent=MainWindow,label="B", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [3,1]), 3, 1)

	grid.push(dpg.add_button(parent=MainWindow,label="7", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [0,2]), 0, 2)
	grid.push(dpg.add_button(parent=MainWindow,label="8", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [1,2]), 1, 2)
	grid.push(dpg.add_button(parent=MainWindow,label="9", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [2,2]), 2, 2)
	grid.push(dpg.add_button(parent=MainWindow,label="C", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [3,2]), 3, 2)

	grid.push(dpg.add_button(parent=MainWindow,label="*", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [0,3]), 0, 3)
	grid.push(dpg.add_button(parent=MainWindow,label="0", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [1,3]), 1, 3)
	grid.push(dpg.add_button(parent=MainWindow,label="#", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [2,3]), 2, 3)
	grid.push(dpg.add_button(parent=MainWindow,label="D", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=ButtonPress, user_data = [3,3]), 3, 3)

MainWindow = dpg.add_window(width=WindowSize[0], height=WindowSize[1], tag="PrimaryWindow")
grid = dpgGrid.Grid(4, 4, MainWindow)

AddButtons()

with dpg.item_handler_registry() as window_hr:
    dpg.add_item_visible_handler(callback=grid)
dpg.bind_item_handler_registry(MainWindow, window_hr)

dpg.set_primary_window("PrimaryWindow", True)
dpg.start_dearpygui()