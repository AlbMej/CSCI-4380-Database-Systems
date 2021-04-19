DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS enroll;
DROP TABLE IF EXISTS grades;

CREATE TABLE course(
  name VARCHAR(255),
  semester CHAR(3),
  time VARCHAR(63),
  location VARCHAR(63),
  capacity INTEGER,
  PRIMARY KEY (name, semester)
);

CREATE TABLE student(
  name VARCHAR(255),
  email VARCHAR(255) PRIMARY KEY ,
  major CHAR(4)
);

CREATE TABLE enroll(
  student_email VARCHAR(255),
  course_name VARCHAR(255),
  semester CHAR(3),
  registered TIMESTAMP DEFAULT now()
);

CREATE TABLE grades(
  student_email VARCHAR(255),
  course_name VARCHAR(255),
  semester CHAR(3),
  assignment VARCHAR(255),
  comments TEXT,
  grade FLOAT
);

INSERT INTO course(name, semester, time, location, capacity)
VALUES('Database Systems', 'S19', 'mr4-6', 'DCC-318', 168);


INSERT INTO course(name, semester, time, location, capacity)
VALUES('Database Systems', 'F18', 'w6-9', 'LOW-3039', 20);


INSERT INTO course(name, semester, time, location, capacity)
VALUES('Operating Systems', 'S19', 'tf10-12', 'DCC-318', 200);


INSERT INTO course(name, semester, time, location, capacity)
VALUES('Programming Languages', 'S19', 'mr12-2', 'DCC-318', 120);

INSERT INTO student(name, email, major)
VALUES ('alice', 'alice@example.com', 'CSCI');


INSERT INTO student(name, email, major)
VALUES ('bob', 'bob@example.com', 'CSCI');


INSERT INTO student(name, email, major)
VALUES ('carol', 'carol@example.co.uk', 'MATH');

INSERT INTO enroll(student_email, course_name, semester)
VALUES ('alice@example.com', 'Database Systems', 'S19');

INSERT INTO enroll(student_email, course_name, semester, registered)
VALUES ('bob@example.com', 'Database Systems', 'S19', '2018-11-30');

INSERT INTO grades(student_email, course_name, semester, assignment, comments, grade)
VALUES ('alice@example.com', 'Database Systems', 'S19', 'HW-1', NULL, .8);

INSERT INTO grades(student_email, course_name, semester, assignment, comments, grade)
VALUES ('alice@example.com', 'Database Systems', 'S19', 'HW-2', NULL, .7);

INSERT INTO grades(student_email, course_name, semester, assignment, comments, grade)
VALUES ('bob@example.com', 'Database Systems', 'S19', 'HW-1', NULL, .9);

INSERT INTO grades(student_email, course_name, semester, assignment, comments, grade)
VALUES ('bob@example.com', 'Database Systems', 'S19', 'HW-2', NULL, .55);