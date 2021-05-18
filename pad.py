import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox,font,colorchooser,filedialog
import os
window=tk.Tk()
window.geometry('1200x800')
window.title("Pad")
# -------------------------- Main Menu----------------------------------
main_menu=tk.Menu(window)
file=tk.Menu(main_menu,tearoff=0)
edit=tk.Menu(main_menu,tearoff=0)
view=tk.Menu(main_menu,tearoff=0)
color_theme=tk.Menu(main_menu,tearoff=0)
new_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-add-file-16.png")
open_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-view-details-16.png")
save_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-save-16.png")
saveas_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-save-as-16.png")
exit_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-exit-16.png")
copy_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-copy-16.png")
cut_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-cut-16.png")
paste_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-paste-16.png")
selectall_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-clear-symbol-16.png")
find_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-find-hospital-16.png")

v=tk.StringVar()
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monoki':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)

# &&&&&&&&&&&&&&&&&&&&&&&&&&& Tool Bar &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
tool_bar=ttk.Label(window)
tool_bar.pack(side=tk.TOP,fill=tk.X)
#font
font_tuple=tk.font.families()
font_variable=tk.StringVar()
box=ttk.Combobox(tool_bar,textvariable=font_variable,state="readonly")
box['value']=font_tuple
box.current(font_tuple.index('Arial'))
box.grid(row=0,column=0,padx=3)
#size
size_variable=tk.IntVar()
size=ttk.Combobox(tool_bar,width=7,textvariable=size_variable,state='readonly')
size['value']=tuple(range(8,81,2))
size.grid(row=0,column=1)
#bold button
bold_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-bold-16.png")
bold=ttk.Button(tool_bar,image=bold_icon)
bold.grid(row=0,column=2)
#Italic buttom
italic_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-italic-16.png")
italic=ttk.Button(tool_bar,image=italic_icon)
italic.grid(row=0,column=3)
#underline buttom
underline_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-underline-16.png")
underline=ttk.Button(tool_bar,image=underline_icon)
underline.grid(row=0,column=4)  
#fontcolor buttom
color_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-text-color-16 (1).png")
font_color=ttk.Button(tool_bar,image=color_icon)
font_color.grid(row=0,column=5)
#left buttom
left_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-align-left-16.png")
left=ttk.Button(tool_bar,image=left_icon)
left.grid(row=0,column=6)
# center
center_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-align-center-16.png")
center=ttk.Button(tool_bar,image=center_icon)
center.grid(row=0,column=7)
# right
right_icon=tk.PhotoImage(file=r"C:\Users\kartik\Downloads\icons8-align-right-16.png")
right=ttk.Button(tool_bar,image=right_icon)
size.current(2)
right.grid(row=0,column=8)

# &&&&&&&&&&&&&&&&&&&&&&&&&&&& Text Editor &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
editor=tk.Text(window)
scrollbar=tk.Scrollbar(window)
editor.config(wrap='word',relief=tk.FLAT)
editor.focus_set()
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
editor.pack(expand=True,fill=tk.BOTH)
scrollbar.config(command=tk.YView)
editor.config(yscrollcommand=scrollbar.set)
current_font='Arial'
current_size=12
def font_type(window):
    global current_font
    current_font=font_variable.get()
    editor.configure(font=(current_font,current_size))
def font_size(window):
    global current_size
    current_size=size_variable.get()
    editor.configure(font=(current_font,current_size))
box.bind('<<ComboboxSelected>>',font_type)
size.bind('<<ComboboxSelected>>',font_size)
def bold_change():
    text_content=tk.font.Font(font=editor['font'])
    if text_content.actual()['weight']=='normal':
        editor.configure(font=(current_font,current_size,'bold'))
    if text_content.actual()['weight']=='bold':
        editor.configure(font=(current_font,current_size,'normal'))
bold.configure(command=bold_change)
def italic_change():
    text_content=tk.font.Font(font=editor['font'])
    if text_content.actual()['slant']=='roman':
        editor.configure(font=(current_font,current_size,'italic'))
    if text_content.actual()['slant']=='italic':
        editor.configure(font=(current_font,current_size,'normal'))
italic.configure(command=italic_change)
def underline_change():
    text_content=tk.font.Font(font=editor['font'])
    if text_content.actual()['underline']==0:
        editor.configure(font=(current_font,current_size,'underline'))
    if text_content.actual()['underline']==1:
        editor.configure(font=(current_font,current_size,'normal'))
underline.configure(command=underline_change)
def fontcolor_change():
    text_color=tk.colorchooser.askcolor()
    editor.configure(fg=text_color[1])
font_color.configure(command=fontcolor_change)
def leftalign():
    text_content=editor.get(1.0,'end')
    editor.tag_config('left',justify=tk.LEFT)
    editor.delete(1.0,tk.END)
    editor.insert(tk.INSERT,text_content,'left')
left.configure(command=leftalign)
def centeralign():
    text_content=editor.get(1.0,'end')
    editor.tag_config('center',justify=tk.CENTER)
    editor.delete(1.0,tk.END)
    editor.insert(tk.INSERT,text_content,'center')
center.configure(command=centeralign)
def rightalign():
    text_content=editor.get(1.0,'end')
    editor.tag_config('right',justify=tk.RIGHT)
    editor.delete(1.0,tk.END)
    editor.insert(tk.INSERT,text_content,'right')
right.configure(command=rightalign)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&& Status Bar &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
status_bar=ttk.Label(window,text="Status Bar")
status_bar.pack(side=tk.BOTTOM,fill=tk.X)
text_changed=True
def change(event=None):
    if editor.edit_modified():
        global text_changed
        character=len(editor.get(1.0,'end-1c').replace(' ',''))
        words=len(editor.get(1.0,'end-1c').split())
        status_bar.config(text=f'character : {character} words : {words}')
    editor.edit_modified(False)
editor.bind("<<Modified>>",change)

url=''
def newfile(event=None):
    global url
    url=''
    editor.delete(1.0,tk.END)
file.add_command(label="New File",image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=newfile)

def openfile(event=None):
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(("Text File",'*.txt'),('All File','*.*')))
    try:
        with open(url,'r') as f:
            editor.delete(1.0,tk.END)
            editor.insert(1.0,f.read())
    except FileNotFoundError:
        return
    except:
        return
    window.title(os.path.basename(url))
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=openfile)

def savefile(event=None):
    global url
    if url:
        content=editor.get(1.0,tk.END)
        with open(url,'w',encoding='utf-8') as f:
            f.write(content)
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextention='*.txt',filetypes=(('Text File','*.txt'),('All File','*.*')))
        content2=editor.get(1.0,tk.END)
        with open(url,'w',encoding='utf-8') as fw:
            fw.write(content2)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=savefile)

def saveasfile(event=None):
    global url
    try:
        content=editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='*txt',filetypes=(("Text File","8.txt"),("All File",'*.*')))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label='Save as',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+S',command=saveasfile)

def exitfile(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("warning",'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content=editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as f:
                        f.write(content)
                else:
                    content2=str(editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='*.txt',filetypes=(("Text File",'*.txt'),('all File','*.*')))
                    url.write(content2)
                    url.close()
                    window.destroy()
            elif mbox is False:
                window.destroy()
        else:
            window.destroy()
    except:
        return
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exitfile)
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda :editor.event_generate('<Control c>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda :editor.event_generate('<Control x>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda :editor.event_generate('<Control v>'))
edit.add_command(label='Delete all',image=selectall_icon,compound=tk.LEFT,accelerator='Ctrl+A',command=lambda:editor.delete(1.0,tk.END))

def findfun(event=None):
    def find():
        word=find_entry.get()
        editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                editor.tag_config('match',foreground="red",background="yellow")
    
    def replace():
        word=find_entry.get()
        replace_text=replace_entry.get()
        content=editor.get(1.0,tk.END)
        content2=content.replace(word,replace_text)
        editor.delete(1.0,tk.END)
        editor.insert(1.0,content2)

    find_dialoug=tk.Toplevel()
    find_dialoug.geometry('300x250+400+200')
    find_dialoug.title('Find')
    find_dialoug.resizable(0,0)
    frame=tk.LabelFrame(find_dialoug,text='Find')
    frame.pack(pady=20)
    find_label=ttk.Label(frame,text="Find")
    replace_label=ttk.Label(frame,text="Replace")
    find_variable=tk.StringVar()
    find_entry=ttk.Entry(frame,width=20,textvariable=find_variable)
    replace_variable=tk.StringVar()
    replace_entry=ttk.Entry(frame,width=20,textvariable=replace_variable)
    find_button=ttk.Button(frame,text="Find",command=find)
    replace_button=ttk.Button(frame,text='Replace',command=replace)
    find_label.grid(row=0,column=0,padx=2,pady=3)
    replace_label.grid(row=1,column=0,padx=2,pady=3)
    find_entry.grid(row=0,column=1,padx=2)
    replace_entry.grid(row=1,column=1,padx=2)
    find_button.grid(row=2,column=1,padx=2,pady=5)
    replace_button.grid(row=2,column=2,padx=2,pady=5)
    find_dialoug.mainloop()
edit.add_command(label='Find',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=findfun)

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
def hide_tool():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        editor.pack(expand=True,fill=tk.BOTH)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,variable=show_toolbar,command=hide_tool)
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True
view.add_checkbutton(label="Status Bar",onvalue=1,offvalue=False,variable=show_statusbar,command=hide_statusbar)

def change_theme():
    chosen_theme=v.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    editor.config(background=bg_color,fg=fg_color)
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,variable=v,command=change_theme)
# &&&&&&&&&&&&&&&&&&&&&&&&&& End Menu &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#bind ShortcutKey
window.bind('<Control-n>',newfile)
window.bind('<Control-o>',openfile)
window.bind('<Control-s>',savefile)
window.bind('<Control-Shift-s>',saveasfile)
window.bind('<Control-q>',exitfile)
window.bind('<Control-f>',findfun)

window.config(menu=main_menu)
window.mainloop()