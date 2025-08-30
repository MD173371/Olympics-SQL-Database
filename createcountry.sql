/* createcountry.sql: MySQL file for country table creation*/
DROP TABLE IF EXISTS Country;
CREATE TABLE Country (
    countryID VARCHAR(3) PRIMARY KEY,
    countryName VARCHAR(100) NOT NULL,
    numBronze INT NOT NULL DEFAULT 0,
    numSilver INT NOT NULL DEFAULT 0,
    numGold INT NOT NULL DEFAULT 0
);

