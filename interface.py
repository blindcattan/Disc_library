#First version
from tkinter import *
from tkinter import ttk
from functools import partial

import DB_Backend


root = Tk()
Button_Frame = Frame (root)
Text_Media = Text(Button_Frame)

def startWindowLoop(conn):
    global my_tree
    global GroupCombo
    global Text_Media
    global Text_Description
    global LocationCombo

    #root = Tk()
    root.title("Media Data Base")
    root.geometry("1170x650")

    #Button_Frame = Frame (root)
    Button_Frame.pack()

    Text_Media = Text(Button_Frame)
    Text_Media.config(width=20,height=1,)

    LabelMediaRef = Label(Button_Frame)
    LabelMediaRef.config(width=10, height=1, text='Media Ref')

    Text_Description = Text(Button_Frame)
    Text_Description.config(width=20, height=1 )

    LabelDescription = Label(Button_Frame)
    LabelDescription.config(width=10, height=1, text='Description')

    GroupCombo = ttk.Combobox(Button_Frame)
    GroupCombo.config(width=30, height=5)
    LoadGroups(conn)

    LocationCombo = ttk.Combobox(Button_Frame)
    LocationCombo.config(width=20, height=5)
    LoadLocations(conn)

    LabelGroup = Label(Button_Frame)
    LabelGroup.config(width=5, height=1, text='Group')
    LabelLocation = Label(Button_Frame)
    LabelLocation.config(width=8, height=1, text='Location')

    SearchButton = Button(Button_Frame,text='Search')
    clearButton = Button(Button_Frame, text='Clear')

    #SearchButton.config(command=partial(searchButtonBtn, Text_Media,Text_Description,GroupCombo, ""))
    SearchButton.config(command=partial(searchButtonBtn,conn))
    clearButton.config(command=partial(clearSearch, conn))


    #Pack button frame
    LabelMediaRef.pack(side=LEFT)
    Text_Media.pack(side=LEFT)
    LabelDescription.pack(side=LEFT)
    Text_Description.pack(side=LEFT)
    LabelGroup.pack(side=LEFT)

    GroupCombo.pack(side=LEFT)
    LabelLocation.pack(side=LEFT)
    LocationCombo.pack(side=LEFT)

    SearchButton.pack(side=LEFT)
    clearButton.pack(side=LEFT)
    #create Tree Frame
    tree_frame = Frame(root)
    tree_frame.pack()
    #cretae a tree
    #create tree view scroll bar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse" )
    my_tree.pack()
    # configure scrollbar
    tree_scroll.config(command=my_tree.yview)


    #DEFINE COLS
    '''
    Disk_ID     Active_Disk  Media_ref   Description         Checksum    Location_ID  Group_ID    part_number  Version_Number  Field_1     Field_2
    '''
    my_tree['columns'] = ("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version Number")
    my_tree['height'] = 27


    my_tree.column("#0", width=1, minwidth=1)
    my_tree.column("Active_Disk", anchor=W, width=50)
    my_tree.column("Media_ref", anchor=W, width=90)
    my_tree.column("Description", anchor=W, width=310)
    my_tree.column("Checksum", width=90, minwidth=5, anchor=W)
    my_tree.column("Location", width=170, minwidth=5, anchor=W)
    my_tree.column("Group", width=150, minwidth=5, anchor=W)
    my_tree.column("Part Number", width=130, minwidth=5, anchor=W)
    my_tree.column("Version Number", width=100, minwidth=5, anchor=W)

    #Create Headings ("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version Number")
    #my_tree.heading("#0", text="Label", anchor=W)

    my_tree.heading("Active_Disk", text="Active", anchor=W)
    my_tree.heading("Media_ref", text="Media ref", anchor=W)
    my_tree.heading("Description", text="Description", anchor = W )
    my_tree.heading("Checksum", text="Checksum",  anchor=W)
    my_tree.heading("Location", text="Location", anchor=W)
    my_tree.heading("Group", text="Group", anchor=W)
    my_tree.heading("Part Number", text="Part Number", anchor=W)
    my_tree.heading("Version Number", text="Version", anchor=W)

    #Add Data

    LoadTreeViewData(DB_Backend.LoadDiskData(conn))

    root.mainloop()

    return my_tree

def LoadTreeViewData(rows):
    # ("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version_Number")
    count = 0
    for r in rows:
        my_tree.insert(parent='', index='end', iid=count, values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
        count = count + 1
    my_tree.pack(pady=20)

def LoadGroups(conn):
    rows = DB_Backend.returnGroupNames(conn)
    #aa     print(rows)
    cache = []
    for r in rows:
        print (r[0])
        cache.append(r[0])
    GroupCombo['values'] = cache
    #tobys 66ufi6ur6st line of 7tcoyde`333333333333333333333333333333314rqerc         3s
    #.jhkk("hi`")

def LoadLocations(conn):
    rows = DB_Backend.returnLocationNames(conn)
    #print(rows)
    cache = []
    for r in rows:
        #print (r[0])
        cache.append(r[0])
    LocationCombo['values'] = cache


def searchButtonBtn(conn):

    MediaID = Text_Media.get(1.0,"end-1c")
    description = Text_Description.get(1.0,"end-1c")
    Group = GroupCombo.get()
    location = ""
    #print("media ID: ", MediaID, "Description", description, "GROUP ", Group)


    #clear the empty bits
    if MediaID == "":
        MediaID = "%"
    else:
        MediaID = "%" + MediaID + "%"
    if description == "":
        description = "%"
    else:
        description = "%" + description + "%"
    if Group == "":
        Group = "%"
    else:
        Group = "%" + Group + "%"
    if location == "":
        location = "%"
    else:
        location = "%" + location + "%"


    # clear the tree
    my_tree.delete(*my_tree.get_children())

    #generate the tuple that will provide the search data
    searchterms = (MediaID,description,Group,location)

    #run command to
    rows = DB_Backend.SearchMedia(conn,searchterms)
    LoadTreeViewData(rows)


def clearSearch(conn):
    #clear search fields
    GroupCombo.set('')
    Text_Description.delete(1.0,END)
    LocationCombo.set('')
    Text_Media.delete(1.0,END)

    #perform search
    searchButtonBtn(conn)





