import enum
import JsonUtils as jsu
datafile='kits.json'
data=jsu.read(datafile)
import pyautogui as gui
import os
def setpaste(text:str=''):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

try:
    while 1:
        kitnames=[]
        for _,kit in enumerate(data):
            kitnames.append(kit['name'])
        mykit=gui.confirm('Select a kit:',"KitManager",kitnames)

        for _,kit in enumerate(data):
            if kit["name"]==mykit:
                wantkit=gui.confirm(f"{kit['description']}\ncopy {kit['name']} to clipboard?","KitManager",['yes','no'])
                if wantkit=='yes':
                    setpaste(kit['paste'])
                    gui.confirm(f"'{kit['paste']}'\n copied to clipboard",'KitManager',['ok'])
except KeyboardInterrupt:
    print('\nExiting...')
    exit()