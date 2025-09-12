import dearpygui.dearpygui as dpg
import numpy as np
import pyaudio
import time
import json

WindowSize = (480, 600)
srOptions = [8000, 22500, 44100, 48000, 96000, 192000]
freq1 = [1209, 1336, 1477, 1633]
freq2 = [697, 770, 852, 941]
ButtonLabels = ["1","2","3","A","4","5","6","B","7","8","9", "C", "*", "0", "#", "D"]
p = pyaudio.PyAudio()
standardSettings = {
	"volumeValue": 80,
	"soundDurValue": 0.4,
	"pauseDurValue": 0.01,
	"srSelection": "41000",
	"expandedNumpadValue": False
} 
"""
generates the sound with additive synthesis
the np.float32 is the standard python float() precision, np.float64 would bei double(). important to specify in for the np-array and the actual output. 
-> 32 bit depth, couldnt get 16 bit depth to work
"""
def generateSine(FreqPos): 
    sine1 = np.sin(2 * np.pi * np.arange(int(dpg.get_value("srMenu"))*dpg.get_value("soundDurValue"))* freq1[FreqPos[0]]/int(dpg.get_value("srMenu"))).astype(np.float32)
    sine2 = np.sin(2 * np.pi * np.arange(int(dpg.get_value("srMenu"))*dpg.get_value("soundDurValue"))* freq2[FreqPos[1]]/int(dpg.get_value("srMenu"))).astype(np.float32)
    sineAdded = sine1 + sine2
    sineAdded = (sineAdded / np.max(np.abs(sineAdded))) #normalisierung
    print(freq1[FreqPos[0]], freq2[FreqPos[1]])
    return sineAdded.astype(np.float32)

"""
starts audio output at current time, as a mono 32 bit depth audio. no audio file type because we dont write anything
"""
def playAudio(output_bytes):
	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=int(dpg.get_value("srMenu")), output=True)
	start_time = time.time()
	stream.write(output_bytes)

"""
scales the volume settings to n/100. i heard somewhere multiplication is faster than division, therefore n*0.01
sender and app_data are required for user_data to work properly(or at all), even if unused
"""
def buttonPress(sender, app_data, user_data):
	output = ((dpg.get_value("VolumeSettingSlider")*0.01) * generateSine(user_data)).tobytes()
	playAudio(output)

"""
function essentially consists of 2 parts:
1:
checks if user changes the numpad size, deletes the other size, as actual replacement is difficult. 
the else: pass clause is for the first startup of a session, as the toggleExpandedNumpad always has a value
-> the if no userdata is present it skips the deletions

2:
generates the small/large numpad, as a table of buttons.
callback=buttonPress triggers audio generation
"""
def addButtons(sender, app_data, user_data):
	if user_data == "checkboxValueChanged" and dpg.get_value("toggleExpandedNumpad") == True:
		dpg.delete_item("buttonTableSmall")
	elif user_data == "checkboxValueChanged" and dpg.get_value("toggleExpandedNumpad") == False:
		dpg.delete_item("buttonTableLarge")
	else:
		pass

	if dpg.get_value("expandedNumpadValue") == True:
		with dpg.table(header_row=False, tag="buttonTableLarge", parent="tabNumpad"):
			for i in range(4):
				dpg.add_table_column(tag=f"buttonTableLargeColum{i}")
			for i in range(0, 4):
				with dpg.table_row(tag=f"buttonTableLargeRow{i}"):
					for j in range(0, 4):
						dpg.add_button(label=f"{ButtonLabels[(3*i)+(j+i)]}", width=WindowSize[0]/5, height=WindowSize[1]/5, callback=buttonPress, user_data = [j,i])

	else:
		with dpg.table(header_row=False, tag="buttonTableSmall", parent="tabNumpad"):
			for i in range(3):
				dpg.add_table_column(tag=f"buttonTableSmallColum{i}")
			for i in range(0, 4):
				with dpg.table_row(tag=f"buttonTableSmallRow{i}"):
					for j in range(0, 3):
						dpg.add_button(label=f"{ButtonLabels[j+(4*i)]}", width=WindowSize[0]/3, height=WindowSize[1]/5, callback=buttonPress, user_data = [j,i])


"""
tries to read the settings.json file, if not present creates it and sets the settings to standart values
dumnps the json file in to the settingsDICT
"""
try:
	with open("settings.json") as file:
		settingsDICT = json.loads(file.read())
		print("settings.json read")
except (FileNotFoundError):
	print("settings file not found, creating a new one :)")
	file = open("settings.json", "x")
	with open("settings.json", "w") as file:
		file.write(json.dumps(standardSettings))
	settingsDICT = standardSettings


"""
https://dearpygui.readthedocs.io/en/latest/reference/dearpygui.html#dearpygui.dearpygui.create_context
"""
dpg.create_context()


"""
creates values usable (e.g. accessable and modifyable) by dearPyGUI. 
default/original values derived from the settingsDICT
"""
with dpg.value_registry():
    dpg.add_int_value(default_value=settingsDICT["volumeValue"], tag="volumeValue")
    dpg.add_float_value(default_value=settingsDICT["soundDurValue"], tag="soundDurValue")
    dpg.add_float_value(default_value=settingsDICT["pauseDurValue"], tag="pauseDurValue")
    dpg.add_bool_value(default_value=bool(settingsDICT["expandedNumpadValue"]), tag="expandedNumpadValue")

"""
window creation. self explanatory
"""
with dpg.window(tag="mainWindow"):
    with dpg.tab_bar(tag="tabBar") as tb:
        with dpg.tab(label="Numpad", tag="tabNumpad"):
        	addButtons(None, None, None)
        with dpg.tab(label="Settings", tag="tabSettings"):
        	dpg.add_slider_int(label="Volume", tag="VolumeSettingSlider", min_value=0, max_value=100, source="volumeValue")
        	dpg.add_slider_float(label="Sound Duration", tag="soundDurSlider", min_value=0.04, max_value=1, source="soundDurValue")
        	dpg.add_slider_float(label="Pause Duration", tag="pauseDurSlider", min_value=0.001, max_value=0.01, source="pauseDurValue")
        	dpg.add_combo(label="Sample Rate", tag="srMenu", items=srOptions, default_value=settingsDICT["srSelection"])
        	dpg.add_checkbox(label="Toggle expanded Numpad", tag="toggleExpandedNumpad", source="expandedNumpadValue", callback=addButtons, user_data="checkboxValueChanged")


"""
requiered for viewable/interactable window
"""
dpg.setup_dearpygui()
dpg.create_viewport(width=WindowSize[0], height=WindowSize[1], title="An actual Phone?!")
dpg.show_viewport()
dpg.set_primary_window("mainWindow", True)
dpg.start_dearpygui()

"""
after dpg.start_dearpygui() is over (when the dpg window is closed) fetches the current settings values and writes the into settingsDICT
"""
settingsDICT = {
	"volumeValue": dpg.get_value("volumeValue"),
	"soundDurValue": dpg.get_value("soundDurValue"),
	"pauseDurValue": dpg.get_value("pauseDurValue"),
	"srSelection": dpg.get_value("srMenu"),
	"expandedNumpadValue": dpg.get_value("expandedNumpadValue")
}


"""
dumps settingsDICT in to the settings.json file, which then is dumped in to settingsDICT at next startup
"""
with open("settings.json", "w") as file:
	file.write(json.dumps(settingsDICT))
	print("saved settings")

"""
after file modification ends dearPyGUI
"""
dpg.destroy_context()
