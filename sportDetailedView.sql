# sportDetailedView View
# Provides a detailed view of sports and there venue details

DROP VIEW IF EXISTS sportDetailedView;
CREATE VIEW sportDetailedView AS
SELECT
    S.sportName AS 'Sport-Name',
    V.venueName AS 'Venue-Name',
    V.openDate AS 'Open-Date',
    V.closeDate AS 'Close-Date'
FROM Sport S
INNER JOIN HeldAt H ON S.sportCode = H.sportCode
INNER JOIN Venue V ON H.venueCode = V.venueCode;
