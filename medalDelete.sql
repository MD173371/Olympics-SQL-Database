# medalDelete trigger
# Allows for thee update of medal tallies when a medal tuple is deleted

DROP TRIGGER IF EXISTS medalDelete;
DELIMITER //
CREATE TRIGGER medalDelete
AFTER DELETE ON Medal
FOR EACH ROW
    BEGIN
        DECLARE country VARCHAR(3);

        SELECT countryID INTO country
        FROM Athlete
        WHERE athleteId = OLD.athleteID;

        IF OLD.medalType = 'Gold Medal' THEN
            UPDATE Country
            SET numGold = numGold - 1
            WHERE countryID = country;
        ELSEIF OLD.medalType = 'Silver Medal' THEN
            UPDATE Country
            SET numSilver = numSilver - 1
            WHERE countryID = country;
        ELSEIF OLD.medalType = 'Bronze Medal' THEN
            UPDATE Country
            SET numBronze = numBronze - 1
            WHERE countryID = country;
        END IF;
    END//
DELIMITER ;

