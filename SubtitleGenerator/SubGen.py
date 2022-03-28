#For more detailed info see sg.py and subgenGUI.py
import moviepy.editor as me
import speech_recognition as sr
import time,threading,os,psutil,subprocess,sys
from tkinter import *
from tkinter import filedialog
main,ft=Tk(),(('Videos','*.mkv'),('Videos','*.mp4'),('Videos','*.3gp'))
main.withdraw()
path,r=filedialog.askopenfilename(filetypes=ft),sr.Recognizer()
mainclip,lines=me.AudioFileClip(path),[]
dur,check=mainclip.duration,False
print("Attention! Don't pause, seek or fullscreen your video. Just keep watching.")
def extract():
    init,fin,li=0,5,[]
    global check
    while dur>fin:
        cutclip=mainclip.subclip(init,fin)
        cutclip.write_audiofile('temp.wav',codec='pcm_s16le')
        with sr.AudioFile('temp.wav') as source:
            r.adjust_for_ambient_noise(source,duration=0.3)
            audio=r.record(source)
        init+=5;fin+=5
        try:
            lines.append(r.recognize_sphinx(audio))
        except:
            print('An Error Occured!')
            lines.append(' ')
            continue
class mt(threading.Thread):
    def run(self):
        extract()
main.geometry('1000x120+260+650')
main.overrideredirect(True)
main.configure(bg='black')
main.wm_attributes('-transparentcolor','black','-topmost',True)
sv,t1,residue=StringVar(),mt(),''
t=Label(main,textvariable=sv,wraplength=1000,font=('Calibri',25),bg='black',fg='white')
t1.start()
def refresh(t,count,show):
    global check,residue#F:\Python\python.exe D:\Python\SubGen.py
    if(len(lines)>0):
        if show==False:
            main.deiconify()
            subprocess.call(path,shell=True)
            #main.overrideredirect(False)
            #main.wm_attributes('-fullscreen',True)
            show=True;check=True
        sv.set(residue+'\n'+lines[0])
        residue=lines[0]
        lines.pop(0)
    else:
        sv.set('Wait')
    if count>dur:
        main.destroy()
        return
    t.pack()
    count+=5
    t.after(5000,refresh,t,count,show)
refresh(t,0,False)
main.mainloop()
os.remove('temp.wav')
os._exit(1)
