import random
import pygame
import pygame.mixer
import os
import ntpath
from tkinter import Button,Tk,Frame,TOP,Label,Listbox,CENTER,END


pygame.mixer.init()
root=Tk()
root.geometry("1600x800+0+0")
root.configure(background="white")
Tops=Frame(root,width=1350,height=50,bd=8,bg="black")
Tops.pack(side=TOP)

lblinfo=Label(Tops,font=('Blackadder ITC',40,'bold'),text="Music Player",bd=10,fg="red")
lblinfo.grid(row=0,column=0)
list=[]
list5=[]
for rt, dirs, files in os.walk('D:/INNOVATIVE/songs'):
    for file in files:
        if file.endswith('.mp3'):
            list.append(os.path.join(rt,file))	
txtdisplay=Listbox(root,height=23,width=38,bd=16,font=('arial',15,'bold'),fg="green",bg="black")
txtdisplay.place(relx=0.7,rely=0.6,anchor=CENTER)

i=0
for name in list:
    list5.append(ntpath.basename(name))
    txtdisplay.insert(END,list5[i])
    i+=1					
index=0
def next():


    global index
    index+=1 
    if index==len(list):
        btn5['state']='disabled'
        pygame.mixer.music.stop()
        txtdisplay.itemconfig(index-1, {'fg': 'green'})
        index=0
        
    else:
        txtdisplay.itemconfig(index-1, {'fg': 'green'})
        txtdisplay.itemconfig(index, {'fg': 'red'})
        pygame.mixer.music.load(list[index])
        pygame.mixer.music.play()
def stop():
  
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause() 
def previous():
    global index
    index-=1               
    if index==-1:
        pygame.mixer.music.stop()
        txtdisplay.itemconfig(index+1, {'fg': 'green'})
        index=0
    else:
        txtdisplay.itemconfig(index, {'fg': 'red'})
        txtdisplay.itemconfig(index+1, {'fg': 'green'})            
        pygame.mixer.music.load(list[index])
        pygame.mixer.music.play() 
def play():
    global index
    btn5['state']='normal'
    txtdisplay.itemconfig(index, {'fg': 'red'})
    pygame.mixer.music.load(list[index])
    pygame.mixer.music.play()
def exit1():
    exit()
    return
btn6=Button(root,text="play",fg="powder blue",padx=10,pady=10,bd=4,width=10,bg="blue",font=('Brush Script MT',15,'bold'),command=play)
btn6.place(relx=0.1,rely=0.3,anchor=CENTER)                                                          
btn5=Button(root,text="next",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,state="normal",font=('Brush Script MT',15,'bold'),command=next)
btn5.place(relx=0.3,rely=0.3,anchor=CENTER)        
btn1=Button(root,text="stop",fg="powder blue",bg="red",padx=10,pady=10,bd=4,width=10,font=('Brush Script MT',15,'bold'),command=stop)
btn1.place(relx=0.2,rely=0.45,anchor=CENTER)
btn2=Button(root,text="pause",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,font=('Brush Script MT',15,'bold'),command=pause)
btn2.place(relx=0.1,rely=0.6,anchor=CENTER)
btn3=Button(root,text="unpause",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,font=('Brush Script MT',15,'bold'),command=unpause)
btn3.place(relx=0.3,rely=0.6,anchor=CENTER)
btn4=Button(root,text="previous",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,font=('Brush Script MT',15,'bold'),command=previous)
btn4.place(relx=0.1,rely=0.8,anchor=CENTER)    
btn7=Button(root,text="Exit",fg="powder blue",bg="blue",padx=10,pady=10,bd=4,width=10,font=('Brush Script MT',15,'bold'),command=exit)
btn7.place(relx=0.3,rely=0.8,anchor=CENTER)
root.mainloop()                         
