SELECT DISTINCT(CITY) FROM STATION 
WHERE 
lower(substr(CITY,-1,1)) not in ('a','e','i','o','u')
or
lower(substr(CITY,1,1)) not in ('a','e','i','o','u');