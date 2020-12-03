
from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter import filedialog

class font_size():
    def font1():
        pass



def new_file():
    text.delete(1.0,END)
    root.title("New File - Notepad")
    pass
def open_file():
    global text_file
    text_file=filedialog.askopenfilename(initialdir="C:/Users/Shreyansh/Desktop/",title="Open Text File",defaultextension=".txt",filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    text_file=open(text_file,"r+")
    stuff=text_file.read()
    text.insert(END,stuff)
    root.title(f"{text_file} - Notepad")
    text_file.close()
    pass

def save_file():
    text_file=open(text_file,'w')
    text_file.write(text.get(1.0,END))
    pass
def exit_file():
    pass
def saveas_file():
    text_file=filedialog.asksaveasfilename(initialdir="C:/Users/Shreyansh/Desktop/",title="Open Text File",defaultextension=".txt",filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    text_file=open(text_file,'w')
    text_file.write(text.get(1.0,END))
    pass


def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def find():
    pass
def find_r():
    pass


def word_c():
    t=text.get("1.0",'end')
    t=t.split()
    t=len(t)
    showinfo(title="word count", message=f"{t} words ")
def char_c():
    t=text.get("1.0",'end')
    t=t.split()
    t="".join(t)
    t=len(t)
    showinfo(title="Characters count", message=f"{t} characters ")
def c_time():
    pass
def m_time():
    pass



if __name__ == "__main__":
    root=Tk()
    root.title("untitled - Notepad")
    root.geometry("700x500")
    # root.config(bg="#000000")
    text=Text(root)
    text.pack(fill=BOTH,expand=True)
    file =None

    #menu
    menu=Menu(root,bd=2)

    file_menu=Menu(menu,tearoff=0)
    file_menu.add_command(label="New",command=new_file)
    file_menu.add_command(label="Open",command=open_file)
    file_menu.add_command(label="Save",command=save_file)
    file_menu.add_command(label="Save AS",command=saveas_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=exit_file)
    menu.add_cascade(label="File",menu=file_menu)

    edit_menu=Menu(menu,tearoff=0)
    edit_menu.add_command(label="Cut",command=cut)
    edit_menu.add_command(label="Copy",command=copy)
    edit_menu.add_command(label="Paste",command=paste)
    edit_menu.add_command(label="Find",command=find)
    edit_menu.add_command(label="Find & Replace",command=find_r)
    menu.add_cascade(label="Edit",menu=edit_menu)

    stats_menu=Menu(menu,tearoff=0)
    stats_menu.add_command(label="Word Count",command=word_c)
    stats_menu.add_command(label="Char Count",command=char_c)
    stats_menu.add_command(label="Created Time",command=c_time)
    stats_menu.add_command(label="Modified Time",command=m_time)
    menu.add_cascade(label="Stats",menu=stats_menu)

    fontsize_menu=Menu(menu,tearoff=0)
    fontsize_menu.add_command(label="6 px",command=font_size.font1)
    fontsize_menu.add_command(label="8 px",command=save_file)
    fontsize_menu.add_command(label="10 px",command=font_size.font1)
    fontsize_menu.add_command(label="12 px",command=save_file)
    fontsize_menu.add_command(label="14 px",command=font_size.font1)
    fontsize_menu.add_command(label="16 px",command=save_file)
    fontsize_menu.add_command(label="18 px",command=font_size.font1)
    fontsize_menu.add_command(label="20 px",command=save_file)
    menu.add_cascade(label="Font Size",menu=fontsize_menu)

    root.config(menu=menu)

    # scroll bar code 
    scroll=Scrollbar(text)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    root.mainloop()