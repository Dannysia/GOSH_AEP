SELECT Longitude, Latitude FROM PoleImages WHERE ImageID = 1;
SELECT PlacemarkID, (SQRT(POWER(Latitude-(-82.6103),2))+POWER(Longitude-(38.0734),2)) AS Distance FROM KMLCoords ORDER BY Distance ASC LIMIT 1;
