import os, win32api
from tkinter import *
from screeninfo import get_monitors

#def main()
mon_prin = []
dmcolor = "#D1F2EB"
dtcolor = "#EAFAF1"
dfont = ("Arial", 16)
def choose_monitor():
    monitors = []
    #save primary monitor index in monitors list
    primary_mon = 0
    act = 1
    # 0 - x; 1 - y; 2 - width; 3 - height; 6 - name; 7 - is_primary
    #create monitor info list
    for m in get_monitors():
        m = str(m)
        infol = m[8:-1]
        infol = infol.split(", ")
        for index in range(len(infol)):
            infol[index] = infol[index][infol[index].find("=")+1:]
        monitors.append(infol)
        #find primary monitor
        if infol[7] == True:
            primary_mon = act
        act += 1
    primary_monitor = monitors[primary_mon]
    win = Tk()
    win.configure(bg = dmcolor)
    Label(win, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).pack(side = BOTTOM)
    #adjust choosing window to primary monitor (primary monitor set in windows)
    win.geometry(f"{int( primary_monitor[2] ) // 3}x{int( primary_monitor[3] ) // 4}")
    win.geometry(f"+{int( primary_monitor[2]) // 2}+{int( primary_monitor[3] ) // 2}")
    winw = int ( primary_monitor[2] ) // 4
    winh = int ( primary_monitor[3] ) // 4
    Label(win, text = "Write the monitor number you want to use", font = dfont, bg = dtcolor).pack()
    #text_choose = Label(win, text = "Write the monitor number you want to use")
    #text_choose.pack()
    mon_num = Text(win, width = int( 0.1 * winw ), height = int( 0.02 * winh ), font = dfont, bg = dtcolor)
    mon_num.pack()
    x = 1
    #displaying on each monitor it's coresponding number
    for m in monitors:
        def toplev():
            monsel = Toplevel(win)
            monsel.geometry(f"+{m[0]}+{m[1]}")
            monsel.title(f"Monitor {x}")
            ntext = Label(monsel, text = f"Monitor {x}", font = ("Helvetica", 50))
            ntext.pack()
        toplev()
        x += 1
    #if button is pressed, we set that monitor as main and ignore the others
    def finish():
        global mon_prin
        number = mon_num.get( "1.0" , 'end-1c')
        number = int(number)
        mon_prin = monitors[number - 1]
        win.destroy()
    monbut_click = False
    monbut = Button(win, text = "Next", font = dfont, command = finish, bg = dtcolor)
    monbut.pack()
    win.mainloop()

choose_monitor()
window = Tk()
window.configure(bg = dmcolor)
window.title("LFA Projects Made by Gherca Darius")
window.geometry(f"{mon_prin[2]}x{mon_prin[3]}")
window.geometry(f"+{mon_prin[0]}+{mon_prin[1]}")
Label(window, text = "Choose desired project", font = dfont, bg = dtcolor).pack(side = TOP)

window.mainloop()