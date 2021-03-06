import sqlite3
from datetime import date
from sqlite3 import Error


sql_create_disks_table = """ CREATE TABLE IF NOT EXISTS disks (
                                        Disk_ID integer PRIMARY KEY,
                                        Active_Disk BOOLEAN NOT NULL,
                                        Media_ref text NOT NULL UNIQUE,
                                        Description text NOT NULL,
                                        Checksum text,
                                        Location_ID integer,
                                        Group_ID text,
                                        part_number text,
                                        Version_Number text,
                                        Field_1 text,
                                        Field_2 text,
                                        FOREIGN KEY (Location_ID) REFERENCES Locations (ID),
                                        FOREIGN KEY (Group_ID) REFERENCES Groups (ID)
                                    ); """

sql_create_ABorrows_table = """ CREATE TABLE IF NOT EXISTS ABorrows (
                                        Borrow_ID integer PRIMARY KEY,
                                        Engineer_ID integer, 
                                        Media_ID integer ,
                                        Date_Taken date,
                                        Date_Returned date,
                                        FOREIGN KEY (Engineer_ID) REFERENCES Locations (ID),
                                        FOREIGN KEY (Media_ID) REFERENCES disks (Disk_ID)
                                        ); """

sql_create_Persons_table = """ CREATE TABLE IF NOT EXISTS Persons (
                                            Active BOOLEAN,
                                            Person_ID integer PRIMARY KEY,
                                            Person_Name text NOT NULL
                                        ); """

sql_create_Groups_table = """ CREATE TABLE IF NOT EXISTS Groups (
                                                ID integer PRIMARY KEY,
                                                GroupName text,
                                                MasterGroups integer,
                                                hasSubGroup Boolean
                                            ); """

sql_create_Locations_table = """ CREATE TABLE IF NOT EXISTS Locations (
                                                    ID integer PRIMARY KEY,
                                                    theLocation text,
                                                    Masterlocations integer,
                                                    hasSubLocations  boolean
                                                ); """

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def Find_Disk_On_ID(conn,ID):
    cur = conn.cursor()
    cur.execute("SELECT * FROM disks WHERE Disk_ID=?", (ID,))
    rows = cur.fetchall()
    return rows

def Find_Disk_On_MediaRef(conn,MediaRef):
    cur = conn.cursor()
    cur.execute("SELECT * FROM disks WHERE Media_ref=?", (MediaRef,))
    rows = cur.fetchall()
    #print (rows)
    return rows

def PullNextMediaRef(conn):
    cur = conn.cursor()
    cur.execute("SELECT Media_ref FROM disks")
    rows = cur.fetchall()
    temp = []
    for r in rows:
        tempvalue = int(r[0])
        temp.append(tempvalue)
    return str(max(temp)+1)

def Find_all_Borrows(conn):
    cur = conn.cursor()
    cur.execute("SELECT Aborrows.Engineer_ID,"
                " Aborrows.Date_Taken,"
                " Aborrows.Date_Returned, "
                "Persons.Person_ID,"
                "Persons.Person_Name,"
                "disks.Media_ref,"
                "disks.Description  "
                "FROM ((Aborrows "
                "Inner Join Persons ON Aborrows.Engineer_ID = Persons.Person_ID)"
                "Inner Join disks ON disks.Disk_ID = Aborrows.Media_ID) "
                "")
    rows = cur.fetchall()
    return  rows

def LoadDiskData(conn):
    cur = conn.cursor()
    #("Active_Disk", "Media_ref", "Description", "Checksum", "Location","Group", "Part Number", "Version_Number")
    #Disk_ID     Active_Disk  Media_ref   Description         Checksum    Location_ID  Group_ID    part_number  Version_Number  Field_1     Field_2
    cur.execute("SELECT DISKS.Active_Disk, "
                "DISKS.Media_ref, "
                "DISKS.Description, "
                "DISKS.Checksum, "
                "Locations.theLocation, "
                "Groups.GroupName, "
                "DISKS.part_number, "
                "DISKS.Version_Number "
                "FROM ((DISKS "
                "Inner Join Locations ON Disks.Location_ID = Locations.ID)"
                "Inner Join Groups ON disks.Group_ID = Groups.ID) "
                "")
    rows = cur.fetchall()
    return  rows

def PrepareGroups():
    #ID integer, GroupName  text, MasterGroups integer, hasSubGroup Boolean
    ID = None
    GroupName = "Test_Group"
    MasterGroups = 0
    hasSubGroup = False
    group = (ID, GroupName, MasterGroups, hasSubGroup)
    return group

def PrepareLocations():
    # ID integer PRIMARY KEY, theLocation text, Masterlocations integer, hasSubLocations  boolean,
    ID = None
    theLocation = "Test_Group"
    Masterlocations = 0
    hasSubLocations = False
    location = (ID, theLocation, Masterlocations, hasSubLocations)
    return location

def PreparePersons():
    #Active BOOLEAN, Person_ID integer PRIMARY KEY, Person_Name text NOT NULL
    Active = True
    Person_ID = None
    Person_Name = "Clive"
    person = (Active, Person_ID, Person_Name)
    return person

def Prepare_Disk(conn):
    diskID= None
    Active_Disk= True
    Media_ref = PullNextMediaRef(conn)
    Description ="third  disk attempt"
    Checksum = "002000"
    Location_ID ="2"
    Group_ID ="2"
    part_number = "PN"
    Version_number = "Version"
    Field_1 ="f1"
    Field_2 ="f2"
    Disk =   (diskID,Active_Disk, Media_ref, Description,Checksum,Location_ID , Group_ID, part_number, Version_number, Field_1, Field_2)
    return Disk

def CreateDisk(conn, theDisc):
    sql = ''' INSERT INTO disks(Disk_ID,Active_Disk, Media_ref, Description,Checksum,Location_ID , Group_ID, part_number, Version_number, Field_1, Field_2)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, theDisc)
    conn.commit()

def createPerson(conn,person):
    # Active BOOLEAN, Person_ID integer PRIMARY KEY, Person_Name text NOT NULL
    sql = ''' INSERT INTO Persons(Active,Person_ID,Person_Name) VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, person)
    conn.commit()

def createGroups(conn,group):
    # ID integer, GroupName  text, MasterGroups integer, hasSubGroup Boolean
    sql = ''' INSERT INTO Groups(ID,GroupName,MasterGroups,hasSubGroup) VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, group)
    conn.commit()

def createLocation(conn,location):
    # ID integer PRIMARY KEY, theLocation text, Masterlocations integer, hasSubLocations  boolean,
    sql = ''' INSERT INTO Locations(ID, theLocation, Masterlocations, hasSubLocations) VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, location)
    conn.commit()

def prepareAborrow():
    # Borrow_ID  integer    PRIMARY KEY, Engineer_ID integer, Media_ID integer, Date_Taken date, Date_Returned date,
    Borrow_ID = None
    Engineer_ID = 1
    Media_ID = 4
    #YY-MM-DD
    Date_Taken = "2020-01-31"
    Date_Returned = ""

    aB = (Borrow_ID,Engineer_ID,Media_ID,Date_Taken,Date_Returned)
    return aB

def creataABorrow(conn,aB):
    # Borrow_ID  integer    PRIMARY KEY, Engineer_ID integer, Media_ID integer, Date_Taken date, Date_Returned date,
    sql = ''' INSERT INTO ABorrows(Borrow_ID, Engineer_ID, Media_ID, Date_Taken, Date_Returned) VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, aB)
    conn.commit()

def createtable(conn):
    # create tables
    if conn is not None:
        # create disks table
        create_table(conn, sql_create_disks_table)

        # create borrows table
        create_table(conn, sql_create_ABorrows_table)

        # create persons
        create_table(conn, sql_create_Persons_table)

        #create group persons
        create_table(conn, sql_create_Groups_table)

        #create tables
        create_table(conn, sql_create_Locations_table)

    else:
        print("Error! cannot create the database connection.")

def returnMedia(conn,BorrowID):
    # Borrow_ID  integer    PRIMARY KEY, Engineer_ID integer, Media_ID integer, Date_Taken date, Date_Returned date,
    theDate = date.today()
    task = (BorrowID,2,3,4,theDate,BorrowID)
    sql = ''' UPDATE ABorrows
                  SET Borrow_ID = ? ,
                      Engineer_ID = ? ,
                      Media_ID = ? ,
                      Date_Taken = ? ,
                      Date_Returned = ?
                  WHERE Borrow_ID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def UpdateMedia(conn,Media):
    sql = ''' UPDATE disks
                    SET Disk_ID = ? ,
                        Active_Disk = ?, 
                        Media_ref = ?, 
                        Description= ? ,
                        Checksum = ?,
                        Location_ID = ? , 
                        Group_ID = ?,
                        part_number = ?,
                        Version_number = ?,
                        Field_1 = ?, Field_2 = ?
                WHERE Disk_ID = ? '''
    cur = conn.cursor()
    cur.execute(sql, Media)
    conn.commit()

def deActivatePerson(conn,ID):
    # Active BOOLEAN, Person_ID integer PRIMARY KEY, Person_Name text NOT NULL
    Clearance = (False,ID)
    sql = '''UPDATE Persons
                SET Active = ?
            WHERE Person_ID = ?'''
    cur = conn.cursor()
    cur.execute(sql, Clearance)
    conn.commit()

def SetupConnection():
    database = r"media_Table.db"
    # create a database connection
    conn = create_connection(database)
    createtable(conn)
    return conn

def returnGroupNames(conn):
    sql = '''SELECT GroupName 
            FROM Groups  '''
    cur =conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    #print(rows)
    return rows

def returnLocationNames(conn):
    sql = '''SELECT theLocation 
            FROM Locations  '''
    cur =conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    #print(rows)
    return rows

def SearchMedia(conn, searchterms):
    #print (searchterms)
    cur = conn.cursor()
    sql = ("SELECT DISKS.Active_Disk, "
                "DISKS.Media_ref, "
                "DISKS.Description, "
                "DISKS.Checksum, "
                "Locations.theLocation, "
                "Groups.GroupName, "
                "DISKS.part_number, "
                "DISKS.Version_Number "
                "FROM ((DISKS "
                "Inner Join Locations ON Disks.Location_ID = Locations.ID)"
                "Inner Join Groups ON disks.Group_ID = Groups.ID) "
                "WHERE DISKS.Media_ref LIKE ? "
                "AND DISKS.Description LIKE ? "
                "AND Groups.GroupName LIKE ? "
                "AND Locations.theLocation LIKE ? "
                "")
    cur.execute(sql,searchterms)
    searchterms
    rows = cur.fetchall()
    return rows