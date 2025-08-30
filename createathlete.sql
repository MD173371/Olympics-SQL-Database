/* createathlete.sql: MySQL file for athlete table creation */
DROP TABLE IF EXISTS Athlete;
CREATE TABLE Athlete (
    athleteID INT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    countryID VARCHAR(3) NOT NULL,
    CONSTRAINT fk_Country
        FOREIGN KEY (countryID)
        REFERENCES Country(countryID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

