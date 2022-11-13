#Katie Jones
#Task manager program
#22/10/2020

from tkinter import *
import random

screenSize = "1200x700+360+150"
mainbg = "#FFFFFF"
mainFont="Arial 30"
taskFont = "Arial 24"
doneFont = "Arial 17"
btnbg = "#F6B9F7"
mainfg = "#000000"
activebtnbg = "#C696C7"
btnheight = 2
btnwidth = 30

def back_to_menu(Screen, mainMenu):
    Screen.destroy()
    mainMenu.deiconify()

def resume_progress(mainMenu, save_indicator):

    save_indicator = True
    displayTasks(mainMenu, save_indicator)
    

def displayTasks(mainMenu, save_indicator):
    mainMenu.withdraw()

    dT = Toplevel()
    dT.title("Don't you dare think about not doing this task D:<")
    dT.geometry(screenSize)
    dT["bg"] = mainbg

    file = open("tasks.txt", "r")
    tasks_to_read = file.read()
    tasks_list = tasks_to_read.split(",")
    file.close()

    del tasks_list[-1]

    random_task = random.choices(tasks_list)

    def roll_task(tasks_list):
        random_task = random.choice(tasks_list)
        task_entry.delete(0, END)
        task_entry.insert(0, random_task)
        return random_task
    
    def save_quit(mainMenu, Screen):

        task_to_save = task_entry.get()
        
        file = open("saved_task.txt", "w")
        file.write(task_to_save)
        file.close()

        Screen.destroy()

        mainMenu.deiconify()

    def completed_task(tasks_list, mainMenu, Screen):

        task_to_remove = task_entry.get()
        tasks_list.remove(task_to_remove)
        
        file = open("tasks.txt", "w")
        for i in range(len(tasks_list)):
            file.write(tasks_list[i] + ",")
        file.close()

        Screen.destroy()
        mainMenu.deiconify()
    
    lab0 = Label(dT, text="", bg=mainbg, height = 5)
    lab0.pack()

    lab_title = Label(dT, text="Here is your mission:", font=mainFont, bg=mainbg, fg=mainfg)
    lab_title.pack()

    lab0 = Label(dT, text="", bg=mainbg, height=1)
    lab0.pack()

    frame0 = Frame(dT, bg=mainbg)
    frame1 = Frame(dT, bg=mainbg)
    frame2 = Frame(dT, bg=mainbg)

    lab0 = Label(frame0, text="", bg=mainbg, width=20)
    lab0.pack()

    reroll_btn = Button(frame0, text="Re-roll", command=lambda: roll_task(tasks_list), font=doneFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg)
    reroll_btn.pack(side=RIGHT)

    main_menu_btn = Button(frame0, text="Back to main menu", command=lambda: back_to_menu(dT, mainMenu), font=doneFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg)
    main_menu_btn.pack(side=BOTTOM)

    frame0.pack(anchor=W, fill=Y, expand=False, side=LEFT)

    lab0 = Label(frame1, text="", bg=mainbg, height=1)
    lab0.pack()

    task_entry = Entry(frame1,font=taskFont, bg=btnbg, fg=mainfg, width=37)
    task_entry.pack()

    frame1.pack(side=LEFT)

    lab0 = Label(frame2, text="", bg=mainbg, height=1)
    lab0.pack()

    done_btn = Button(frame2, text="Done!", command=lambda: completed_task(tasks_list, mainMenu, dT),font=doneFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg)
    done_btn.pack(side=LEFT)

    save_btn = Button(frame2, text="Save and quit", command = lambda: save_quit(mainMenu, dT), font=doneFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg)
    save_btn.pack(side=BOTTOM)

    frame2.pack(anchor=E, fill=Y, expand=False, side=RIGHT)

    if save_indicator == False:
        roll_task(tasks_list)
    elif save_indicator == True:
        file = open("saved_task.txt", "r")
        saved_task_to_read = file.read()
        file.close()

        task_entry.delete(0, END)
        task_entry.insert(0, saved_task_to_read)
        

    dT.mainloop()    

def add_to_textfile(task):
    file = open("tasks.txt", "a")
    file.write(task)
    file.close()

def addToList(mainMenu):

    mainMenu.withdraw()
    
    addTL = Toplevel()
    addTL.title("Add to list")
    addTL.geometry(screenSize)
    addTL["bg"] = mainbg

    def get_task():
        task = task_entry.get()
        task_entry.delete(0, END)
        add_to_textfile(task + ",")
        

    lab0 = Label(addTL, text="", bg=mainbg, height=10)
    lab0.pack()

    task_entry = Entry(addTL, bg=btnbg, font=mainFont, width=40)
    task_entry.pack()

    lab0 = Label(addTL, text="", bg=mainbg, height=1)
    lab0.pack()

    task_entry_btn = Button(addTL, text="Add task", command=lambda: get_task(), font=mainFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg, width= btnwidth, height=btnheight)
    task_entry_btn.pack()

    lab0 = Label(addTL, text="", bg=mainbg, height=1)
    lab0.pack()

    main_menu_btn = Button(addTL, text="Back to main menu", command=lambda:back_to_menu(addTL, mainMenu), font=mainFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg, width= btnwidth, height=btnheight)
    main_menu_btn.pack()

    addTL.mainloop()

def main_menu():

    mainMenu = Tk()
    mainMenu.title("Main Menu")
    mainMenu.geometry(screenSize)
    mainMenu["bg"] = mainbg

    spaceheight = 4
    #btnheight = 2
    #btnwidth = 30
    save_indicator = False

    lab0 = Label(mainMenu, text="", bg=mainbg, height=spaceheight)
    lab0.pack()

    add_to_list_btn = Button(mainMenu, text="Add tasks to list", command=lambda: addToList(mainMenu), font=mainFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg, width= btnwidth, height=btnheight)
    add_to_list_btn.pack()

    lab0 = Label(mainMenu, text="", bg=mainbg, height=spaceheight)
    lab0.pack()

    give_task_btn = Button(mainMenu, text="Give me a task", command=lambda: displayTasks(mainMenu, save_indicator), font=mainFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg, width= btnwidth, height=btnheight)
    give_task_btn.pack()

    lab0 = Label(mainMenu, text="", bg=mainbg, height=spaceheight)
    lab0.pack()

    resume_tasks_btn = Button(mainMenu, text="Resume previous tasks", command=lambda: resume_progress(mainMenu, save_indicator), font=mainFont, bg=btnbg, fg=mainfg, activebackground=activebtnbg, activeforeground=mainfg, width= btnwidth, height=btnheight)
    resume_tasks_btn.pack()

    mainMenu.mainloop()

main_menu()
