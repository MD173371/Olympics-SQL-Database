/* createmedal.sql: MySQL file for medal table creation*/
DROP TABLE IF EXISTS Medal;
CREATE TABLE Medal(
    medalType VARCHAR(20),
    eventName VARCHAR(100),
    sportCode VARCHAR(3),
    athleteID INT,
    date DATE NOT NULL,
    PRIMARY KEY (medalType, eventName, sportCode, athleteID),
    CONSTRAINT fk_Event
        FOREIGN KEY (eventName, sportCode)
        REFERENCES Event(eventName, sportCode)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_Athlete
       FOREIGN KEY (athleteID)
       REFERENCES Athlete(athleteID)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

