# getAthleteMedals procedure
# Allows for the detailed display of an athletes medals when there ID is input
# Id is input as first and only variable

DROP VIEW IF EXISTS medalDetailedView2;
DROP PROCEDURE IF EXISTS getAthleteMedals;
CREATE VIEW medalDetailedView2 AS
SELECT
    C.countryName,
    A.name AS 'athleteName',
    A.athleteID,
    M.medalType,
    M.eventName,
    S.sportName,
    M.date
FROM Country C INNER JOIN
Athlete A ON C.countryID = A.countryID
INNER JOIN Medal M ON A.athleteID = M.athleteID
INNER JOIN Sport S ON M.sportCode = S.sportCode;

DELIMITER //

CREATE PROCEDURE getAthleteMedals (
    IN inAthleteID INT
)
BEGIN
    SELECT
        MD.countryName AS `Country`,
        MD.athleteName AS `Athlete Name`,
        MD.medalType AS `Medal Type`,
        MD.eventName AS `Event Name`,
        MD.sportName AS `Sport Name`,
        MD.date AS `Date Awarded`
    FROM medalDetailedView2 MD
    WHERE MD.athleteID = inAthleteID
    ORDER BY MD.date DESC;
END
//

DELIMITER ;
