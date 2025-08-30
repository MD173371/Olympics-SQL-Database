/* createvent.sql: MySQL file for event table creation*/
DROP TABLE IF EXISTS Event;
CREATE TABLE Event (
    eventName VARCHAR(100),
    sportCode VARCHAR(3),
    PRIMARY KEY (eventName, sportCode),
    CONSTRAINT fk_Sport
        FOREIGN KEY (sportCode)
        REFERENCES Sport(sportCode)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

