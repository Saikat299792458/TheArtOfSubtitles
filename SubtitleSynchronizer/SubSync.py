#some lines are missing in the synched file
from tkinter import filedialog
from tkinter import *
ft={('Subtitle','*.srt')}
main=Tk()
main.withdraw()
path=filedialog.askopenfilename(filetypes=ft)
main.destroy()
if path=='':
    quit()
spath=path.rstrip('.srt')+'-synced.srt'
fr,fw=open(path,'r'),open(spath,'w')
dif=input('Enter time shift(min:sec:msec).(Use negative for reverse shift):')
mul=1;
if dif[0]=='-':
    mul=-1
    dif=dif.lstrip('-')
tl,m=[0,0,0],0
for i in dif.split(':'):
    tl[m]=int(i)
    m+=1
get,write=0,1
ind,string=1,fr.readline()
while string!='':
    if get==0:
        get=1
        pass
    elif get==1:
        get=2
        tm=string.split(' --> ')
        for i in range(2):
            temp=tm[i].split(',')
            msec=int(temp[1])
            temp2=temp[0].split(':')
            hr,min,sec=int(temp2[0]),int(temp2[1]),int(temp2[2])
            msec+=mul*tl[2]
            if msec>=1000:
                sec+=msec/1000
                msec=msec%1000
            sec+=mul*tl[1]
            if sec>=60:
                min+=sec/60
                sec=sec%60
            min+=mul*tl[0]
            if min>=60:
                hr+=min/60
                min=min%60
            if msec<0 or sec<0 or min<0:
                write=0
                break
            tm[i]=str(hr).rjust(2,'0')+':'+str(min).rjust(2,'0')+':'+str(sec).rjust(2,'0')+','+str(msec).rjust(3,'0')
        else:
            fw.write(str(ind)+'\n'+' --> '.join(tm)+'\n')
            ind+=1
            write=1
    else:
        if string=='\n':
            get=0
        if write:
            fw.write(string)
    string=fr.readline()
fr.close()
fw.close()
