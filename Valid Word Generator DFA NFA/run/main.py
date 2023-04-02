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
    Label(win, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).pack(side = BOTTOM, padx = 10, pady = 10)
    #adjust choosing window to primary monitor (primary monitor set in windows)
    win.geometry(f"{int( primary_monitor[2] ) // 3}x{int( primary_monitor[3] ) // 4}")
    win.geometry(f"+{int( primary_monitor[2]) // 2}+{int( primary_monitor[3] ) // 2}")
    winw = int ( primary_monitor[2] ) // 4
    winh = int ( primary_monitor[3] ) // 4
    def exit():
        win.destroy()
        quit()
    Button(win , text="Exit" , bg="#FE736F" , font=dfont , command = exit).place( x=10 , y=10 )
    Label(win, text = "Write the monitor number you want to use", font = dfont, bg = dtcolor).pack(side = TOP, padx = 10, pady = 10)
    #text_choose = Label(win, text = "Write the monitor number you want to use")
    #text_choose.pack()
    mon_num = Text(win, width = int( 0.1 * winw ), height = int( 0.02 * winh ), font = dfont, bg = dtcolor)
    mon_num.pack(padx = 10, pady = 10)
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

def draw_main():
    global window
    global winw
    global winh
    for wid in window.slaves():
        wid.forget()
    def exit():
        window.destroy()
        quit()
    Button( window , text="Exit" , bg="#FE736F" , font=dfont , command = exit ).place( x=10 , y=10 )
    Label(window, text = "Choose desired project", font = dfont, bg = dtcolor).pack(side = TOP, padx = int(0.05 * winw), pady = int(0.05 * winh))
    Button(window, text = "Word Checker", font = dfont, bg = dtcolor, command = wordcheck).pack(side = TOP, padx = 10, pady = 30)
    Button(window, text = "Valid Word Generator", font = dfont, bg = dtcolor, command = wordgen).pack(side = TOP, padx = 10, pady = 15)
    Label(window, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).pack(side = BOTTOM, padx = int(0.05 * winw), pady = int(0.05 * winh))
def wordcheck():
    global window
    global winw
    global winh
    print(winw, winh)
    for wid in window.slaves():
        wid.forget()
    Label(window, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).pack(side = BOTTOM, padx = int(0.05 * winw), pady = int(0.05 * winh))
    def exit():
        return draw_main()
    Button(window, text = "Back", font = dfont, bg = dtcolor, command = exit).pack(side = BOTTOM, padx = 5, pady = 5)
    Label(text = "Stare initiala", font = dfont, bg = dtcolor).pack(side = LEFT, padx = 5, pady = 5)
    stareinit = Text(window, font = dfont, bg = dtcolor, width = int(0.01 * winw), height = int(0.01 * winh))#, width = int (0.4 * winw), height = int(0.4 * winh))
    stareinit.pack(side = LEFT, padx = 10, pady = 10)
    Label(text = "Stari finale", font = dfont, bg = dtcolor).pack(side = LEFT, padx = 5, pady = 5)
    starfin = Text(window, font = dfont, bg = dtcolor, width = int(0.01 * winw), height = int(0.01 * winh))
    starfin.pack(side = LEFT, padx = 10, pady = 10)
    Label(text = "Tranzitii sub forma: stare caracter stare ( exemplu: q1 a q2)", font = dfont, bg = dtcolor).pack(side = LEFT, padx = 5, pady = 5)
    tranziti = Text(window, font = dfont, bg = dtcolor)
    tranziti.pack(side = LEFT, padx = 10, pady = 10)
    word = Text(window, font = dfont, bg = dtcolor, width = int(0.2 * winw))
    word.pack(side = RIGHT, padx = 10, pady = 10)

def wordgen():
    global window

choose_monitor()
window = Tk()
window.configure(bg = dmcolor)
window.title("LFA Projects Made by Gherca Darius")
window.geometry(f"{int(0.8 * int( mon_prin[2] ))}x{int(0.8 * int ( mon_prin[3] ))}")
window.geometry(f"+{mon_prin[0]}+{mon_prin[1]}")
winw = int( mon_prin[ 2 ] )
winh = int( mon_prin[ 3 ] )
draw_main()
window.mainloop()