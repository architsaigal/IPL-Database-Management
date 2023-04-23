#IPL Database Management Project
#Stores records of all teams with their performance
#Enables insertion, deletion, alteration and selection of data

#Importing mysql.connector and prettytable
#mysql.connector helps in connecting mysql to python
#prettytable helps in printing the output properly

import mysql.connector as mydb
from prettytable import PrettyTable

#Connecting to database
#Change host, username and password according to system
db = mydb.connect(host="localhost",user="root",passwd="root")
#Creating a cursor
cur = db.cursor(buffered=True)

def line():
    """Draws a line"""
    for i in range(25):
               print("-",end="")

def arrow():
    """Draws an arrow"""
    for i in range(1):
               print(" >  ",end="")

def CreateDatabase():
    """Creates 'IPL' database"""
    cur.execute("CREATE DATABASE IF NOT EXISTS IPL;")
    print("DATABASE CREATED")
    
def UseDatabase():
    """Uses 'IPL' database"""
    cur.execute("USE IPL;")
      
def CreateTable():
    """ Creates 'IPL' table"""
    cur.execute("""CREATE TABLE IF NOT EXISTS IPL(TEAM VARCHAR(30),
    YEAR INT(4), CAPTAIN VARCHAR(20), COACH VARCHAR(20),
    WINS INT(2), LOSSES INT(2), TIED INT(2), NETRUNRATE DECIMAL(4,2),
    LEAGUEPOINTS INT(2), PRIMARY KEY(TEAM, YEAR));""")
    print("Table Created Successfully!")

def ShowTables():
    """Shows all tables in a database"""
    cur.execute("SHOW TABLES;")
    rows=cur.fetchall()
    y=PrettyTable(["Table Name"])
    for i in rows:
        y.add_row([i])
    print(y)

def DescribeTable():
    """Describes the structure of the table"""
    cur.execute("DESC IPL;")
    rows=cur.fetchall()
    y=PrettyTable(["Field","Type","Null","Key","Default","Extra"])
    for a,b,c,d,e,f in rows:
        y.add_row([a,b,c,d,e,f])
    print(y)

def InsertData():
    """ Inserts data into table"""
    a=input("Enter team name: ")
    b=int(input("Enter year: "))
    c=input("Enter captain name: ")
    d=input("Enter coach name: ")
    e=int(input("Enter no of wins: "))
    f=int(input("Enter no of losses: "))
    g=int(input("Enter no of tied games: "))
    h=float(input("Enter net run rate: "))
    i= int(input("Enter league points: "))
    cur.execute("""INSERT INTO IPL VALUES
    ('{}',{},'{}','{}',{},{},{},{},{});""".format(a,b,c,d,e,f,g,h,i))
    print("Data Inserted")
    db.commit()
    
def DeleteData():
    """Deletes specific rows"""
    line()
    print("Delete Data Sub Menu")
    print("| 1. Delete All Records                |")
    print("| 2. Delete by (Team, Year)            |")
    c= int(input("Enter your choice (1 or 2): "))
    
    #-----Choice 1
    if c==1:
      ch= input("Confirm: Do you want to delete all the data (Y/N): ")
      if ch=="Y":
        cur.execute("DELETE FROM IPL;")
        line()
        print("Data Removed")

      else:
        print("Exiting to main menu")

    #-----Choice 2
    elif c==2:
      t=input("Enter Team: ")
      y=int(input("Enter Year: "))
      ch=input("Confirm: Do you want to delete (Y/N)")
      if ch=="Y":
          cur.execute("DELETE FROM IPL WHERE TEAM='{}' AND YEAR='{}';".format(t,y))
          line()
          print("Data Removed")

      else:
          print("Exiting to main menu")
      
    db.commit()

def DisplayTable():
    """Displays all the data of the table"""
    cur.execute("SELECT * FROM IPL")
    rows=cur.fetchall()
    y = PrettyTable(["Team","Year","Captain","Coach","Wins","Losses","Tied","Net Run Rate","League Points"])
    for a,b,c,d,e,f,g,h,i in rows:
        y.add_row([a,b,c,d,e,f,g,h,i])
    print(y)

def ModifyData():
    """Modifies data in table"""
    DisplayTable()
    line()
    print("Modify Data Sub Menu- These are the columns you can modify-")
    print("1. Team")
    print("2. Year")
    print("3. Captain")
    print("4. Coach")
    print("5. Wins")
    print("6. Losses")
    print("7. Tied")
    print("8. NRR")
    print("9. League Points")
    ch=int(input("Enter the column to modify: "))

    #-----Choice 1- Changing Team Name
    if ch==1:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        t2= input("Enter the new team name: ")
        cur.execute("UPDATE IPL SET TEAM='{}' WHERE TEAM='{}' AND YEAR={}; ".format(t2,t1,y1))

    #-----Choice 2- Changing Year       
    elif ch==2:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        y2= int(input("Enter the new year: "))
        cur.execute("UPDATE IPL SET YEAR={} WHERE TEAM='{}' AND YEAR={};".format(y2,t1,y1))

    #-----Choice 3- Changing Captain Name
    elif ch==3:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        c1= input("Enter the new captain name: ")
        cur.execute("UPDATE IPL SET CAPTAIN='{}' WHERE TEAM='{}' AND YEAR={};".format(c1,t1,y1))

    #-----Choice 4- Changing Coach Name
    elif ch==4:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        c1= input("Enter the new coach: ")
        cur.execute("UPDATE IPL SET COACH='{}' WHERE TEAM='{}' AND YEAR={};".format(c1,t1,y1))

    #-----Choice 5- Changing Number of Wins
    elif ch==5:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        w1= int(input("Enter the new number of wins: "))
        cur.execute("UPDATE IPL SET WINS={} WHERE TEAM='{}' AND YEAR={};".format(w1,t1,y1))

    #-----Choice 6- Changing Number of Losses
    elif ch==6:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        l1= int(input("Enter the new number of losses: "))
        cur.execute("UPDATE IPL SET LOSSES={} WHERE TEAM='{}' AND YEAR={};".format(l1,t1,y1))

    #-----Choice 7- Changing Number of Tied Games
    elif ch==7:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        g1= int(input("Enter the new number of tied games: "))
        cur.execute("UPDATE IPL SET TIED={} WHERE TEAM='{}' AND YEAR={};".format(g1,t1,y1))

    #-----Choice 8- Changing Run Rate
    elif ch==8:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        n1= float(input("Enter the new net run rate: "))
        cur.execute("UPDATE IPL SET NETRUNRATE={} WHERE TEAM='{}' AND YEAR={};".format(n1,t1,y1))

    #-----Choice 9- Changing League Points
    elif ch==9:
        t1= input("Enter the team in the existing record: ")
        y1= int(input("Enter the year of the existing record: "))
        l1= int(input("Enter the new league points: "))
        cur.execute("UPDATE IPL SET LEAGUEPOINTS={} WHERE TEAM='{}' AND YEAR={};".format(l1,t1,y1))

    line()    
    print("Data Altered")    
    db.commit()

def SearchTable():
    """Selects and displays specific data"""
    line()
    print("Search Table Sub Menu")
    print("1. All records for a particular year")
    print("2. All records for a particular team")
    print("3. Teams qualified for play-offs for a particular year")
    print("4. Teams in order of run rate for a particular year")
    print("5. Exit to main menu")
    ch= int(input("Enter your choice: "))

    #-----Choice 1- Records For a Particular Year
    if ch==1:
        y= int(input("Enter the year: "))
        cur.execute("SELECT * FROM IPL WHERE YEAR={} ORDER BY LEAGUEPOINTS DESC;".format(y))
        rows=cur.fetchall()
        y = PrettyTable(["Team","Year","Captain","Coach","Wins","Losses","Tied","Net Run Rate","League Points"])
        for a,b,c,d,e,f,g,h,i in rows:
            y.add_row([a,b,c,d,e,f,g,h,i])
        print(y)

    #-----Choice 2- Records For a Particular Team
    elif ch==2:
        t= input("Enter the team name: ")
        cur.execute("SELECT * FROM IPL WHERE TEAM='{}' ORDER BY YEAR;".format(t))
        rows=cur.fetchall()
        y = PrettyTable(["Team","Year","Captain","Coach","Wins","Losses","Tied","Net Run Rate","League Points"])
        for a,b,c,d,e,f,g,h,i in rows:
            y.add_row([a,b,c,d,e,f,g,h,i])
        print(y)

    #-----Choice 3- Teams Qualified to Play-Offs For a Particular Year
    elif ch==3:
        y= int(input("Enter the year: "))
        cur.execute("SELECT * FROM IPL WHERE YEAR={} ORDER BY LEAGUEPOINTS DESC;".format(y))
        rows=cur.fetchmany(4)
        y = PrettyTable(["Team","Year","Captain","Coach","Wins","Losses","Tied","Net Run Rate","League Points"])
        for a,b,c,d,e,f,g,h,i in rows:
            y.add_row([a,b,c,d,e,f,g,h,i])
        print(y)

    #-----Choice 4- Decreasing Order of Run Rate For a Particular Year
    elif ch==4:
        y= int(input("Enter the year: "))
        cur.execute("SELECT * FROM IPL WHERE YEAR={} ORDER BY NETRUNRATE DESC;".format(y))
        rows=cur.fetchall()
        y = PrettyTable(["Team","Year","Captain","Coach","Wins","Losses","Tied","Net Run Rate","League Points"])
        for a,b,c,d,e,f,g,h,i in rows:
            y.add_row([a,b,c,d,e,f,g,h,i])
        print(y)

    
#__main__

while True:
    print("IPL Database Management System")
    print("1. Create Database 'IPL'")
    print("2. Use Database 'IPL'")
    print("3. Create a Table")
    print("4. Check if table is created")
    print("5. Display the structure of the table")
    print("6. Insert Data")
    print("7. Delete Data")
    print("8. Display all data")
    print("9. Modify Data")
    print("10. Search for Data")
    print("99. Exit")
    choice= int(input("Enter option: "))
    
    if choice==1:
        CreateDatabase()
        
    elif choice==2:
        UseDatabase()
        
    elif choice==3:
        UseDatabase()
        CreateTable()
        
    elif choice==4:
        UseDatabase()
        ShowTables()
        
    elif choice==5:
        UseDatabase()
        DescribeTable()
        
    elif choice==6:
        UseDatabase()
        InsertData()
        
    elif choice==7:
        UseDatabase()
        DeleteData()
        
    elif choice==8:
        UseDatabase()
        DisplayTable()
        
    elif choice==9:
        UseDatabase()
        AlterTable()
        
    elif choice==10:
        UseDatabase()
        SearchTable()
        
    elif choice==99:
        break

db.commit()
db.close()

