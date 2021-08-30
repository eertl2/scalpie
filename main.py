from scheduler import Scheduler
import sys
import os
import dbg
import traceback

dbg = dbg.Dbg()

if __name__ == "__main__":
    try:
        scheduler = Scheduler()
        scheduler.run()
    except: 
        dbg.debug("Program failed: " + traceback.format_exc())

#I seen somewhere to stick this in the main code for pyinstaller, no idea if it does anything or not
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)