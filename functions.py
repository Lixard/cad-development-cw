import os
from stat import FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_NORMAL
from time import sleep
from win32api import *
from win32file import *
from win32clipboard import *
from win32con import *
from win32ctypes import *
from win32file import *

# file system
def get_logical_drive_strings():
    drives = GetLogicalDriveStrings()
    return [x.rstrip("\\") for x in drives.split('\000') if x]


def get_current_directory():
    return os.getcwd()


def get_file_attributes(path: str):
    return GetFileAttributes(path)


def set_current_directory(path: str):
    SetCurrentDirectory(path)
    return get_current_directory()


def set_file_attributes(path: str, type):
    return SetFileAttributes(path, type)


def create_file(path: str):
    CreateFile()


def read_file(path: str):
    ReadFile()


# manual input devices
def get_keyboard_type():
    pass
    ## TODO


def get_keyboard_state():
    arr = GetKeyboardState()
    if arr[VK_CAPITAL]:
        print("Caps lock is active")
    else:
        print("Caps lock is not active") 


def get_cursor_pos():
    return GetCursorPos()


def get_mouse_keyboard_state():
    print(VK_LBUTTON)
    x = 0
    while not x:
        state = GetKeyboardState()
        x = state[VK_XBUTTON1]
        print(x)
        sleep(0.5)
        


def clip_cursor():
    pass


def set_cursor_pos():
    pass


def system_parameters_info():
    pass


# videosystem
def get_system_metrics():
    pass


def get_device_caps():
    pass


def enum_display_setting():
    pass


def set_sys_colors():
    pass


def change_display_setting():
    pass


# printer
def get_profile_string():
    pass


def device_capabilities():
    pass


def print_dlg():
    pass


def write_file():
    pass


def bit_blt():
    pass


# com-port

# настройка параметров приемной стороны

# прием текста

if __name__ == "__main__":
    print(get_mouse_keyboard_state())