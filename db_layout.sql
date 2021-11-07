CREATE TABLE Users(
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    _Password VARCHAR(64),
    _Disabled CHAR(1)
);

CREATE TABLE Poles(
    PoleID INT AUTO_INCREMENT PRIMARY KEY,
    Latitude FLOAT,
    Longitude FLOAT,
    Altitude FLOAT
);

CREATE TABLE PoleImages(
    ImageID INT AUTO_INCREMENT PRIMARY KEY,
    OriginalName VARCHAR(100),
    DateTaken DATETIME,
    LikelyPole INT REFERENCES PoleID,
    Latitude FLOAT,
    Longitude FLOAT,
    Altitude FLOAT
);

CREATE TABLE PoleReports(
    ReportID INT AUTO_INCREMENT PRIMARY KEY,
    ReporterID INT REFERENCES Users(UserID),
    Description VARCHAR(500),
    ReportDate DATETIME
);

CREATE TABLE KMLCoords(
    PlacemarkID CHAR(9),
    Type CHAR(1),
    Latitude DOUBLE,
    Longitude DOUBLE,
    Altitude DOUBLE,
    AltitudeMode VARCHAR(50),
    Extrude INT,
    PRIMARY KEY(PlacemarkID, Type)
);