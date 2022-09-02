SELECT 
	name_album, 
	release_year
FROM albums
WHERE TO_CHAR(release_year, 'YYYY') = '2018'
;

SELECT 
	name_composition,
	duration
FROM 
	compositions
ORDER BY duration DESC
LIMIT 1
;

SELECT 
	name_composition,
	duration
FROM 
	compositions
WHERE duration > 3.5
ORDER BY duration 
;

SELECT 
	name_digest, 
	release_year
FROM 
	digests
WHERE release_year BETWEEN '2018-01-01' AND '2020-12-31'
;

SELECT 
	name_artist
FROM artists
WHERE name_artist NOT LIKE '% %'
;


SELECT 
	name_composition
FROM compositions
WHERE 
	name_composition ~* '.*мой.*' 
	OR name_composition ~* '.*my.*'
;







