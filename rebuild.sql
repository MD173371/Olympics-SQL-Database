-- Creating tables in olympics database and adding triggers, procedures and views

\. createdb.sql

DROP TABLE IF EXISTS Medal;
DROP TABLE IF EXISTS HeldAt;
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Athlete;
DROP TABLE IF EXISTS Venue;
DROP TABLE IF EXISTS Sport;
DROP TABLE IF EXISTS Country;

\. createcountry.sql
\. createsport.sql
\. createvenue.sql
\. createathlete.sql
\. createevent.sql
\. createheldat.sql
\. createmedal.sql

\. addAthlete.sql
\. getAthleteMedals.sql
\. medalUpdate.sql
\. medalDelete.sql
\. medalDetailedView.sql
\. sportDetailedView.sql
