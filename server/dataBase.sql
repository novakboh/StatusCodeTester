CREATE DATABASE db_test;
USE db_test;

CREATE TABLE [Users] (
    [ID] INT IDENTITY PRIMARY KEY,
    [Name] VARCHAR(255),
    [Login] VARCHAR(255),
    [Password] VARCHAR(255)
);
CREATE TABLE [Tests] (
    [ID] INT IDENTITY PRIMARY KEY,
    [Name] VARCHAR(255),
    [Description] VARCHAR(255)
);
CREATE TABLE [Questions] (
    [ID] INT IDENTITY PRIMARY KEY,
	[TestID] INT FOREIGN KEY REFERENCES [Tests]([ID]),
    [Text] VARCHAR(255)
);
CREATE TABLE [Answers] (
    [ID] INT IDENTITY PRIMARY KEY,
	[QuestionID] INT FOREIGN KEY REFERENCES [Questions]([ID]),
    [Text] VARCHAR(255),
	[Correctness] VARCHAR(255)
);
CREATE TABLE [Results] (
    [ID] INT IDENTITY PRIMARY KEY,
	[UserID] INT FOREIGN KEY REFERENCES [Users]([ID]),
	[TestID] INT FOREIGN KEY REFERENCES [Tests]([ID]),
    [Date] DATE,
	[Percent] INT
);