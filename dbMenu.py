import mysql.connector
import sys

# Menu display logic, calls functions for different tasks or exits
def menu(ODB):
    close = False

    while not close:
        displayDialog()
        option = input("Input required option number: ")
        if(option == '1'):
            insertData(ODB)
        elif(option == '2'):
            queryMenu(ODB)
        elif(option == '3'):
            customSelect(ODB)
        elif(option == '4'):
            insertNewData(ODB)
        elif(option == '5'):
            updateData(ODB)
        elif(option == '6'):
            deleteEntry(ODB)
        elif(option == '7'):
            addAthlete(ODB)
        elif(option == '8'):
            getAthleteMedals(ODB)
        elif(option == '0'):
            close = True
        else:
            print("Error: Option does not exist, try again")

# Get athlete medal procedure logic and error handling
def getAthleteMedals(ODB):
    cur = ODB.cursor()

    athleteID = input("Enter the ID of the athlete: ")

    try:
        cur.callproc('getAthleteMedals', (athleteID, ))

        for result in cur.stored_results():
            row = result.fetchone()

        print(row)

    except mysql.connector.errors.DatabaseError:
        print("Athlete Id doesnt exist or is in wrong format")
    
    cur.close()

# Add athlete medal procedure logic and error handling
def addAthlete(ODB):
    cur = ODB.cursor()

    athleteName = input("Enter the new athletes name: ")
    athleteGender = input("Enter the athletes gender (One character): ")
    athleteCountry = input("Enter the athletes country (3 Characters): ")
    athleteID = 0

    args = (athleteName, athleteGender, athleteCountry, athleteID)

    try:
        result = cur.callproc('addAthlete', args)
    
        athID = result[3]

        print("New athlete details: " + str(result))
    except mysql.connector.errors.DataError:
        print("Athlete not added, Input variables not in correct format")
    except mysql.connector.errors.IntegrityError:
        print("Athlete not added, Check foreign keys")
    
    ODB.commit()
    cur.close()

# Entry deletion logic
def deleteEntry(ODB):
    cur = ODB.cursor()
    
    tableMap = {
        '1': 'Athlete',
        '2': 'Country',
        '3': 'Event',
        '4': 'HeldAt',
        '5': 'Medal',
        '6': 'Sport',
        '7': 'Venue',
        } 
    

    displayInsertMenu()
    
    validInput = False
    
    option = input("Input Table to delete entry from: ")

    if int(option) > 0 and int(option) < 8:
        tableName = tableMap[option]
        
        cur.execute(f"DESCRIBE `{tableName}`")
        cols = cur.fetchall()
                        
        print("\nThese are the fields of the table:")
        numCols = len(cols)

        for col in cols:
            print("Field name: " + str(col[0]) + ", Data Type is " + str(col[1]))
        
        try:
            if tableName in ('Athlete', 'Country', 'Sport', 'Venue'):
                prevField = input("Enter the field to identify entry you wish to delete: ")
                prevData = input("Enter the value of field to identify the entry: ")
                 
                deleteQuery = f"DELETE FROM `{tableName}` WHERE `{prevField}` = %s"
                cur.execute(deleteQuery, (prevData,))
                
            if tableName in ('Event', 'HeldAt'):
                prevField1 = input("Enter 1st field to identify entry you wish to update: ")
                prevData1 = input("Enter the value of 1st field to identify the entry: ")
                prevField2 = input("Enter 2nd field to identify entry you wish to update: ")
                prevData2 = input("Enter the value of 2nd field to identify the entry: ")
                 
                deleteQuery = f"DELETE FROM `{tableName}` WHERE `{prevField1}` = %s AND `{prevField2}` = %s"

                cur.execute(deleteQuery, (prevData1, prevData2))
            
            if tableName == ('Medal'):
                prevField1 = input("Enter 1st field to identify entry you wish to update: ")
                prevData1 = input("Enter the value of 1st field to identify the entry: ")
                prevField2 = input("Enter 2nd field to identify entry you wish to update: ")
                prevData2 = input("Enter the value of 2nd field to identify the entry: ")
                prevField3 = input("Enter 3rd field to identify entry you wish to update: ")
                prevData3 = input("Enter the value of 3rd field to identify the entry: ")
                prevField4 = input("Enter 4th field to identify entry you wish to update: ")
                prevData4 = input("Enter the value of 4th field to identify the entry: ")

                deleteQuery = f"DELETE FROM `{tableName}` WHERE `{prevField1}` = %s AND `{prevField2}` = %s AND `{prevField3}` = %s AND `{prevField4}` = %s"

                cur.execute(deleteQuery, (prevData1, prevData2, prevData3, prevData4))
        
        except mysql.connector.errors.IntegrityError:
            print("Data not deleted, check foreign keys")
        except mysql.connector.errors.ProgrammingError:   
            print("Data not deleted, check field names")

    ODB.commit()
    cur.close()

# Data update logic
def updateData(ODB):
    cur = ODB.cursor()
    
    tableMap = {
        '1': 'Athlete',
        '2': 'Country',
        '3': 'Event',
        '4': 'HeldAt',
        '5': 'Medal',
        '6': 'Sport',
        '7': 'Venue',
        } 
    
    displayInsertMenu()
    option = input("Input Table to update value from: ")

    if int(option) > 0 and int(option) < 8:
        tableName = tableMap[option]
        
        cur.execute(f"DESCRIBE `{tableName}`")
        cols = cur.fetchall()
                        
        print("\nThese are the fields of the table:")
        numCols = len(cols)

        for col in cols:
            print("Field name: " + str(col[0]) + ", Data Type is " + str(col[1]))
        try:
            if tableName in ('Athlete','Country','Sport','Venue'):
                prevField = input("Enter the field to identify entry you wish to update: ")
                prevData = input("Enter the value of field to identify the entry: ")

                upField = input("Enter the field of the data you would like to update: ")
                upData = input("Enter the new value for the field: ")
                 
                updateQuery = f"UPDATE `{tableName}` SET `{upField}` = %s WHERE `{prevField}` = %s"
                cur.execute(updateQuery, (upData, prevData))
            
            if tableName in ('Event', 'HeldAt'):
                prevField1 = input("Enter 1st field to identify entry you wish to update: ")
                prevData1 = input("Enter the value of 1st field to identify the entry: ")
                prevField2 = input("Enter 2nd field to identify entry you wish to update: ")
                prevData2 = input("Enter the value of 2nd field to identify the entry: ")


                upField = input("Enter the field of the data you would like to update: ")
                upData = input("Enter the new value for the field: ")
                 
                updateQuery = f"UPDATE `{tableName}` SET `{upField}` = %s WHERE `{prevField1}` = %s AND `{prevField2}` = %s"

                cur.execute(updateQuery, (upData, prevData1, prevData2))
            
            if tableName == ('Medal'):
                prevField1 = input("Enter 1st field to identify entry you wish to update: ")
                prevData1 = input("Enter the value of 1st field to identify the entry: ")
                prevField2 = input("Enter 2nd field to identify entry you wish to update: ")
                prevData2 = input("Enter the value of 2nd field to identify the entry: ")
                prevField3 = input("Enter 3rd field to identify entry you wish to update: ")
                prevData3 = input("Enter the value of 3rd field to identify the entry: ")
                prevField4 = input("Enter 4th field to identify entry you wish to update: ")
                prevData4 = input("Enter the value of 4th field to identify the entry: ")

                upField = input("Enter the field of the data you would like to update: ")
                upData = input("Enter the new value for the field: ")
                 
                updateQuery = f"UPDATE `{tableName}` SET `{upField}` = %s WHERE `{prevField1}` = %s AND `{prevField2}` = %s AND `{prevField3}` = %s AND `{prevField4}` = %s"

                cur.execute(updateQuery, (upData, prevData1, prevData2, prevData3, prevData4))
        except mysql.connector.errors.IntegrityError:
            print("Data not updated, check foreign keys")
        except mysql.connector.errors.ProgrammingError:   
            print("Data not updated, check field names")

    ODB.commit()
    cur.close()

# Data insert logic
def insertNewData(ODB): 

    cur = ODB.cursor()
    
    tableMap = {
        '1': 'Athlete',
        '2': 'Country',
        '3': 'Event',
        '4': 'HeldAt',
        '5': 'Medal',
        '6': 'Sport',
        '7': 'Venue',
        } 
    
    displayInsertMenu()
    option = input("Input Table to insert into: ")

    if int(option) > 0 and int(option) < 8:
        tableName = tableMap[option]
        
        cur.execute(f"DESCRIBE `{tableName}`")
        cols = cur.fetchall()
                        
        print("\nEnter inputs for fields of selected Table:")
        numCols = len(cols)
        listInserts = [] 

        for col in cols:
            print("Data Type is " + str(col[1]))
            if col[3] == '':
                print("Value is not a key")
            elif col[3] == 'PRI':
                print("Value is primary key")
            elif col[3] == 'UNI':
                print("Value must be unique")
            else:
                print("Value is a foreign key, make sure it exists")
            current = input("Enter value for " + str(col[0]) + ": ")
            listInserts.append(current)
        
        tupleInserts = tuple(listInserts)
        
        placeholders = ("%s, " * (numCols - 1)) + "%s"

        insertQuery = f"INSERT INTO `{tableName}` VALUES (" + placeholders + ")"
        
        try:
            cur.execute(insertQuery, tupleInserts)
        except mysql.connector.errors.DatabaseError:
            print("Data not inserted, Incorrect input for insert statements")
            
    ODB.commit()
    cur.close()

# Displays tables in database
def displayInsertMenu():
    print()
    print("<1> Athlete")
    print("<2> Country")
    print("<3> Event")
    print("<4> HeldAt")
    print("<5> Medal")
    print("<6> Sport")
    print("<7> Venue")
    print("<0> Exit insertion menu")
    print() 

# Custom select query logic
def customSelect(ODB):
    cur = ODB.cursor()
    
    tableMap = {
        '1': 'Athlete',
        '2': 'Country',
        '3': 'Event',
        '4': 'HeldAt',
        '5': 'Medal',
        '6': 'Sport',
        '7': 'Venue',
        '8': 'medalDetailedView',   
        '9': 'sportDetailedView'
    }
    
    exitSelect = False
    
    while not exitSelect: 
        displayTableOptions()

        tableChoice = input("Enter table to view: ")
        print()

        if tableChoice == '0':
            exitSelect = True
        elif int(tableChoice) < 0 or int(tableChoice) > 9:
            print("Incorrect menu choice, try again.")
        else:
            
            tableName = tableMap[tableChoice]
            exitOption = False
            
            while not exitOption:
                print("<1> Display complete tables")
                print("<2> Search tables by field values")
                print("<0> Return\n")
                
                search = input("Input required option number: ")
                
                if search == '1':
                    selectQuery = f"SELECT * FROM `{tableName}`"
                    try: 
                        cur.execute(selectQuery)
                    except mysql.connector.errors.ProgrammingError as err: 
                        print(f"Error= {err}")
                    rows = cur.fetchall()

                    for row in rows:
                        print(row)

                    exitOption = True

                elif search == '2':
                    cur.execute(f"DESCRIBE `{tableName}`")
                    cols = cur.fetchall()
                    
                    print("\nFields of selected Table:")
                    for col in cols:
                        print(col[0], end=" ")
                    print("\n")
                   
                    print("The following inputs are case-insensitive")
                    field = input("Enter the field you wish to search by: ").strip()
                    selectQuery = f"SELECT * FROM `{tableName}` WHERE LOWER(`{field}`) LIKE LOWER(%s)"
                    value = input("Enter the value, or part of the value, you are searching for: ").strip()
                    searchValue = f"%{value}%"
                    
                    try: 
                        cur.execute(selectQuery, (searchValue, ))
                    except mysql.connector.errors.ProgrammingError as err: 
                        print(f"Error= {err}")
                    
                    rows = cur.fetchall()

                    for row in rows:
                        print(row)
                    exitOption = True

                elif search == '0':
                    exitOption = True
                else:
                    print("Incorrect input choice, try again\n")
                
                
                
    cur.close()

# Displays the tables and views
def displayTableOptions():
    print()
    print("<1> Athlete")
    print("<2> Country")
    print("<3> Event")
    print("<4> HeldAt")
    print("<5> Medal")
    print("<6> Sport")
    print("<7> Venue")
    print("<8> Detailed Medals")
    print("<9> Detailed Sports")
    print("<0> Exit custom display menu")
    print() 

# Query strings for the defined selection queries
def queryMenu(ODB):
    exitQMenu = False

    selectQueries = [ 
            """SELECT sportName AS 'Sport Name', sportCode AS 'Sport Code'
                FROM Sport
                WHERE sportName LIKE '%Gymnastics%'
                """,
            """ SELECT countryName AS 'Country Name', numBronze AS 'Bronze Medals Won', 
                    numSilver AS 'Silver Medals Won', numGold AS 'Gold Medals Won', 
                    (numBronze + numSilver + numGold) AS 'Total Medals Won'
                FROM Country
                WHERE (numBronze + numSilver + numGold) > 20
                ORDER BY `Total Medals Won` DESC;               
                """,
            """ SELECT (numBronze + numSilver + numGold) AS 'Total Medals', 
                    CONCAT(countryName, ' - ', countryID) AS 'Country and Country Code'
                FROM Country
                WHERE countryID IN ('AUS', 'CHN', 'MEX');               
                """,
            """SELECT MIN(date) AS 'First Medal Date', 
                    MAX(date) AS 'Last Medal Date', 
                    DATEDIFF(MAX(date), MIN(date)) AS 'Days Between'
                FROM Medal
                WHERE sportCode = 'CRD'
                """,
            """SELECT venueName AS 'Name of Venue', 
                    DATE_FORMAT(openDate, '%D %M %Y %r') AS 'Opening Date and Time', 
                    DATE_FORMAT(closeDate, '%D %M %Y %r') AS 'Closing Date and Time', 
                    TIMESTAMPDIFF(HOUR, openDate, closeDate) AS 'Hours open for Olympics'
                FROM Venue
                WHERE openDate BETWEEN '2024-07-24 12:00:00' AND '2024-07-28 12:00:00'
                """,
            """SELECT E.eventName AS 'Event Name'
                FROM Event E INNER JOIN 
                Sport S ON E.sportCode = S.sportCode
                WHERE S.sportName LIKE '%Swimming%'
                """,
            """SELECT C1.countryName AS "Country's Name", 
                    C1.numGold AS "Number of Gold Medals"
                FROM Country C1
                WHERE  C1.numGold = (
                    SELECT MAX(numGold)
                    FROM Country C2
                    )
                """,
            """SELECT DISTINCT A.name AS "Athlete's Name", A.gender AS "Gender", 
                    S.sportName AS "Competed Sport"
                FROM Athlete A INNER JOIN 
                Country C ON A.countryID = C.countryID
                INNER JOIN Medal M ON A.athleteID = M.athleteID
                INNER JOIN Sport S ON M.sportCode = S.sportCode
                WHERE C.countryName = 'Australia'
                    AND A.athleteID IN (
                        SELECT athleteID
                        FROM Medal
                        WHERE medalType = 'Gold Medal'
                        )
                ORDER BY A.name;
                """,
            """SELECT A.name AS 'Athlete Name', COUNT(*) AS 'Number of Events'
                FROM Medal M INNER JOIN
                Athlete A ON M.athleteID = A.athleteID
                WHERE A.countryID = 'AUS'
                GROUP BY A.athleteID
                HAVING COUNT(*) > 1
                """,
            """SELECT A.name AS 'Athlete Name', A.gender AS 'Gender', 
                    M.TotalMedals FROM Athlete A
                JOIN (
                    SELECT athleteID, COUNT(*) AS TotalMedals
                    FROM Medal
                    GROUP BY athleteID ) M
                    ON A.athleteID = M.athleteID
                WHERE M.TotalMedals > 1
                ORDER BY M.TotalMedals DESC 
                """
        ]

    while not exitQMenu:
        displayQueryDialog()
        queryOption = input("Input required query number:")
        if(queryOption == '1'):
            executeSelect(selectQueries[0], ODB)
        elif(queryOption == '2'):
            executeSelect(selectQueries[1], ODB)
        elif(queryOption == '3'):
            executeSelect(selectQueries[2], ODB)
        elif(queryOption == '4'):
            executeSelect(selectQueries[3], ODB)
        elif(queryOption == '5'):
            executeSelect(selectQueries[4], ODB)
        elif(queryOption == '6'):
            executeSelect(selectQueries[5], ODB)
        elif(queryOption == '7'):
            executeSelect(selectQueries[6], ODB)
        elif(queryOption == '8'):
            executeSelect(selectQueries[7], ODB)
        elif(queryOption == '9'):
            executeSelect(selectQueries[8], ODB)
        elif(queryOption == '10'):
            executeSelect(selectQueries[9], ODB)
        elif(queryOption == '0'):
            exitQMenu = True
        else:
            print("Error: Option does not exist, try again")

# Executes the select queries
def executeSelect(query, ODB):

    cur = ODB.cursor()

    cur.execute(query)

    rows = cur.fetchone()

    while rows is not None:
        print(rows)
        rows = cur.fetchone()
   
    cur.close()

# Defined queries menu
def displayQueryDialog():
    print()
    print("Display:")
    print("<1> Gymnastics Sports names and sport codes")
    print("<2> Details of countries that won more than 20 medals in solo events  ")
    print("<3> Total medals won by Australia, China and Mexico in solo events")
    print("<4> Date of first and last medal for cycling events, and number of days between ")
    print("<5> For venues that opened between the 24th and 28th of July 2024, show open and close datetime, and number of hours they were open for overall")
    print("<6> Show all the Swimming Events")
    print("<7> Show the country with the most solo event Gold Medals")
    print("<8> Show all gold winning athletes for solo events from Australia")
    print("<9> Show Australian athletes who won more than one medal")
    print("<10> Show all athletes who won multiple medals")
    print("OR:")
    print("<0> Exit select query menu")
    print()

# Prints the initial menu options
def displayDialog():
    print()
    print("<1> Insert csv file data into tables.")
    print("<2> Display defined queries.")
    print("<3> Search tables/Select queries with custom variables.")
    print("<4> Insert new custom data into tables.")
    print("<5> Update data entry from a table.")
    print("<6> Delete data entry from a table.")
    print("<7> Use add athlete procedure.")
    print("<8> Use get athlete medals procedure.")
    print("<0> Close the menu.")
    print()

# Iterates through each csv file and calls insert table with its information
def insertData(ODB):

    tables = [
        ['CountryData.csv', 'Country', 5],
        ['SportData.csv', 'Sport', 2],
        ['VenueData.csv', 'Venue', 4],
        ['AthleteData.csv', 'Athlete', 4],
        ['EventData.csv', 'Event', 2],
        ['HeldAtData.csv', 'HeldAt', 2],
        ['MedalData.csv', 'Medal', 5]
    ]

    # Insert data for each table
    for table in tables:
        insertTable(
            ODB,
            table[0],  # csvFile
            table[1],  # table_name
            table[2]   # numColumns
        )

    print("All data inserted.")

# Logic for the reading of csv files and execution of inserts
# adapted from https://www.w3schools.com/python/python_mysql_insert.asp
def insertTable(ODB, csvFile, tableName, numColumns):
    
    # Create cursor and empty list for row data
    cursor = ODB.cursor()
    table_data = []

    # Open and read CSV file
    with open(csvFile, 'r') as f:
        # Read the header line
        heading_line = f.readline().strip()
        # Read the rest of the lines
        data_lines = f.readlines()

    # Process each data line
    for line in data_lines:
        temp = line.strip().split(",")
        table_data.append(tuple(temp))

    # Create the SQL INSERT statement
    placeholders = ("%s, " * (numColumns - 1)) + "%s"
    sql_insert = "INSERT INTO " + tableName + " VALUES (" + placeholders + ")"

    # Execute the insertion, commit and close cursor
    try:
        cursor.executemany(sql_insert, table_data)
    except mysql.connector.errors.IntegrityError:
        print("Data already inserted")
    ODB.commit()
    cursor.close()

# Gets login information and makes db connection, then calls menu
# Closes database connection on exit
def main():
    # Prompt the user for MySQL database details
    username = input("Enter MySQL username: ")
    inPassword = input("Enter MySQL password: ")  
    databaseName = "olympics_17378383"

    # adapted from https://www.w3schools.com/python/python_mysql_getstarted.asp
        
    # Attempt to connect to the MySQL database
    try:
        ODB = mysql.connector.connect(
            host = "localhost",
            user = username,
            password = inPassword,
            database = databaseName,
            ssl_disabled = True
        )
        print("Connected to MySQL database.")
    except mysql.connector.Error as e:  # from MySQL Documentation
        print("ERROR: Could not connect to the database.", e)
        sys.exit(1)

    
    menu(ODB)

    # Close database connection
    ODB.close()

if __name__ == "__main__":
    main()
