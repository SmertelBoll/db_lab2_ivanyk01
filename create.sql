CREATE TABLE Owners(
	owner_id   SERIAL PRIMARY KEY,
	owner_name VARCHAR(255)
);

CREATE TABLE Fuels(
	fuel_id   SERIAL PRIMARY KEY,
	fuel_name VARCHAR(50)
);

CREATE TABLE Powerplants(
	id         VARCHAR(12) PRIMARY KEY,
	name       VARCHAR(255) NOT NULL,
	country    VARCHAR(255),
	capacity   NUMERIC,
	latitude   NUMERIC,
	longtitude NUMERIC,
	owner      INT REFERENCES Owners(owner_id) ON DELETE CASCADE,
	fuel_type  INT REFERENCES Fuels(fuel_id) ON DELETE RESTRICT
);