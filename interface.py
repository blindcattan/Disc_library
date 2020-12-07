#First version
from tkinter import *
from tkinter import ttk

def startWindowLoop(conn):
    global my_tree
    root = Tk()
    root.title("Media Data Base")
    root.geometry("1170x650")
    #cretae a tree
    my_tree = ttk.Treeview(root)

    #DEFINE COLS
    '''
    Disk_ID     Active_Disk  Media_ref   Description         Checksum    Location_ID  Group_ID    part_number  Version_Number  Field_1     Field_2
    '''
    my_tree['columns'] = ("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version Number")


    my_tree.column("#0", width=1, minwidth=1)
    my_tree.column("Active_Disk", anchor=W, width=100)
    my_tree.column("Media_ref", anchor=W, width=90)
    my_tree.column("Description", anchor=W, width=225)
    my_tree.column("Checksum", width=100, minwidth=5, anchor=W)
    my_tree.column("Location", width=180, minwidth=5, anchor=W)
    my_tree.column("Group", width=180, minwidth=5, anchor=W)
    my_tree.column("Part Number", width=130, minwidth=5, anchor=W)
    my_tree.column("Version Number", width=130, minwidth=5, anchor=W)

    #Create Headings ("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version Number")
    #my_tree.heading("#0", text="Label", anchor=W)

    my_tree.heading("Active_Disk", text="Active_Disk", anchor=W)
    my_tree.heading("Media_ref", text="Media_ref", anchor=W)
    my_tree.heading("Description", text="Description", anchor = W )
    my_tree.heading("Checksum", text="Checksum",  anchor=W)
    my_tree.heading("Location", text="Location", anchor=W)
    my_tree.heading("Group", text="Group", anchor=W)
    my_tree.heading("Part Number", text="Part Number", anchor=W)
    my_tree.heading("Version Number", text="Version Number", anchor=W)

    #Add Data
    '''
    my_tree.insert(parent='',index='end',iid=0,values=("05504", "Test Description 1", "Dan's House"))
    my_tree.insert(parent='',index='end',iid=1,values=("05505", "Test Description 2", "Dan's House"))
    my_tree.insert(parent='',index='end',iid=2,values=("05506", "Test Description 3", "Dan's House"))
    my_tree.insert(parent='',index='end',iid=3,values=("05507", "Test Description 4", "Dan's House"))
    my_tree.insert(parent='',index='end',iid=4,values=("05508", "Test Description 5", "Tims House"))
    my_tree.insert(parent='',index='end',iid=5, values=("05509", "Test Description 6", "Dan's House"))
    '''
    Data = [""]
    my_tree.pack(pady=20)
    root.mainloop()

def LoadTreeViewData(rows):
    # ("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version_Number")
    count = 0
    for r in rows:
        print(r)

        my_tree.insert(parent='', index='end', iid=0, values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
        count += 1





