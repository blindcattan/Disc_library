#################
#Initial Verison#
#################

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


def main():
    database = r"media_Table.db"
    # create a database connection
    conn = create_connection(database)
    createtable(conn)
    # diskID,Active_Disk, Media_ref, Description,Checksum,Location_ID , Group_ID, part_number, Version_number, Field_1, Field_2
    with conn:
        #Create Disk
        #theDisc = Prepare_Disk()
        #lastrow = CreateDisk(conn, theDisc)

        #Create Person
        #thePerson = PreparePersons()
        #createPerson(conn,thePerson)

        #Create Group
        #theGroup = PrepareGroups()
        #createGroups(conn,theGroup)

        #Create Locations
        #theLocation = PrepareLocations()
        #createLocation(conn, theLocation)

        #creataABorrow(conn,prepareAborrow())

        #return the book
        #returnMe"dia(conn,1)

        #Update Disk
        # (diskID,Active_Disk, Media_ref, Description,Checksum,Location_ID , Group_ID, part_number, Version_number, Field_1, Field_2)
        #mediaUpdate =  (2,True,"05445", "UpdatedDescription","1111111!",3,1,"Part Number Changed"," version 2.2", "F1.1","F1.2",2)
        #UpdateMedia(conn,mediaUpdate)

        deActivatePerson(conn,1)


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

def Prepare_Disk():
    diskID= None
    Active_Disk= True
    Media_ref = "0507"
    Description ="Second disk attempt"
    Checksum = "000000"
    Location_ID ="1"
    Group_ID ="1"
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
    Engineer_ID = 0
    Media_ID = 0
    #YY-MM-DD
    Date_Taken = "2020-01-31"
    Date_Returned = "2020-02-31"

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

if __name__ == '__main__':
    main()

