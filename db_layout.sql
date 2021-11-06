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
    Longitude FLOAT
);

CREATE TABLE PoleImages(
    PoleID INT REFERENCES Poles(PoleID),
    ImageID INT AUTO_INCREMENT PRIMARY KEY,
    OriginalName VARCHAR(50)
);

CREATE TABLE PoleReports(
    ReportID INT AUTO_INCREMENT PRIMARY KEY,
    ReporterID INT REFERENCES Users(UserID),
    Description VARCHAR(500),
    ReportDate DATETIME
);