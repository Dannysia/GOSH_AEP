SELECT Longitude, Latitude FROM PoleImages WHERE ImageID = %(imageID)s
SELECT PlacemarkID, (SQRT(POWER(Latitude-%(targetLat)s,2))+POWER(Longitude-%(targetLong)s,2)) AS Distance FROM KMLCoords ORDER BY Distance ASC LIMIT 1
