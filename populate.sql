INSERT INTO Fuels(fuel_name) 
VALUES ('oil'), ('hydro'), ('solar'), ('gas'), ('wind'), ('coal'), ('biomass');

INSERT INTO Owners(owner_name)
VALUES ('Unión Eléctrica'),
('SunRay Power LLC'),
('126 Grove Solar LLC'),
('Skypower Ltd / Sunedison'),
('PAR Renewables'),
('Konoike Pacific'),
('Avidan Energy Solutions'),
('Rochelle Municipal Utilities'),
('158th Fighter Wing'),
('180 Raritan Energy Solutions LLC');

INSERT INTO Powerplants(id,	name, country, capacity, latitude, longtitude, owner, fuel_type)
VALUES ('WRI1002017', '10 De Octubre (nuevitas) Powerplant', 'Cuba', 280.0, 21.5656, -77.2711, 1, 1),
('USA0059371', '12 Applegate Solar LLC', 'United States of America', 1.9, 40.2003, -74.5761, 2, 3),
('USA0060858', '126 Grove Solar LLC', 'United States of America', 2.0, 42.0761, -71.4227, 3, 3),
('CAN0007595', '13th Side Road', 'Canada', 9.5, 42.855, -80.3607, 4, 3),
('GBR0005673', '14 Tullywiggan Road', 'United Kingdom', 1.0, 54.6221, -6.7398, 5, 7),
('USA0057310', '1420 Coil Av #C', 'United States of America', 1.3, 33.7943, -118.2414, 6, 3),
('USA0057458', '145 Talmadge Solar', 'United States of America', 3.8, 40.5358, -74.3913, 7, 3),
('USA0007770', '1515 S Caron Road', 'United States of America', 4.2, 41.9084, -89.0466, 8, 4),
('USA0060542', '158th Fighter Wing Solar Farm', 'United States of America', 1.3, 44.4777, -73.1534, 9, 3),
('USA0058187', '180 Raritan Solar', 'United States of America', 1.9, 40.5161, -74.34, 10, 3);




