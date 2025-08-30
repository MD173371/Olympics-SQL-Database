# medalUpdate Trigger
# Allows for the update of medal tallies when a medal tuple is added

DROP TRIGGER IF EXISTS medalUpdate;
DELIMITER //
CREATE TRIGGER medalUpdate
AFTER INSERT ON Medal
FOR EACH ROW
    BEGIN
        DECLARE country VARCHAR(3);
        DECLARE err_msg_invalidMedal VARCHAR(100);

        SET err_msg_invalidMedal = CONCAT('The medal input for ', NEW.athleteID, ' is invalid');

        SELECT countryID INTO country
        FROM Athlete
        WHERE athleteId = NEW.athleteID;


        IF NEW.medalType = 'Gold Medal' THEN
            UPDATE Country
            SET numGold = numGold + 1
            WHERE countryID = country;
        ELSEIF NEW.medalType = 'Silver Medal' THEN
            UPDATE Country
            SET numSilver = numSilver + 1
            WHERE countryID = country;
        ELSEIF NEW.medalType = 'Bronze Medal' THEN
            UPDATE Country
            SET numBronze = numBronze + 1
            WHERE countryID = country;
        ELSE
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = err_msg_invalidMedal;
        END IF;
    END//
DELIMITER ;

