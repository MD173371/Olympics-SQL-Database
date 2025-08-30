/* createsport.sql: MySQL file for sport table creation*/
DROP TABLE IF EXISTS Sport;
CREATE TABLE Sport (
    sportCode VARCHAR(3) PRIMARY KEY,
    sportName VARCHAR(100) NOT NULL UNIQUE
);

