DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  rating TEXT,
  visited BOOLEAN
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  countries_id INT REFERENCES countries(id) ON DELETE CASCADE
);
