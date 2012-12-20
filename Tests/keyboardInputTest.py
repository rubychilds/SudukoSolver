import pythoncom, pyHook, sys

def OnKeyboardEvent(event):
    x = chr(event.Ascii)
    print "Key: ", chr(event.Ascii)
    #do something here
    #x can be a conditional for something
    return True #,return x
    
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages() #will wait forever