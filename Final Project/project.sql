DROP TABLE IF EXISTS liquor;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS agency;
DROP TABLE IF EXISTS license_types;
DROP TABLE IF EXISTS crimes;

CREATE TABLE locations (
	id SERIAL PRIMARY KEY,
	city VARCHAR(63) NOT NULL,
	state CHAR(2) NOT NULL,
	zip VARCHAR(11),
	UNIQUE(city, state, zip)
);

CREATE TABLE agency (
id SERIAL PRIMARY KEY,
name VARCHAR(63),
num INT,
UNIQUE(name, num)
);

CREATE TABLE license_types (
	id SERIAL PRIMARY KEY,
	type_name VARCHAR(63),
	class_code INT,
	type_code VARCHAR(4),
	UNIQUE(class_code, type_code)
);

CREATE TABLE liquor (
	ser_num INT PRIMARY KEY,
	License_type_id INT REFERENCES license_types (id),
	Agency_id INT REFERENCES agency (id),
	county VARCHAR(63) NOT NULL,
	premise_name VARCHAR(63) NOT NULL,
	dba VARCHAR(63),
	address1 VARCHAR(63) NOT NULL,
	address2 VARCHAR(63),
	Location_id INT REFERENCES locations (id),
	cert_num INT,
	issue_date DATE,
	effect_date DATE,
	expir_date DATE,
	lat FLOAT, 
	long FLOAT
);

CREATE TABLE crimes (
	county VARCHAR(63) NOT NULL,
 	agency VARCHAR(63) NOT NULL,
	year INT NOT NULL,
	months_reported INT,
	total INT ,
	violent_total INT  ,
	murder INT ,
	rape INT ,
	robbery INT ,
	aggravated INT ,
	property INT,
	burglary INT ,
	larceny INT ,
	vehicle INT ,
	region VARCHAR(63),
	PRIMARY KEY(county, agency, year, region)
	
)	
	