# medalDetailedView View
# Provides a detailed view of an athletes medals, including country and full name

DROP VIEW IF EXISTS medalDetailedView;
CREATE VIEW medalDetailedView AS
SELECT
    C.countryName AS 'Country',
    A.name AS 'Athlete',
    A.athleteID AS 'Athlete-ID',
    M.medalType AS 'Medal-Type',
    M.eventName AS 'Event-Name',
    S.sportName AS 'Sport-Name',
    M.date AS 'Awarded-Date'
FROM Country C INNER JOIN
Athlete A ON C.countryID = A.countryID
INNER JOIN Medal M ON A.athleteID = M.athleteID
INNER JOIN Sport S ON M.sportCode = S.sportCode;
