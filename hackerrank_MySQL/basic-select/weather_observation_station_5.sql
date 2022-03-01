SELECT CITY, length(CITY) FROM STATION
order by length(city),city ASC
limit 1;

-- and 

SELECT CITY, length(CITY) FROM STATION
order by length(city) DESC
limit 1;
