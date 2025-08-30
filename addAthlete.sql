# addAthlete procedure
# Allows for adding athletes easily though generating an athleteID for them.
# Returns the generated id into the 4th provided variable

DROP PROCEDURE IF EXISTS addAthlete;
DELIMITER //
CREATE PROCEDURE addAthlete(
    IN inName VARCHAR(200),
    IN inGender VARCHAR(1),
    IN inCountryID VARCHAR(3),
    OUT outAthleteID INT
)
    BEGIN
        DECLARE maxID INT;

        SELECT MAX(athleteID) INTO maxID
        FROM Athlete;

        SET outAthleteID = maxID + 1;

        INSERT INTO Athlete(athleteID, name, gender, countryID)
        VALUES(outAthleteID, inName, inGender, inCountryID);
    END
//
DELIMITER ;
