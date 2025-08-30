/* createheldat.sql: MySQL file for HeldAt table creation */
DROP TABLE IF EXISTS HeldAt;
CREATE TABLE HeldAt(
    venueCode INT,
    sportCode VARCHAR(3),
    PRIMARY KEY (venueCode, sportCode),
    CONSTRAINT fk_Venue
        FOREIGN KEY (venueCode)
        REFERENCES Venue(venueCode)
        ON UPDATE CASCADE,
    CONSTRAINT fk_Sport2
        FOREIGN KEY (sportCode)
        REFERENCES Sport(sportCode)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

