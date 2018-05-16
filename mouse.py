import time
import win32api,win32con
# function responsible for leftClick()
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("click")
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print(leftDown)
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ("left release")
def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))
    # function getting the cordinate of our mouse
def get_cords():
    x,y = win32api.GetCursorPos()
    print(x,y)

############################################################################################
# We can actually use this cord to open any application e.g game,while you relax and watch your machine
#     working for you all you need is get the cord of each button and do something like:
#     def startApp()
#     mousePos(200,300) #cord of buttons(200,300) this will actually do the first clicking for you
#     leftClick()#operation to perform,do left click
#     time.sleep(.1)period for evaluation
#
#     #second button
#     repeat mousePos() action
#     leftClick() action
#     time.sleep()action and boom you are in.