CREATE TABLE IF NOT EXISTS departaments(
	id_departament INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name_departament VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS collaborators(
	id_collaborator INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name_collaborator VARCHAR(100) NOT NULL,
	id_departament INT NOT NULL,
	head_departament VARCHAR(100) UNIQUE,
	FOREIGN KEY (id_departament) REFERENCES departaments(id_departament)
);

ALTER TABLE departaments ADD COLUMN
						 head VARCHAR(100);
ALTER TABLE departaments ADD
						 FOREIGN KEY (head) 
					     REFERENCES collaborators(head_departament);

SELECT name_collaborator, name_departament, head
FROM collaborators
	INNER JOIN departaments ON collaborators.id_departament = departaments.id_departament 
						    AND collaborators.head_departament = departaments.head;