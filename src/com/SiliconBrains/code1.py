from tkinter import *  
import os
import json
from cryptography.fernet import Fernet
import datetime

root = Tk()
root.geometry('1000x650')
root.configure(bg='gray')
root.title(f'Silicon Brains')
photo = PhotoImage(file = 'logo.png')
root.iconphoto(False, photo)

date = datetime.date.today()
data = open('data/api.json', 'r')
js = json.load(data)
version = js["version"] 
fontColor = js["fontColor"]
path = js["saveData"]
bg = js["backGround"]
font = js["font"]
cli = js["terminal"]

# input the text in textbox
EnterText = Text(root, width=500, height=500, bg=bg, fg=fontColor, font=font, inactiveselectbackground='green', insertbackground='green', selectbackground='yellow')
EnterText.pack(fill=X)

#create file and save data in file 
def saveData():
    kali = Tk()
    kali.geometry('200x100')
    kali.configure(bg='gray')
    kali.title('Silicon Brains')
    Label(kali, text='File Name', bg='yellow', fg='green').pack()
    global fileName
    fileName = Entry(kali)
    fileName.pack()
    global bt
    def bt():
        global fileN
        fileN = fileName.get()
        os.system(f'touch {fileN}')
        codeData = EnterText.get(1.0, END)
        with open(f'{fileN}', 'w') as f:
            print(f.write(codeData))
            f.close()
        os.system(f'mv {fileN} {path}')
        kali.destroy()
    
    bt1 = Button(kali, text='Save File', bg='gold', fg='red', command=bt)
    bt1.pack()

    kali.mainloop()

# clear all data
def clearData():
    EnterText.delete(1.0, END)

#open terminal
def terminal():
    os.system(f'cd {path} && {cli}')

#run cpp code
def cpp():
    os.system('clear')
    os.system(f'cd {path} && g++ {fileN} -o a && ./a')

#run python code
def python():
    os.system('clear')
    os.system(f'cd {path} && python3 {fileN}')

#run java code
def java():
    os.system('clear')
    os.system(f'cd {path} && java {fileN}')

def javaScript():
    os.system('clear')
    os.system(f'cd {path} && node {fileN}')

#reade the file data
def fileData():
    window1 = Tk()
    window1.geometry('1000x550')
    window1.title('Silicon Brains')
    window1.configure(bg='gray')
    Label(window1, text='Enter file path', bg='yellow', fg='red').pack(fill=X)
    e1 = Entry(window1)
    e1.pack()
    et = Text(window1, bg='black', fg='lime', font='hack')
    et.pack(fill=X)
    def readFile():
        filer = e1.get()
        data = open(f'{filer}', 'r')
        fd = data.read()
        et.insert(1.0, fd)

    bt = Button(window1, text='read_file', fg='lime', bg='black', command=readFile)
    bt.pack(side=TOP)
   
    window1.mainloop()

#show the app vesion or oner
def halp():
    window2 = Tk()
    window2.geometry('300x100')
    window2.title('Silicon Brains')
    window2.configure(bg='gray')
    Label(window2, text='Version : '+version, bg='yellow', fg='red').pack()
    Label(window2, text='Company Name : Silicon Brains', bg='yellow', fg='red').pack()
    Label(window2, text='Developer Name : Maikal Shivankar', fg='red', bg='yellow').pack()
    Label(window2, text='Oner Name : Maikal Shivankar', bg='yellow', fg='red').pack()
    window2.mainloop()

#save the file
def save():
    os.system(f'touch {fileN}')
    print(fileN)
    codeDa = EnterText.get(1.0, END)
    with open(f'{fileN}', 'a') as f:
        print(f.write(codeDa))
        f.close()
    os.system(f'mv {fileN} {path}')
    f.close()

#ecrypt the file
def enc():
    global key
    global fd
    key = Fernet.generate_key()
    with open('myKey.key', 'wb') as f1:
        f1.write(key)
        f1.close()
    
    fd = Fernet(key)

    with open(f'{path}{fileN}', 'rb') as f2:
        encd = f2.read()
        f2.close()

    encry = fd.encrypt(encd)

    with open(f'{fileN}', 'wb') as encData:
        encData.write(encry)
        encData.close()

    os.system(f'mv {fileN} {path}')

# derypt the file 
def dec():
    with open('myKey.key', 'wb') as f1:
        f1.write(key)
        f1.close()

    with open(f'{path}{fileN}', 'rb') as f2:
        decry = f2.read()
        f2.close()

    dec = fd.decrypt(decry)

    with open(f'{fileN}', 'wb') as f3:
        f3.write(dec)
        f3.close()
    os.system(f'mv {fileN} {path}')

#open file on code Editor
def ope():
    window3 = Tk()
    window3.geometry('200x100')
    window3.configure(bg='gray')
    window3.title('Silicon Brains')
    Label(window3, text='Enter file path', background='yellow', fg='red').pack()
    e1 = Entry(window3)
    e1.pack()

    def pat():
        global fdata
        e = e1.get()
        with open(f'{e}', 'r') as re:
            fdata = re.read()
            re.close()
        EnterText.insert(0.1, fdata)
        os.system(f'cp {e} {path}')
        window3.destroy()

    b = Button(window3, text='Summit', bg='gold', fg='green', command=pat)
    b.pack()

    window3.mainloop()

# menu bar all manu in this code part
MainMenu = Menu(root, bg=bg, fg=fontColor)
m1 = Menu(MainMenu,  bg=bg, fg=fontColor, tearoff=0)

m1.add_command(label='open', command=ope)
m1.add_command(label='save', command=save)
m1.add_command(label='save as', command=saveData)
m1.add_separator()
m1.add_command(label='clear', command=clearData)
MainMenu.add_cascade(label='File', menu=m1)
m1.add_command(label='Exit', command=quit)

m2 = Menu(MainMenu, bg=bg, fg=fontColor , tearoff=0)
MainMenu.add_cascade(label='CodeRunner', menu=m2)
m2.add_command(label='python', command=python)
m2.add_command(label='cpp', command=cpp)
m2.add_command(label='java', command=java)
m2.add_command(label='javaScript', command=javaScript)

m3 = Menu(MainMenu, bg=bg, fg=fontColor, tearoff=0)
MainMenu.add_cascade(label='encrypter', menu=m3)
m3.add_command(label='encryptData', command=enc)
m3.add_command(label='decryptData', command=dec)

MainMenu.add_command(label='Terminal', command=terminal)
MainMenu.add_command(label='show_file_data', command=fileData)

m4 = Menu(root, bg=bg, fg=fontColor, tearoff=0)
MainMenu.add_cascade(label='date', menu=m4)
m4.add_command(label=date)

MainMenu.add_command(label='about!', command=halp)

root.config(menu=MainMenu)
root.mainloop()
os.system('clear')
