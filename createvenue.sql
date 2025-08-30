/* createvenue.sql: MySQL file for venue table creation /
DROP TABLE IF EXISTS Venue;
CREATE TABLE Venue (
    venueCode INT PRIMARY KEY,
    venueName VARCHAR(100) NOT NULL,
    openDate DATETIME,
    closeDate DATETIME
);

