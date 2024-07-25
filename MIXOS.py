from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk
be = Tk()

def fol():
    our_image = PhotoImage(file="C:/Users/delde/OneDrive/Pulpit/MY PROJECT/MIXOS/MixoeOS_System/MIXOS_System15/MixoeOS_Icon\older.png")
    our_image = our_image.subsample(3, 3)
    our_label = Label(be)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x = 152, y = 99)
def support():
    os.startfile('C:/Users/delde/OneDrive/Pulpit/MY PROJECT/MIXOS/MixoeOS_System/System_Application\Suppot_MixoeOS.py')


def screenShot():
    os.startfile('C:/Users/delde/OneDrive/Pulpit/MY PROJECT/MIXOS/MixoeOS_System/System_Application/Screenshot_Image\ScreenShot.py')

def popup(event):
    global x, y 
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


x = 0
y = 0




def X():
    if messagebox.askokcancel("Shut down", "Are you sure you want to turn off the system?"):
        be.deiconify()
        exit()



 
def Clock():
    os.startfile('C:/Users/delde/OneDrive/Pulpit/MY PROJECT/MIXOS/MixoeOS_System/System_Application\clock.py')
   

def Paint():
    os.startfile('C:/Users/delde/OneDrive/Pulpit/MY PROJECT/MIXOS/MixoeOS_System/System_Application/Paint_Image\Paint.py')



be.title('MixoeOS')
be.geometry('1400x784')
be.resizable(width=False, height=False)
C = Canvas(be, width=1400, height=784, bg='#330066')
C.pack()

C.bind('<Button-3>', popup)
menu = Menu(tearoff=0)
menu.add_command(label='shut down', command=X)
menu.add_command(label='ScreenShot', command=screenShot)
menu.add_command(label='Support', command=support)
menu.add_command(label='Create Folder', command=fol)
menu.add_command(label='Background',)

be['bg'] = 'black'

Shut_down = Button(be, text='Shut down', bg='black', fg='violet', font=('Comic Sans MS', 8, 'bold'), command=X)
Shut_down.place(x=10, y=10, width=60, height=40)

Clock = Button(be, text='Clock', bg='black', fg='violet', font=('Comic Sans MS', 10, 'bold'), command=Clock)
Clock.place(x=72, y=10, width=39, height=40)

Paint = Button(be, text='Paint', bg='black', fg='violet', font=('Comic Sans MS', 10, 'bold'), command=Paint)
Paint.place(x=112, y=10, width=39, height=40)



qw = Button(be, text='AB', bg='violet', fg='black', font=('Comic Sans MS', 10, 'bold'))
qw.place(x=0, y=755, width=80, height=30)



be.mainloop()

