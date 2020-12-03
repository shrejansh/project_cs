
from tkinter import *


def new_file():
    pass
def open_file():
    pass
def save_file():
    pass
def exit_file():
    pass
def saveas_file():
    pass

if __name__ == "__main__":
    root=Tk()
    root.title("untitled - Notepad")
    root.geometry("700x500")
    root.config(bg="#000000")

    text=Text(root,bg="black",fg="white").pack(fill=BOTH,expand=True)
    file =None

    #menu
    menu=Menu(root)

    file_menu=Menu(menu,tearoff=0)
    file_menu.add_command(label="New",command=new_file)
    file_menu.add_command(label="Open",command=open_file)
    file_menu.add_command(label="Save",command=save_file)
    file_menu.add_command(label="Save AS",command=saveas_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=exit_file)
    menu.add_cascade(label="File",menu=file_menu)

    edit_menu=Menu(menu,tearoff=0)
    edit_menu.add_command(label="Cut",command=new_file)
    edit_menu.add_command(label="Copy",command=open_file)
    edit_menu.add_command(label="Paste",command=save_file)
    edit_menu.add_command(label="Find",command=open_file)
    edit_menu.add_command(label="Find & Replace",command=save_file)
    menu.add_cascade(label="Edit",menu=edit_menu)

    stats_menu=Menu(menu,tearoff=0)
    stats_menu.add_command(label="Word Count",command=open_file)
    stats_menu.add_command(label="Char Count",command=save_file)
    stats_menu.add_command(label="Created Time",command=open_file)
    stats_menu.add_command(label="Modified Time",command=save_file)
    menu.add_cascade(label="Stats",menu=stats_menu)


    root.config(menu=menu)



    root.mainloop()