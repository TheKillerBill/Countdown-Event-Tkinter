import tkinter
from tkinter import font
from tkinter import messagebox
import configparser
import time
import os
import playsound

def resize_Frame_EnterEvent(e): #Resize text with window
    global default_font, root
    default_font.configure( size = ( int(root.winfo_height()/1.15) + root.winfo_width())//85 )

def resize_Frame_Countdown(e):
    global Frame_Date, Frame_Time, Frame_CountdownButtons
    font_size = ( int(root.winfo_height()/1.15) + root.winfo_width())//60
    for children in Frame_Date.winfo_children():
        try:
            children.configure( font = ('TkDefaultFont', str(font_size) ) )
        except:
            pass
    for children in Frame_Time.winfo_children():
        try:
            children.configure( font = ('TkDefaultFont', str(font_size) ) )
        except:
            pass
    for children in Frame_CountdownButtons.winfo_children():
        try:
            children.configure( font = ('TkDefaultFont', str(font_size) ) )
        except:
            pass
    try:
        Label_EventName.configure( font = ('Segoe Print',str(( int(root.winfo_height()/1.15) + root.winfo_width())//40)) )
    except:
        Label_EventName.configure( font = ('TkDefaultFont',str(( int(root.winfo_height()/1.15) + root.winfo_width())//40)) )

def Start_Event():
    global Entry_EventName, Spinbox_DateYear, Spinbox_DateMonth, Spinbox_DateDay, Spinbox_DateHour,\
    Spinbox_DateMinute, Spinbox_DateSecond, Frame_EnterEvent, default_font, root, Timer_Identifier,\
    Frame_Countdown, Label_Year, Label_Month, Label_Day, Label_Hour, Label_Minute, Label_Second, Time_Left,\
    Frame_Date, Frame_Time, Label_EventName, Frame_CountdownButtons, Event_Saved
    if not ( Spinbox_DateYear.get().isdigit() and Spinbox_DateMonth.get().isdigit() and Spinbox_DateDay.get().isdigit()  ):
        messagebox.showerror('Error','Enter Date as digits')
        return
    elif not( Spinbox_DateHour.get().isdigit() and Spinbox_DateMinute.get().isdigit() and Spinbox_DateSecond.get().isdigit() ):
        messagebox.showerror('Error','Enter Time as digits')
        return
    if int(Spinbox_DateYear.get()) > 9999 or int(Spinbox_DateMonth.get()) > 12 or \
        int(Spinbox_DateDay.get()) > 31 or int(Spinbox_DateHour.get()) > 23 or \
        int(Spinbox_DateMinute.get()) > 59 or int(Spinbox_DateSecond.get()) > 59:
        messagebox.showerror('Error',"Wrong date formula entered")
        return
    Date_Now = time.strftime('%Y %m %d %H %M %S')   # Date_Now is the string of year month day etc..
    Date_Now = Date_Now.split()            # Date_Now is [year,month,day, etc...]
    if int(Spinbox_DateYear.get()) < int(Date_Now[0]):        #If year entered is lower than
        messagebox.showerror('Date','Date entered is in the past')  # the actual year
        return
    elif int(Spinbox_DateYear.get()) == int(Date_Now[0]):  #If year entered is the actual year
        if int(Spinbox_DateMonth.get()) < int(Date_Now[1]):       #If month entered is lower than
            messagebox.showerror('Date','Date entered is in the past') # actual month
            return
        elif int(Spinbox_DateMonth.get()) == int(Date_Now[1]): #Same for days and hours etc..
            if int(Spinbox_DateDay.get()) < int(Date_Now[2]):
                messagebox.showerror('Date','Date entered is in the past')
                return
            elif int(Spinbox_DateDay.get()) == int(Date_Now[2]):
                if int(Spinbox_DateHour.get()) < int(Date_Now[3]):
                    messagebox.showerror('Time','Time entered is in the past')
                    return
                elif int(Spinbox_DateHour.get()) == int(Date_Now[3]):
                    if int(Spinbox_DateMinute.get()) < int(Date_Now[4]):
                        messagebox.showerror('Time','Time entered is in the past')
                        return
                    elif int(Spinbox_DateMinute.get()) == int(Date_Now[4]):
                        if int(Spinbox_DateSecond.get()) < int(Date_Now[5]):
                            if Event_Saved == True:
                                Time_Reached()
                            else:
                                messagebox.showerror('Time','Time entered is in the past')
                            return
    if Entry_EventName.get() == '':
        messagebox.showwarning('Event Name','No Event Name entered')
    Frame_EnterEvent.pack_forget()
    Frame_Countdown = tkinter.Frame(root)
    Frame_Countdown.pack( fill = 'none', expand = True )
    Label_EventName = tkinter.Label(Frame_Countdown, text = Entry_EventName.get(), justify = 'center' )
    try:
        Label_EventName.configure( font = ('Segoe Print',str(( int(root.winfo_height()/1.15) + root.winfo_width())//60)) )
    except:
        Label_EventName.configure( font = ('TkDefaultFont',str(( int(root.winfo_height()/1.15) + root.winfo_width())//60)) )
    Label_EventName.grid(row = 0, columnspan = 10, pady = 30 )
    Years_Left = str(int(Spinbox_DateYear.get()) - int(Date_Now[0]))
    Months_Left = str(int(Spinbox_DateMonth.get()) - int(Date_Now[1]))
    Days_Left = str(int(Spinbox_DateDay.get()) - int(Date_Now[2]))
    Hours_Left = str(int(Spinbox_DateHour.get()) - int(Date_Now[3]))
    Minutes_Left = str(int(Spinbox_DateMinute.get()) - int(Date_Now[4]))
    Seconds_Left = str(int(Spinbox_DateSecond.get()) - int(Date_Now[5]))
    if int(Seconds_Left) < 0:
        Seconds_Left = str(int(Seconds_Left) + 60)
        Minutes_Left = str( int(Minutes_Left) - 1)
    if int(Minutes_Left) < 0:
        Minutes_Left = str( int(Minutes_Left) + 60)
        Hours_Left = str( int(Hours_Left) - 1)
    if int(Hours_Left) < 0:
        Hours_Left = str( int(Hours_Left) + 24)
        Days_Left = str( int(Days_Left) - 1)
    if int(Days_Left) < 0:
        if int(Months_Left) <= 0:
            Years_Left = str(int(Years_Left) - 1)
            Months_Left = str(int(Months_Left) + 12)
        if int(Months_Left) == 1 or int(Months_Left) == 3 or int(Months_Left) == 5 or int(Months_Left) == 7 or\
        int(Months_Left) == 8 or int(Months_Left) == 10 or int(Months_Left) == 12:
            Days_Left = str( int(Days_Left) + 30 )
        elif int(Months_Left) == 4 or int(Months_Left) == 6 or int(Months_Left) == 9 or int(Months_Left) == 11:
            Days_Left = str( int(Days_Left) + 29 )
        elif int(Months_Left) == 2:
            if int(Months_Left) % 4 == 0:
                if int(Months_Left) % 100 == 0:
                    if int(Months_Left) % 400 == 0:
                        Days_Left = str( int(Days_Left) + 28 )
                    else:
                        Days_Left = str( int(Days_Left) + 27 )
                else:
                    Days_Left = str( int(Days_Left) + 28 )
            else:
                Days_Left = str( int(Days_Left) + 27 )
        Months_Left = str( int(Months_Left) - 1 )
    if int(Months_Left) < 0:
        Years_Left = str(int(Years_Left) - 1)
        Months_Left = str(int(Months_Left) + 12)
    while len(Years_Left) < 4:
        Years_Left = '0' + Years_Left
    while len(Months_Left) < 2:
        Months_Left = '0' + Months_Left
    while len(Days_Left) < 2:
        Days_Left = '0' + Days_Left
    while len(Hours_Left) < 2:
        Hours_Left = '0' + Hours_Left
    while len(Minutes_Left) < 2:
        Minutes_Left = '0' + Minutes_Left
    while len(Seconds_Left) < 2:
        Seconds_Left = '0' + Seconds_Left
    Time_Left = [Years_Left, Months_Left, Days_Left, Hours_Left, Minutes_Left, Seconds_Left]
    Frame_Date = tkinter.Frame(Frame_Countdown)
    Frame_Date.grid( row = 1, column = 0, columnspan = 5, padx = 30 )
    Label_DD = tkinter.Label(Frame_Date, justify = 'center', text = 'Days' )
    Label_DD.grid( row = 0, column = 0 )
    Label_Day = tkinter.Label(Frame_Date, justify = 'center', text = Days_Left )
    Label_Day.grid(row = 1, column = 0 )
    Label_B1 = tkinter.Label(Frame_Date, justify = 'center', text = '-' )
    Label_B1.grid(row = 1, column = 1, padx = 20 )
    Label_MM = tkinter.Label(Frame_Date, justify = 'center', text = 'Months' )
    Label_MM.grid( row = 0, column = 2 )
    Label_Month = tkinter.Label(Frame_Date, justify = 'center', text = Months_Left )
    Label_Month.grid(row = 1, column = 2 )
    Label_B2 = tkinter.Label(Frame_Date, justify = 'center', text = '-' )
    Label_B2.grid(row = 1, column = 3, padx = 20 )
    Label_YY = tkinter.Label(Frame_Date, justify = 'center', text = 'Years' )
    Label_YY.grid( row = 0, column = 4 )
    Label_Year = tkinter.Label(Frame_Date, justify = 'center', text = Years_Left )
    Label_Year.grid(row = 1, column = 4 )
    Frame_Time = tkinter.Frame(Frame_Countdown )
    Frame_Time.grid( row = 1, column = 5, columnspan = 5, padx = 30 )
    Label_HH = tkinter.Label(Frame_Time, justify = 'center', text = 'Hours' )
    Label_HH.grid( row = 0, column = 0 )
    Label_Hour = tkinter.Label(Frame_Time, justify = 'center', text = Hours_Left )
    Label_Hour.grid(row = 1, column = 0 )
    Label_B3 = tkinter.Label(Frame_Time, justify = 'center', text = ':' )
    Label_B3.grid(row = 1, column = 1 )
    Label_MI = tkinter.Label(Frame_Time, justify = 'center', text = 'Minutes' )
    Label_MI.grid( row = 0, column = 2 )
    Label_Minute = tkinter.Label(Frame_Time, justify = 'center', text = Minutes_Left )
    Label_Minute.grid(row = 1, column = 2 )
    Label_B4 = tkinter.Label(Frame_Time, justify = 'center', text = ':' )
    Label_B4.grid(row = 1, column = 3 )
    Label_SS = tkinter.Label(Frame_Time, justify = 'center', text = 'Seconds' )
    Label_SS.grid( row = 0, column = 4 )
    Label_Second = tkinter.Label(Frame_Time, justify = 'center', text = Seconds_Left )
    Label_Second.grid(row = 1, column = 4 )
    Timer_Identifier = root.after( 1000, Run_Timer )
    font_size = ( int(root.winfo_height()/1.15) + root.winfo_width())//60
    for children in Frame_Date.winfo_children():
        try:
            children.configure( font = ('TkDefaultFont', str(font_size) ) )
        except:
            pass
    for children in Frame_Time.winfo_children():
        try:
            children.configure( font = ('TkDefaultFont', str(font_size) ) )
        except:
            pass
    Frame_CountdownButtons = tkinter.Frame( Frame_Countdown )
    Frame_CountdownButtons.grid( row = 2, columnspan = 10, pady = 40, sticky = 'NSEW' )
    tkinter.Grid.rowconfigure(Frame_CountdownButtons, 0, weight = 1)
    tkinter.Grid.columnconfigure(Frame_CountdownButtons, 0, weight = 1)
    tkinter.Grid.columnconfigure(Frame_CountdownButtons, 1, weight = 1)
    Save_Button = tkinter.Button( Frame_CountdownButtons, justify = 'center', text = 'Save', bd = 4 )
    Save_Button.configure( command = lambda: Save_Event(Entry_EventName, Spinbox_DateYear, Spinbox_DateMonth, Spinbox_DateDay, Spinbox_DateHour, Spinbox_DateMinute, Spinbox_DateSecond ) )
    Save_Button.grid( row = 0, column = 0, sticky = 'NSEW', padx = 15 )
    Reset_Button = tkinter.Button( Frame_CountdownButtons, justify = 'center', text = 'Reset', bd = 4 )
    Reset_Button.configure( command = Reset_Event)
    Reset_Button.grid( row = 0, column = 1, sticky = 'NSEW', padx = 15 )
    Frame_Countdown.bind('<Configure>', resize_Frame_Countdown)

def Save_Event(Entry_EventName, Spinbox_DateYear, Spinbox_DateMonth, Spinbox_DateDay, Spinbox_DateHour, Spinbox_DateMinute, Spinbox_DateSecond ):
    try:
        config = configparser.ConfigParser()
        config['Event Name'] = { 'Name' : Entry_EventName.get() }
        config['Date'] = { 'Year' : Spinbox_DateYear.get(), 'Month' : Spinbox_DateMonth.get(),
                            'Day' : Spinbox_DateDay.get() }
        config['Time'] = { 'Hour' : Spinbox_DateHour.get(), 'Minute' : Spinbox_DateMinute.get(),
                            'Second' : Spinbox_DateSecond.get() }
        with open('Config.ini','w') as configfile:
            config.write(configfile)
        messagebox.showinfo('Event saved', 'Your event has been saved!')
    except:
        messagebox.showerror('Error','Unable to save the event')

def Reset_Event():
    global Frame_Countdown, Frame_EnterEvent, Timer_Identifier, Frame_TimeReached
    try:
        root.after_cancel(Timer_Identifier)
        Frame_Countdown.pack_forget()
    except Exception as e:
        print(e)
    try:
        Frame_TimeReached.pack_forget()
    except Exception as e:
        print(e)
    Frame_EnterEvent.pack( fill = 'both', expand = True )
    for i in range(4):
        tkinter.Grid.rowconfigure(Frame_EnterEvent, i, weight = 1)
    for i in range(2):
        tkinter.Grid.columnconfigure(Frame_EnterEvent, i, weight = 1)
    if os.path.isfile('Config.ini'):
        os.remove('Config.ini')

def Run_Timer():
    global Label_Year, Label_Month, Label_Day, Label_Hour, Label_Minute, Label_Second, Time_Left, Timer_Identifier
    if int(Time_Left[5]) == 0:
        Time_Left[5] = '59'
        if int(Time_Left[4]) == 0:
            Time_Left[4] = '59'
            if int(Time_Left[3]) == 0:
                Time_Left[3] = '23'
                if int(Time_Left[2]) == 0:
                    Find_Month = ( int(time.strftime("%m")) + int(Time_Left[1] ) - 2 ) % 12
                    Find_Month += 1
                    if Find_Month == 1 or Find_Month == 3 or Find_Month == 5 or Find_Month == 7 or Find_Month == 8 \
                        or Find_Month == 10 or Find_Month == 12:
                        Time_Left[2] = '30'
                    elif Find_Month == 4 or Find_Month == 6 or Find_Month == 9 or Find_Month == 11:
                        Time_Left[2] = '29'
                    elif Find_Month == 2:
                        Find_Year = int(time.strftime("%Y")) + int(Time_Left[0]) + 1 
                        if Find_Year % 4 == 0:
                            if Find_Year % 100 == 0:
                                if Find_Year % 400 == 0:
                                    Time_Left[2] = '28'
                                else:
                                    Time_Left[2] = '27'
                            else:
                                Time_Left[2] = '28'
                        else:
                            Time_Left[2] = '27'
                    if int(Time_Left[1]) == 0:
                        Time_Left[1] = '11'
                        if int(Time_Left[0]) == 0:
                            Time_Reached()
                            return
                        else:
                            Time_Left[0] = str( int(Time_Left[0]) - 1)
                            while len( Time_Left[0] ) < 4:
                                Time_Left[0] = '0' + Time_Left[0]
                            Label_Year.configure( text = Time_Left[0] )
                    else:
                        Time_Left[1] = str( int(Time_Left[1]) - 1)
                        while len( Time_Left[1] ) < 2:
                            Time_Left[1] = '0' + Time_Left[1]
                    Label_Month.configure( text = Time_Left[1] )
                else:
                    Time_Left[2] = str( int(Time_Left[2]) - 1)
                    while len( Time_Left[2] ) < 2:
                        Time_Left[2] = '0' + Time_Left[2]
                Label_Day.configure( text = Time_Left[2] )
            else:
              Time_Left[3] = str( int(Time_Left[3]) - 1)
              while len( Time_Left[3] ) < 2:
                  Time_Left[3] = '0' + Time_Left[3]
            Label_Hour.configure( text = Time_Left[3] )
        else:
            Time_Left[4] = str( int(Time_Left[4]) - 1)
            while len( Time_Left[4] ) < 2:
                Time_Left[4] = '0' + Time_Left[4]
        Label_Minute.configure( text = Time_Left[4] )
    else:
        Time_Left[5] = str( int(Time_Left[5]) - 1)
        while len( Time_Left[5] ) < 2:
            Time_Left[5] = '0' + Time_Left[5]
    Label_Second.configure( text = Time_Left[5] )
    Timer_Identifier = root.after( 1000, Run_Timer)

def resize_Frame_TimeReached(e):
    global Label_TimeReached, Button_GoBack
    try:
        Label_TimeReached.configure( font = ('Segoe Print',str(( int(root.winfo_height()/1.15) + root.winfo_width())//40)) )
        Button_GoBack.configure( font = ('Segoe Print',str(( int(root.winfo_height()/1.15) + root.winfo_width())//40)) )
    except:
        Label_TimeReached.configure( font = ('TkDefaultFont',str(( int(root.winfo_height()/1.15) + root.winfo_width())//40)) )
        Button_GoBack.configure( font = ('TkDefaultFont',str(( int(root.winfo_height()/1.15) + root.winfo_width())//40)) )

def Time_Reached():
    global Timer_Identifier, root, Frame_Countdown, Entry_EventName, Label_TimeReached, Button_GoBack, Frame_TimeReached, Frame_EnterEvent
    try:
        root.after_cancel(Timer_Identifier)
        Frame_Countdown.pack_forget()
    except:
        pass
    Frame_EnterEvent.pack_forget()
    Frame_TimeReached = tkinter.Frame(root)
    Frame_TimeReached.pack( fill = 'both', expand = True )
    Label_TimeReached = tkinter.Label(Frame_TimeReached, text = Entry_EventName.get() + ' has arrived!', justify = 'center')
    if Entry_EventName.get() == '':
        Label_TimeReached.configure( text = 'The event has arrived!')
    Label_TimeReached.pack( fill = 'none', expand = True, side = 'top' )
    Button_GoBack = tkinter.Button(Frame_TimeReached, text = 'Back', justify = 'center', command = Reset_Event, bd = 4 )
    Button_GoBack.pack( fill = 'x', expand = True, side = 'bottom', pady = 30, padx = 40 )
    Frame_TimeReached.bind('<Configure>', resize_Frame_TimeReached)
    playsound.playsound('dev/1.mp3')

def Countdown():
    global default_font, root, Entry_EventName, Spinbox_DateYear, Spinbox_DateMonth, Event_Saved,\
    Spinbox_DateDay, Spinbox_DateHour, Spinbox_DateMinute, Spinbox_DateSecond, Frame_EnterEvent
    root = tkinter.Tk()
    root.title("Countdown Timer")
    root.iconbitmap( default = 'dev/chronometer.ico')
    default_font = tkinter.font.nametofont("TkDefaultFont")
    default_font.configure(size= (root.winfo_height() + root.winfo_width())//85 )
    ws = root.winfo_screenwidth() 
    hs = root.winfo_screenheight()      # Info to center the window on the screen
    x = (ws/2) - (760/2)
    y = (hs/2) - (300/2)
    root.geometry('760x300+%d+%d' % (x, y))
    root.option_add("*Font", default_font)
    Event_Saved = False
    Frame_EnterEvent = tkinter.Frame(root)
    Frame_EnterEvent.pack( fill = 'both', expand = True )
    for i in range(4):
        tkinter.Grid.rowconfigure(Frame_EnterEvent, i, weight = 1)
    for i in range(2):
        tkinter.Grid.columnconfigure(Frame_EnterEvent, i, weight = 1)
    Label_EventName = tkinter.Label(Frame_EnterEvent, text = 'Event Name:', justify = 'center')
    Label_EventName.grid( row = 0, column = 0, sticky = 'NSEW' )
    Entry_EventName = tkinter.Entry(Frame_EnterEvent, justify = 'center')
    Entry_EventName.grid( row = 0, column = 1, sticky = 'EW' )
    Label_Date = tkinter.Label(Frame_EnterEvent, text = 'Date:', justify = 'center')
    Label_Date.grid(row = 1, column = 0, sticky = 'NSEW')
    Frame_Date = tkinter.Frame(Frame_EnterEvent)
    Frame_Date.grid(row = 1, column = 1, sticky = 'EW')
    Label_DateYear = tkinter.Label(Frame_Date, text = 'Year', justify = 'center')
    Label_DateYear.grid(row = 0, column = 0, sticky = 'NSEW')
    Label_DateMonth = tkinter.Label(Frame_Date, text = 'Month', justify = 'center')
    Label_DateMonth.grid(row = 0, column = 1, sticky = 'NSEW')
    Label_DateDay = tkinter.Label(Frame_Date, text = 'Day', justify = 'center')
    Label_DateDay.grid(row = 0, column = 2, sticky = 'NSEW')
    Year_Now = time.strftime("%Y")
    Spinbox_DateYear = tkinter.Spinbox(Frame_Date, from_ = int(Year_Now), to = int(Year_Now) + 100, justify = 'center')
    Spinbox_DateYear.grid(row = 1, column = 0, sticky = 'NSEW')
    Spinbox_DateMonth = tkinter.Spinbox(Frame_Date, from_ = 1, to = 12, justify = 'center')
    Spinbox_DateMonth.grid(row = 1, column = 1, sticky = 'NSEW')
    Spinbox_DateDay = tkinter.Spinbox(Frame_Date, from_ = 1, to = 31, justify = 'center')
    Spinbox_DateDay.grid(row = 1, column = 2, sticky = 'NSEW')
    Label_Time = tkinter.Label(Frame_EnterEvent, text = 'Time:', justify = 'center')
    Label_Time.grid(row = 2, column = 0, sticky = 'NSEW')
    Frame_Time = tkinter.Frame(Frame_EnterEvent)
    Frame_Time.grid(row = 2, column = 1, sticky = 'EW')
    Label_DateHour = tkinter.Label(Frame_Time, text = 'Hour', justify = 'center')
    Label_DateHour.grid(row = 0, column = 0, sticky = 'NSEW')
    Label_DateMinute = tkinter.Label(Frame_Time, text = 'Minute', justify = 'center')
    Label_DateMinute.grid(row = 0, column = 1, sticky = 'NSEW')
    Label_DateSecond = tkinter.Label(Frame_Time, text = 'Second', justify = 'center')
    Label_DateSecond.grid(row = 0, column = 2, sticky = 'NSEW')
    Spinbox_DateHour = tkinter.Spinbox(Frame_Time, from_ = 00, to = 23, justify = 'center')
    Spinbox_DateHour.grid(row = 1, column = 0, sticky = 'NSEW')
    Spinbox_DateMinute = tkinter.Spinbox(Frame_Time, from_ = 00, to = 59, justify = 'center')
    Spinbox_DateMinute.grid(row = 1, column = 1, sticky = 'NSEW')
    Spinbox_DateSecond = tkinter.Spinbox(Frame_Time, from_ = 00, to = 59, justify = 'center')
    Spinbox_DateSecond.grid(row = 1, column = 2, sticky = 'NSEW')
    Button_Start = tkinter.Button(Frame_EnterEvent, text = 'Start', command = Start_Event, bd = 4 )
    Button_Start.grid(row = 3, columnspan = 2, sticky = 'EW' )
    for child in Frame_EnterEvent.winfo_children():
        child.grid_configure( padx= 20, pady=15 )
    if os.path.isfile('Config.ini'):
        config = configparser.ConfigParser()
        config.read('Config.ini')
        date = config['Date']['Year'] + '-' + config['Date']['Month'] + '-' + config['Date']['Day']
        date = date + '   ' + config['Time']['Hour'] + ':' + config['Time']['Minute'] + ':' + config['Time']['Second']
        if messagebox.askyesno('Event found','Event found with the name of ' + config['Event Name']['Name'] + '\nAt:\t' + date +'\nDo you want to load in that event?' ):
            Entry_EventName.insert(0, config['Event Name']['Name'])
            Spinbox_DateYear.delete(0,"end")
            Spinbox_DateYear.insert(0,config['Date']['Year'])
            Spinbox_DateMonth.delete(0,"end")
            Spinbox_DateMonth.insert(0,config['Date']['Month'])
            Spinbox_DateDay.delete(0,"end")
            Spinbox_DateDay.insert(0,config['Date']['Day'])
            Spinbox_DateHour.delete(0,"end")
            Spinbox_DateHour.insert(0,config['Time']['Hour'])
            Spinbox_DateMinute.delete(0,"end")
            Spinbox_DateMinute.insert(0,config['Time']['Minute'])
            Spinbox_DateSecond.delete(0,"end")
            Spinbox_DateSecond.insert(0,config['Time']['Second'])
            Event_Saved = True
            Start_Event()
    root.focus_force()
    Frame_EnterEvent.bind('<Configure>', resize_Frame_EnterEvent)
    root.mainloop()

if __name__ == '__main__':
    Countdown()