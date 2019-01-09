
#扫雷游戏窗口
class_name = "TMain"
title_name = "Minesweeper Arbiter "
hwnd = win32gui.FindWindow(class_name, title_name)

#窗口坐标
left = 0
top = 0
right = 0
bottom = 0

if hwnd:
   print("找到窗口")
   left, top, right, bottom = win32gui.GetWindowRect(hwnd)
   #win32gui.SetForegroundWindow(hwnd)
   print("窗口坐标：")
   print(str(left)+' '+str(right)+' '+str(top)+' '+str(bottom))
else:
   print("未找到窗口")
