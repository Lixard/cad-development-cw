import tkinter as tk
from tkinter import LEFT, ttk, messagebox as mb, simpledialog as sd, filedialog as fd
import ctypes
from enum import Enum
import os
from time import sleep
from win32api import *
from win32file import *
from win32clipboard import *
from win32con import *
from win32ctypes import *
from win32file import *
from win32gui import *
from win32print import *
from pywintypes import DEVMODEType

class UI:
    def __init__(self) -> None:
        self._root = tk.Tk()
        self._root.title("Курсовая по разработке САПР бАП-181 Борисов Максим")
        self._root.resizable(False, False)
        self._main_window()
        self._root.mainloop()

    def _main_window(self) -> None:

        # fs
        file_system_label = ttk.Label(
            self._root, text="Дисковая и файловая система", font=("TKDefaultFont", 18)
        ).pack()

        # disk info
        fs_info_disk_label = ttk.Label(self._root, text="Информация о дисках").pack()
        fs_info_disk_frame = ttk.Frame(self._root)

        get_logical_drive_strings_btn = ttk.Button(
            fs_info_disk_frame,
            text="GetLogicalDriveStrings",
            command=self._get_logical_drive_strings_btn_clicked,
        ).pack(side=LEFT)
        get_drive_type_btn = ttk.Button(
            fs_info_disk_frame,
            text="GetDriveType",
            command=self._get_drive_type_btn_clicked,
        ).pack(side=LEFT)
        get_current_directory_btn = ttk.Button(
            fs_info_disk_frame,
            text="GetCurrentDirectory",
            command=self._get_current_directory_btn_clicked,
        ).pack(side=LEFT)
        fs_info_disk_frame.pack()

        # file dir info
        fs_info_file_dir_label = ttk.Label(
            self._root, text="Информация о файлах и директориях"
        ).pack()
        fs_info_file_dir_frame = ttk.Frame(self._root)

        get_file_attributes_btn = ttk.Button(
            fs_info_file_dir_frame,
            text="GetFileAttributes",
            command=self._get_file_attributes_btn_clicked,
        ).pack(side=LEFT)
        set_current_directory_btn = ttk.Button(
            fs_info_file_dir_frame,
            text="SetCurrentDirectory",
            command=self._set_current_directory_btn_clicked,
        ).pack(side=LEFT)
        fs_info_file_dir_frame.pack()

        # fs control functions
        fs_control_functions_label = ttk.Label(
            self._root, text="Управляющие функции"
        ).pack()
        fs_control_functions_frame = ttk.Frame(self._root)

        set_file_attributes_btn = ttk.Button(
            fs_control_functions_frame,
            text="SetFileAttributes",
            command=self._set_file_attributes_btn_clicked,
        ).pack(side=LEFT)
        create_file_btn = ttk.Button(
            fs_control_functions_frame,
            text="CreateFile",
            command=self._create_file_btn_clicked,
        ).pack(side=LEFT)
        read_file_btn = ttk.Button(
            fs_control_functions_frame,
            text="ReadFile",
            command=self._read_file_btn_clicked,
        ).pack(side=LEFT)
        fs_control_functions_frame.pack()

        # input devices
        inpt_devices_label = ttk.Label(
            self._root, text="Устройства ручного ввода", font=("TKDefaultFont", 18)
        ).pack()

        # keyboard info
        info_keyboard_label = ttk.Label(
            self._root, text="Информация о клавиатуре"
        ).pack()
        info_keyboard_frame = ttk.Frame(self._root)

        get_keyboard_type_btn = ttk.Button(
            info_keyboard_frame,
            text="GetKeyboardType",
            command=self._get_keyboard_type_btn_clicked,
        ).pack(side=LEFT)
        get_keyboard_state_btn = ttk.Button(
            info_keyboard_frame,
            text="GetKeyboardState",
            command=self._get_keyboard_state_btn_clicked,
        ).pack(side=LEFT)
        info_keyboard_frame.pack()

        # mouse info
        info_mouse_label = ttk.Label(self._root, text="Информация о мыши").pack()
        info_mouse_frame = ttk.Frame(self._root)

        get_cursor_pos_btn = ttk.Button(
            info_mouse_frame,
            text="GetCursorPos",
            command=self._get_cursor_pos_btn_clicked,
        ).pack(side=LEFT)
        info_mouse_frame.pack()

        # input devices control functions
        id_control_functions_label = ttk.Label(
            self._root, text="Управляющие функции"
        ).pack()
        id_control_functions_frame = ttk.Frame(self._root)

        clip_cursor_btn = ttk.Button(
            id_control_functions_frame,
            text="ClipCursor",
            command=self._clip_cursor_btn_clicked,
        ).pack(side=LEFT)
        set_cursor_pos_btn = ttk.Button(
            id_control_functions_frame,
            text="SetCursorPos",
            command=self._set_cursor_pos_btn_clicked,
        ).pack(side=LEFT)
        system_parameters_info_btn = ttk.Button(
            id_control_functions_frame,
            text="SystemParametersInfo",
            command=self._system_parameters_info_btn_clicked,
        ).pack(side=LEFT)
        id_control_functions_frame.pack()

        # video system
        videosystem_label = ttk.Label(
            self._root, text="Видеосистема", font=("TKDefaultFont", 18)
        ).pack()

        # video info
        v_info_functions_label = ttk.Label(
            self._root, text="Информационные функции"
        ).pack()
        v_info_functions_frame = ttk.Frame(self._root)

        get_system_metrics_btn = ttk.Button(
            v_info_functions_frame,
            text="GetSystemMetrics",
            command=self._get_system_metrics_btn_clicked,
        ).pack(side=LEFT)
        get_device_caps_btn = ttk.Button(
            v_info_functions_frame,
            text="GetDeviceCaps",
            command=self._get_device_caps_btn_clicked,
        ).pack(side=LEFT)
        enum_display_setting_btn = ttk.Button(
            v_info_functions_frame,
            text="EnumDisplaySetting",
            command=self._enum_display_setting_btn_clicked,
        ).pack(side=LEFT)
        v_info_functions_frame.pack()

        # video control functions
        v_control_functions_label = ttk.Label(
            self._root, text="Управляющие функции"
        ).pack()
        v_control_functions_frame = ttk.Frame(self._root)

        set_sys_colors_btn = ttk.Button(
            v_control_functions_frame,
            text="SetSysColors",
            command=self._set_sys_colors_btn_clicked,
        ).pack(side=LEFT)
        change_display_setting_btn = ttk.Button(
            v_control_functions_frame,
            text="ChangeDisplaySetting",
            command=self._change_display_setting_btn_clicked,
        ).pack(side=LEFT)
        v_control_functions_frame.pack()

        # printer
        printer_label = ttk.Label(
            self._root, text="Принтер", font=("TKDefaultFont", 18)
        ).pack()
        printer_frame = ttk.Frame(self._root)

        get_profile_string_btn = ttk.Button(
            printer_frame,
            text="GetProfileString",
            command=self._get_profile_string_btn_clicked,
        ).pack(side=LEFT)
        device_capabilities_btn = ttk.Button(
            printer_frame,
            text="DeviceCapabilities",
            command=self._device_capabilities_btn_clicked,
        ).pack(side=LEFT)
        print_dlg_btn = ttk.Button(
            printer_frame, text="PrintDlg", command=self._print_dlg_btn_clicked
        ).pack(side=LEFT)
        write_file_btn = ttk.Button(
            printer_frame, text="WriteFile", command=self._write_file_btn_clicked
        ).pack(side=LEFT)
        bit_blt_btn = ttk.Button(
            printer_frame, text="BitBlt", command=self._bit_blt_btn_clicked
        ).pack(side=LEFT)
        printer_frame.pack()

    def _get_logical_drive_strings_btn_clicked(self):
        mb.showinfo("GetLogicalDriveStrings", f"Доступные диски: {' '.join(get_logical_drive_strings())}")

    def _get_drive_type_btn_clicked(self):
        drive = sd.askstring("GetDriveType", "Какой диск необходимо обнаружить?")
        if drive is None: return
        res = get_drive_type(drive)
        if res == DRIVE_UNKNOWN:
            msg = "Диск неопознан"
        elif res == DRIVE_NO_ROOT_DIR:
            msg = "Неправильно указан путь"
        elif res == DRIVE_REMOVABLE:
            msg = "Диск является съемным носителем"
        elif res == DRIVE_FIXED:
            msg = "Диск является жестким диском"
        elif res == DRIVE_REMOTE:
            msg = "Диск является удаленным (сетевым)"
        elif res == DRIVE_CDROM:
            msg = "Диск является CDROM"
        elif res == DRIVE_RAMDISK:
            msg = "Диск является оперативной памятью"
            
        mb.showinfo("GetDriveType", msg)

    def _get_current_directory_btn_clicked(self):
        mb.showinfo("GetCurrentDirectory", f"Текущая директория: {get_current_directory()}")

    def _get_file_attributes_btn_clicked(self):
        path = fd.askopenfilename()
        if path == "": return
        res = get_file_attributes(path)
        
        if res == FILE_ATTRIBUTE_ARCHIVE:
            msg = "Архивный файл"
        elif res == FILE_ATTRIBUTE_DIRECTORY:
            msg = "Папка"
        elif res == FILE_ATTRIBUTE_HIDDEN:
            msg = "Спрятан"
        elif res == FILE_ATTRIBUTE_NORMAL:
            msg = "У файла нет особых атрибутов"
        elif res == FILE_ATTRIBUTE_SYSTEM:
            msg = "Зарезервирован системой"
        
        mb.showinfo("GetFileAttributes", msg)

    def _set_current_directory_btn_clicked(self):
        path = fd.askdirectory()
        if path == "": return
        res = set_current_directory(path)
        
        mb.showinfo("SetCurrentDirectory", f"Текущая директория изменена на: {res}")

    def _set_file_attributes_btn_clicked(self):
        path = fd.askopenfilename()
        if path == "": return
        res = set_file_attributes(path)
        
        mb.showinfo("SetFileAttributes", "Файл спрятан")
        

    def _create_file_btn_clicked(self):
        path = fd.asksaveasfilename()
        if path == "": return
        res = create_file(path)
        
        mb.showinfo("CreateFile", "Файл создан")

    def _read_file_btn_clicked(self):
        path = fd.askopenfilename()
        if path == "": return
        res = read_file(path)
        
        mb.showinfo("ReadFile", "Содержимое файла:\n" + res)
        pass

    def _get_keyboard_type_btn_clicked(self):
        res = get_keyboard_type()
        if res[0] == 4:
            kb_type = "Enhanced 101- or 102-key keyboards (and compatibles)"
        else: 
            kb_type = "Неизвестный тип клавиатуры"
        
        mb.showinfo("GetKeyboardType", f"Тип клавиатуры: {kb_type}\nКоличество функциональных клавиш: {res[2]}")


    def _get_keyboard_state_btn_clicked(self):
        x = get_keyboard_state()
        
        if x:
            msg = "CAPS LOCK активен"
        else:
            msg = "CAPS LOCK не активен"    
        
        mb.showinfo("GetKeyboardState", msg)

    def _get_cursor_pos_btn_clicked(self):
        ox, oy = get_cursor_pos()
        mb.showinfo("GetCursorPos", f"Позиция курсора: {ox}, {oy}")

    def _clip_cursor_btn_clicked(self):
        mb.showinfo("ClipCursor", "Курсор будет прикреплен к левому верхнему углу в течении 5 секунд")
        clip_cursor()

    def _set_cursor_pos_btn_clicked(self):
        x = sd.askinteger("SetCursorPos", "Укажите x")
        y = sd.askinteger("SetCursorPos", "Укажите y")
        
        set_cursor_pos(x, y)
        mb.showinfo("SetCursorPos", f"Курсор перемещен на координаты ({x}, {y})")

    def _system_parameters_info_btn_clicked(self):
        path = fd.askopenfilename(initialdir="C:\\Windows\\web\\wallpaper\\Windows")
        mb.showinfo("SystemParametersInfo", "Изображение рабочего стола будет изменено на 15 секунд")
        system_parameters_info(path)

    def _get_system_metrics_btn_clicked(self):
        mb.showinfo("GetSystemMetrics", f"Количество мониторов в системе: {get_system_metrics()}")

    def _get_device_caps_btn_clicked(self):
        horz, vert = get_device_caps()
        mb.showinfo("GetDeviceCaps", f"Горизонтальный размер экрана: {horz}\nВертикальный размер экрана: {vert}")

    def _enum_display_setting_btn_clicked(self):
        mb.showinfo("EnumDisplaySetting", enum_display_setting())

    def _set_sys_colors_btn_clicked(self):
        set_sys_colors()

    def _change_display_setting_btn_clicked(self):
        x = sd.askinteger("ChangeDisplaySetting", "Укажите x")
        y = sd.askinteger("ChangeDisplaySetting", "Укажите y")
        
        mb.showinfo("ChangeDisplaySetting", "Монитор изменит разрешение на 10 секунд")
        change_display_setting(x, y)

    def _get_profile_string_btn_clicked(self):
        name, driver, port = get_profile_string().split(",")
        mb.showinfo("GetProfileString", f"Название принтера: {name}\nДрайвер: {driver}\nПорт: {port}")

    def _device_capabilities_btn_clicked(self):
        max, min = device_capabilities()
        mb.showinfo("DeviceCapabilities", f"Максимальный размер листа: {max}\nМинимальный размер листа: {min}")

    def _print_dlg_btn_clicked(self):
        print_dlg()

    def _write_file_btn_clicked(self):
        sd.askstring("WriteFile", "Введите строку для печати")
        write_file()

    def _bit_blt_btn_clicked(self):
        bit_blt()


# file system
def get_logical_drive_strings() -> list[str]:
    drives = GetLogicalDriveStrings()
    return [x.rstrip("\\") for x in drives.split('\000') if x]


def get_drive_type(drive):
    return GetDriveType(drive)


def get_current_directory():
    return os.getcwd()


def get_file_attributes(path: str):
    return GetFileAttributes(path)


def set_current_directory(path: str):
    SetCurrentDirectory(path)
    return get_current_directory()


def set_file_attributes(path: str):
    return SetFileAttributes(path, FILE_ATTRIBUTE_HIDDEN)


def create_file(path: str):
    with open(path, "w") as f:
        f.write("")


def read_file(path: str):
    with open(path, "r") as f:
        return f.read()


# manual input devices
def get_keyboard_type():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    result = user32.GetKeyboardType(0)
    result1 = user32.GetKeyboardType(1)
    result2 = user32.GetKeyboardType(2)
    return (result, result1, result2)


def get_keyboard_state():
    arr = GetKeyboardState()
    if arr[VK_CAPITAL]:
        return True
    else:
        return False 


def get_cursor_pos():
    return GetCursorPos()


def clip_cursor():
    ClipCursor((1, 1, 1, 1))
    sleep(5)
    ClipCursor((0, 0, 0, 0))


def set_cursor_pos(x, y):
    SetCursorPos((x, y))
    return GetCursorPos()


def system_parameters_info(path):
    before = SystemParametersInfo(SPI_GETDESKWALLPAPER)
    SystemParametersInfo(SPI_SETDESKWALLPAPER, path)
    sleep(10)
    SystemParametersInfo(SPI_SETDESKWALLPAPER, before)

# videosystem
def get_system_metrics():
    return GetSystemMetrics(SM_CMONITORS)


def get_device_caps():
    return (GetDeviceCaps(GetDC(0), HORZRES), GetDeviceCaps(GetDC(0), VERTRES))


def enum_display_setting():
    x = EnumDisplaySettings(None, ENUM_CURRENT_SETTINGS).DisplayOrientation
    if x == DMDO_DEFAULT:
        return "Классическая ориентация монитора"
    elif x == DMDO_90:
        return "Монитор повернут на 90 градусов"
    elif x == DMDO_180:
        return "Монитор повернут на 180 градусов"
    elif x == DMDO_270:
        return "Монитор повернут на 270 градусов"


def set_sys_colors():
    pass
    #color = ctypes.wintypes.RGB(225, 255, 255)
    #ctypes.windll.user32.SetSysColors(1, ctypes.byref(ctypes.c_int(COLOR_BTNTEXT)), ctypes.byref(ctypes.c_int(color)))
    #sleep(10)
    #color2 = ctypes.wintypes.RGB(255, 255, 255)
    #ctypes.windll.user32.SetSysColors(1, ctypes.byref(ctypes.c_int(COLOR_BTNTEXT)), ctypes.byref(ctypes.c_int(color)))


def change_display_setting(x, y):
    devmode = EnumDisplaySettings()
    devmode.PelsWidth = x
    devmode.PelsHeight = y
    ChangeDisplaySettings(devmode, 0)
    sleep(10)
    ChangeDisplaySettings(None, 0)


# printer
def get_profile_string():
    return GetProfileVal("windows","device","")


def device_capabilities():
    printers = EnumPrinters(PRINTER_ENUM_LOCAL)
    return (DeviceCapabilities(printers[0][2], "", DC_MAXEXTENT), DeviceCapabilities(printers[0][2], "", DC_MINEXTENT))


def print_dlg():
    _print()


def write_file():
    _print()


def bit_blt():
    _print()


def _print():
    os.startfile("C:\\123\\TEXT.txt", "print")

UI()
