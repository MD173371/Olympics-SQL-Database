Olympics Database
User Guide for database
Name: Michael Thomas Patrick Durkan

Contains sections:
1. Set up
2. Menu usage
3. File Descriptions

1. How to setup database in linux (in order):

1. Run in terminal:
> pip3 install mysql-connector-python
2. Run in terminal:
> mysql -u dsuser -p
3. Enter password:
> userCreateSQL
4. Run within mysql:
> \. rebuild.sql
(details: Creates database, opens it, runs create table sql files
and adds advanced features)
5. Run in separate terminal:
> python3 dbMenu.py
6. Enter username:
> dsuser
7. Enter password:
> userCreateSQL
8. Type option ‘1’ in the dbMenu.py to insert the csv files into the database.
9. All tables, data, triggers, procedures and views should be now within mysql
database: database olympics_17378383
10. Type option ‘2’ in the dbMenu.py to view a list of select queries, and type
option ‘1’ - ‘10’ to display the different queries. .
Now the other interactive menu can be navigated by selecting options and closed by
entering ‘0’.


2. Interactive Menu Usage:

If need to re-open run python3 dbMenu.py in terminal and enter username: dsuser and
password: userCreateSQL
Listed are the details of every menu option and what they can be used for:
1. Insert csv file data into tables.
Used for adding the data from the csv files AthleteData.csv, CountryData.csv,
MedalData.csv, EventData.csv, SportData.csv, HeldAtData.csv, VenueData.csv to
their corresponding tables.
2. Display defined queries.
Displays the queries created in Part 3. of assignment tasks. Choose option 1-10.
3. Search tables/Select queries with custom variables.
Allows for a table, or view to be selected. Second selection dialog allows for either
the whole table to be viewed, or for the table to be searched by a certain value.
To use the search by value the name of the field that you wish to search through
must be typed in, followed by the value, or part of the value, of the field from the entry
you are looking for. Inputs are case-insensitive.
4. Insert new custom data into tables.
Allows for a new entry to be added into a table. First the table to add too is selected,
then the program goes through every field of the table and takes input from the user.
Key status and data type is presented before every input.
5. Update data entry from a table.
Allows for a data entries field to be updated. First the table to add too is selected,
then the field to identify the entry must be type in, followed by the value of this field.
Next the field to update is entered, followed by the value you would like to update it
to.
6. Delete data entry from a table.
Allows for a data entry to be deleted from a table. First the table to delete from is
selected, followed by typing in the field you wish to use to identify the entry. Next the
value of this field is entered.
7. Add athlete procedure
Allows for an athlete to be added, which assigns them a unique athleteID. The
athletes name, gender and country code are entered, and the details of the athlete
along with their ID are printed.
8. Use get athlete medals procedure.
Allows for an athlete's medals to be printed to the user. The athleteId must be
entered and the result will be displayed.


3. File Descriptions

Database Building files:
● createdb.sql : Creates the database olympics_17378383 and opens it for use.
● rebuild.sql: Runs createdb.sql as well as create tables, and trigger/procedure/view
creation files. Creates table in order needed for correct foreign key handling. Also
allows for resetting the database by dropping the tables in the required order if they
exist.
Create Table Files:
● createathlete.sql : Creates the Athlete table
● createcountry.sql : Creates the Country table
● createevent.sql : Creates the Event table
● createheldat.sql : Creates the HeldAt table
● createmedal.sql : Creates the Medal table
● createsport.sql : Creates the Sport table
● createvenue.sql : Creates the Venue table
Trigger Files:
● medalUpdate.sql : Creates the medal updating trigger for medal creation tallies
● medalDelete.sql : Creates the medal deleting trigger for medal deletion tallies
Procedure Files:
● getAthleteMedals.sql : Creates the athlete medals returning procedure
● addAthlete.sql : Creates the athlete adding procedure
Views:
● medalDetailedView.sql : Creates the detailed medal view
● sportDetailedView.sql : Creates the detailed sport view
Python Connector:
● dbMenu.py : Allows for interaction with database through python connector
CSV Files:
● AthleteData.csv : Contains the athlete data
● CountryData.csv : Contains the country data
● EventData.csv : Contains the event data
● HeldAtData.csv : Contains the sport location data
● MedalData.csv Contains the medal data
● SportData.csv : Contains the sport data
● VenueData.csv : Contains the venue data
Query File (Part 3)
● part3queries.sql : contains the queries defined in part 3, as a runnable sql file