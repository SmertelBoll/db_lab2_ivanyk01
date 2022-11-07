SELECT name, capacity FROM powerplants 
WHERE country = 'United States of America'
ORDER BY capacity DESC;

SELECT fuel_name, COUNT(powerplants.id) FROM fuels
JOIN powerplants ON fuels.fuel_id = powerplants.fuel_type
GROUP BY fuel_name;

SELECT COUNT(fuel_name), SUM(powerplants.capacity) FROM fuels
JOIN powerplants ON fuels.fuel_id = powerplants.fuel_type
GROUP BY fuel_name
ORDER BY SUM(powerplants.capacity);