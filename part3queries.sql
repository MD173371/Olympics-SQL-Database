#Part 3 - Designing Queries 

#1. Show all the Gymnastics Sports names and sport codes

SELECT sportName AS 'Sport Name', sportCode AS 'Sport Code'
FROM Sport
WHERE sportName LIKE '%Gymnastics%';

#2. Show the names and medal counts of countries that won more than 20 medals in solo events
SELECT countryName AS 'Country Name', numBronze AS 'Bronze Medals Won', numSilver AS 'Silver Medals Won', numGold AS 'Gold Medals Won', (numBronze + numSilver + numGold) AS 'Total Medals Won'
FROM Country
WHERE (numBronze + numSilver + numGold) > 20
ORDER BY `Total Medals Won` DESC;

#3. Show the total numbe of medals won by Australia, China and Mexico in solo events, display there names as a single column with Name and Country Code
SELECT (numBronze + numSilver + numGold) AS 'Total Medals', CONCAT(countryName, ' - ', countryID) AS 'Country and Country Code'
FROM Country
WHERE countryID IN ('AUS', 'CHN', 'MEX');

#4. Show the date of the first medal and last medal being awarded for cycling events, and the number of days between
SELECT MIN(date) AS 'First Medal Date', MAX(date) AS 'Last Medal Date', DATEDIFF(MAX(date), MIN(date)) AS 'Days Between'
FROM Medal
WHERE sportCode = 'CRD';

#5. For venues that opened between the 24th and 28th of July 2024, show the open and close dates and times in readable format, aswell as the number of hours they were open for over the whole olympics
SELECT venueName AS 'Name of Venue', DATE_FORMAT(openDate, '%D %M %Y %r') AS 'Opening Date and Time', DATE_FORMAT(closeDate, '%D %M %Y %r') AS 'Closing Date and Time', TIMESTAMPDIFF(HOUR, openDate, closeDate) AS 'Hours open for Olympics'
FROM Venue
WHERE openDate BETWEEN '2024-07-24 12:00:00' AND '2024-07-28 12:00:00';

#6. Show all the Swimming Events
SELECT E.eventName AS 'Event Name'
FROM Event E INNER JOIN 
Sport S ON E.sportCode = S.sportCode
WHERE S.sportName LIKE '%Swimming%';

#7. Show the country with the most solo event Gold Medals
SELECT C1.countryName AS "Country's Name", C1.numGold AS "Number of Gold Medals"
FROM Country C1
WHERE  C1.numGold = (
    SELECT MAX(numGold)
    FROM Country C2
);

#8. Show all gold winning athletes for solo events from Australia:
SELECT DISTINCT A.name AS "Athlete's Name", A.gender AS "Gender", S.sportName AS "Competed Sport"
FROM Athlete A INNER JOIN 
Country C ON A.countryID = C.countryID
INNER JOIN Medal M ON A.athleteID = M.athleteID
INNER JOIN Sport S ON M.sportCode = S.sportCode
WHERE C.countryName = 'Australia'
    AND A.athleteID IN (
        SELECT athleteID
        FROM Medal
        WHERE medalType = 'Gold Medal'
    )
ORDER BY A.name;

#9. Show Australian athletes who won more than one medal
SELECT A.name AS 'Athlete Name', COUNT(*) AS 'Number of Events'
FROM Medal M INNER JOIN
Athlete A ON M.athleteID = A.athleteID
WHERE A.countryID = 'AUS'
GROUP BY A.athleteID
HAVING COUNT(*) > 1;

#10. Show all athletes who won multiple medals
SELECT A.name AS 'Athlete Name', A.gender AS 'Gender', M.TotalMedals
FROM Athlete A
JOIN (
	SELECT athleteID, COUNT(*) AS TotalMedals
	FROM Medal
	GROUP BY athleteID ) M
	ON A.athleteID = M.athleteID
WHERE M.TotalMedals > 1
ORDER BY M.TotalMedals DESC;
