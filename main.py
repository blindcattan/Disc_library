#################
# DAta Base split version Verison #
#################

import sqlite3, interface, DB_Backend
from datetime import date
from sqlite3 import Error


def main():
    conn = DB_Backend.SetupConnection()
    # diskID,Active_Disk, Media_ref, Description,Checksum,Location_ID , Group_ID, part_number, Version_number, Field_1, Field_2
    with conn:
        #Create Disk
        theDisc = DB_Backend.Prepare_Disk(conn)
        lastrow = DB_Backend.CreateDisk(conn, theDisc)

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

        #deActivatePerson(conn,1)

        #Find_Disk_On_ID(conn,2)

        #Find_all_Borrows(conn)

        #Find_Disk_On_MediaRef(conn, "0500" )
        #print (PullNextMediaRef(conn))

        interface.startWindowLoop(conn)


if __name__ == '__main__':
    main()

