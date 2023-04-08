import os, win32api
import subprocess
import multiprocessing
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
    win.geometry(f"{int (int( primary_monitor[2] ) / 2.5)}x{int (int( primary_monitor[3] ) / 2.5)}")
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
    print( os.getcwd( ) + "@")
    for wid in window.grid_slaves():
        wid.destroy()
    def exit():
        window.destroy()
        quit()
    Button( window , text="Exit" , bg="#FE736F" , font=dfont , command = exit ).grid(row = 0, column = 0)
    Label(window, text = "Choose desired project", font = dfont, bg = dtcolor).grid(row = 1, column = 1)
    Button(window, text = "Word Checker", font = dfont, bg = dtcolor, command = wordcheck).grid(row = 2, column = 1)
    Button(window, text = "Valid Word Generator", font = dfont, bg = dtcolor, command = wordgen).grid(row = 3, column = 1)
    Label(window, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).grid(row = 4, column = 0)
def wordgen():
    global window
    global winw
    global winh
    print(winw, winh)
    for wid in window.slaves():
        wid.destroy()
    #Label(window, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).pack(side = BOTTOM, padx = int(0.05 * winw), pady = int(0.05 * winh))
    Label(window, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).grid(row = 5, column = 0)
    def exit():
        window.destroy()
        quit()
    Button( window , text="Exit" , bg="#FE736F" , font=dfont , command = exit ).grid(row = 0, column = 0)
    def wexit():
        return draw_main()
    Button(window, text = "Back", font = dfont, bg = dtcolor, command = wexit).grid(row = 5, column = 2)
    Label(window, text = "Word Generator", font = dfont, bg = dtcolor).grid(row = 0, column = 1)
    Label(text = "Initial State", font = dfont, bg = dtcolor).grid(row = 1, column = 0)
    stareinit = Text(window, font = dfont, bg = dtcolor, width = int(0.01 * winw), height = int(0.01 * winh))#, width = int (0.4 * winw), height = int(0.4 * winh))
    stareinit.grid(row = 2, column = 0)
    Label(text = "Final States", font = dfont, bg = dtcolor).grid(row = 3, column = 0)
    starfin = Text(window, font = dfont, bg = dtcolor, width = int(0.01 * winw), height = int(0.01 * winh))
    starfin.grid(row = 4, column = 0)
    Label(text = "Transitions( example: q1 a q2)", font = dfont, bg = dtcolor).grid(row = 1, column = 1)
    tranziti = Text(window, font = dfont, bg = dtcolor)
    tranziti.grid(row = 2, column = 1, rowspan = 2)
    def bwrite():
        os.chdir( 'wordgen/bin/Debug' )
        #finput = '.\wordgen' + chr(92) + 'bin\Debug\input.txt'
        with open("input.in", "w") as f:
            sint = stareinit.get( "1.0" , 'end-1c' )
            f.write(sint + "\n")
            sfin = starfin.get("1.0", 'end-1c')
            sfin = [x for x in sfin.split()]
            f.write(str( len(sfin) ) + "\n")
            for el in sfin:
                f.write(el + "\n")
            trans = tranziti.get("1.0", 'end-1c')
            print("@\n" + trans)
            f.write(trans)
            f.close()
        os.chdir( '..' )
        os.chdir( '..' )
        os.chdir( '..' )
        return
    Button(window, text = "Write", font = dfont, bg = dtcolor, command = bwrite).grid(row = 4, column = 1)
    def wgen():
        os.chdir( 'wordgen/bin/Debug' )
        #fcuv = '.\wordgen' + chr(92) + 'bin\Debug\word.txt'
        with open("word.in", 'w') as f:
            scuv = word.get("1.0", 'end-1c')
            f.write(scuv)
            f.close()
        #exec_pt = '.\wordgen'+ chr(92) + 'bin\Debug\wordgen.exe'
        with open("input.in", "r") as g:
            for linie in g.readlines():
                print(linie)
            g.close()
        with open("output.txt", "w") as g:
            g.write("")
            g.close()
        #subprocess.run(["./wordgen/bin/Debug/wordgen.exe", ""])
        print(os.getcwd())
        os.system("wordgen.exe")
        print(os.getcwd())
        #gcuv = '.\wordgen' + chr(92) + 'bin\Debug\output.txt'
        while word.get("1.0", 'end-1c'):
            word.delete(1.0)
        with open("output.txt", "r") as g:
            for linie in g:
                word.insert(END, linie)
            g.close()
        os.chdir( '..' )
        os.chdir( '..' )
        os.chdir( '..' )
        print(os.getcwd())
        return
    Button(window, text = "Generate words", font = dfont, bg = dtcolor, command = wgen).grid(row = 1, column = 2)
    word = Text(window, font = dfont, bg = dtcolor, width = int(0.02 * winw), height = int(0.02 * winh))
    word.grid(row = 2, column = 2, rowspan = 2)
    Label(window, text = "Write in the text box the required length of the \n words generated, and then press generate words", font = dfont, bg = dtcolor).grid(row = 4, column = 2)

def wordcheck():
    global window
    global winw
    global winh
    print( winw , winh )
    for wid in window.slaves( ) :
        wid.destroy( )
    # Label(window, text = "Made by Gherca Darius", font = dfont, bg = dtcolor).pack(side = BOTTOM, padx = int(0.05 * winw), pady = int(0.05 * winh))
    Label( window , text="Made by Gherca Darius" , font=dfont , bg=dtcolor ).grid( row=5 , column=0 )
    def exit() :
        window.destroy( )
        quit( )
    Button( window , text="Exit" , bg="#FE736F" , font=dfont , command=exit ).grid( row=0 , column=0 )
    def wexit() :
        return draw_main( )
    Button( window , text="Back" , font=dfont , bg=dtcolor , command=wexit ).grid( row=5 , column=2 )
    Label( window , text="Word Checker" , font=dfont , bg=dtcolor ).grid( row=0 , column=1 )
    Label( window, text = "Initial State" , font=dfont , bg=dtcolor ).grid( row=1 , column=0 )
    stareinit = Text( window , font=dfont , bg=dtcolor , width=int( 0.01 * winw ) , height=int( 0.01 * winh ) )  # , width = int (0.4 * winw), height = int(0.4 * winh))
    stareinit.grid( row=2 , column=0 )
    Label( text="Final states" , font=dfont , bg=dtcolor ).grid( row=3 , column=0 )
    starfin = Text( window , font=dfont , bg=dtcolor , width=int( 0.01 * winw ) , height=int( 0.01 * winh ) )
    starfin.grid( row=4 , column=0 )
    Label( text="Transitions( example: q1 a q2)" , font=dfont , bg=dtcolor ).grid( row=1 , column=1 )
    tranziti = Text( window , font=dfont , bg=dtcolor )
    tranziti.grid( row=2 , column=1 , rowspan=2 )

    def bwrite() :
        os.chdir( ".." )
        os.chdir( 'wordcheck/bin/Debug' )
        # finput = '.\wordgen' + chr(92) + 'bin\Debug\input.txt'
        with open( "input.in" , "w" ) as f :
            sint = stareinit.get( "1.0" , 'end-1c' )
            f.write( sint + "\n" )
            sfin = starfin.get( "1.0" , 'end-1c' )
            sfin = [ x for x in sfin.split( ) ]
            f.write( str( len( sfin ) ) + "\n" )
            for el in sfin :
                f.write( el + "\n" )
            trans = tranziti.get( "1.0" , 'end-1c' )
            print( "@\n" + trans )
            f.write( trans )
            f.close( )
        os.chdir( '..' )
        os.chdir( '..' )
        os.chdir( '..' )
        return

    Button( window , text="Write" , font=dfont , bg=dtcolor , command=bwrite ).grid( row=4 , column=1 )

    def wgen() :
        os.chdir( 'wordcheck/bin/Debug' )
        # fcuv = '.\wordgen' + chr(92) + 'bin\Debug\word.txt'
        with open( "word.in" , 'w' ) as f :
            scuv = word.get( "1.0" , 'end-1c' )
            f.write( scuv )
            f.close( )
        # exec_pt = '.\wordgen'+ chr(92) + 'bin\Debug\wordgen.exe'
        with open( "input.in" , "r" ) as g :
            for linie in g.readlines( ) :
                print( linie )
            g.close( )
        with open( "output.txt" , "w" ) as g :
            g.write( "" )
            g.close( )
        # subprocess.run(["./wordgen/bin/Debug/wordgen.exe", ""])
        print( os.getcwd( ) )
        os.system( "wordcheck.exe" )
        print( os.getcwd( ) )
        # gcuv = '.\wordgen' + chr(92) + 'bin\Debug\output.txt'
        while word.get( "1.0" , 'end-1c' ) :
            word.delete( 1.0 )
        with open( "output.txt" , "r" ) as g :
            for linie in g :
                word.insert( END , linie )
            g.close( )
        os.chdir( '..' )
        os.chdir( '..' )
        os.chdir( '..' )
        print( os.getcwd( ) )
        return

    Button( window , text="Check" , font=dfont , bg=dtcolor , command=wgen ).grid( row=1 , column=2 )
    word = Text( window , font=dfont , bg=dtcolor , width=int( 0.02 * winw ) , height=int( 0.02 * winh ) )
    word.grid( row=2 , column=2 , rowspan=2 )
    Label( window , text="Write in the text box the word to check" , font=dfont , bg=dtcolor ).grid( row=4 , column=2 )


os.chdir( ".." )
choose_monitor()
window = Tk()
window.configure(bg = dmcolor)
window.title("LFA Projects Made by Gherca Darius")
window.geometry(f"{int(0.9 * int( mon_prin[2] ))}x{int(0.9 * int ( mon_prin[3] ))}")
window.geometry(f"+{mon_prin[0]}+{mon_prin[1]}")
winw = int( mon_prin[ 2 ] )
winh = int( mon_prin[ 3 ] )
draw_main()
window.mainloop()