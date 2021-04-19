--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.10.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.10.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.teaching DROP CONSTRAINT IF EXISTS teaching_professor_email_fkey;
ALTER TABLE IF EXISTS ONLY public.teaching DROP CONSTRAINT IF EXISTS teaching_course_fkey;
ALTER TABLE IF EXISTS ONLY public.professor DROP CONSTRAINT IF EXISTS professor_teaching_fk;
DROP TRIGGER IF EXISTS insert_database_student_trigger ON public.database_students;
ALTER TABLE IF EXISTS ONLY public.teaching DROP CONSTRAINT IF EXISTS teaching_professor_email_key;
ALTER TABLE IF EXISTS ONLY public.teaching DROP CONSTRAINT IF EXISTS teaching_course_semester_key;
ALTER TABLE IF EXISTS ONLY public.student DROP CONSTRAINT IF EXISTS student_pkey;
ALTER TABLE IF EXISTS ONLY public.professor DROP CONSTRAINT IF EXISTS professor_pkey;
ALTER TABLE IF EXISTS ONLY public.course DROP CONSTRAINT IF EXISTS course_pkey;
DROP TABLE IF EXISTS public.teaching;
DROP TABLE IF EXISTS public.professor;
DROP TABLE IF EXISTS public.grades;
DROP VIEW IF EXISTS public.database_students;
DROP TABLE IF EXISTS public.student;
DROP VIEW IF EXISTS public.database_enrollment;
DROP TABLE IF EXISTS public.enroll;
DROP TABLE IF EXISTS public.course;
DROP FUNCTION IF EXISTS public.new_sum(double precision[]);
DROP FUNCTION IF EXISTS public.insert_database_student();
DROP FUNCTION IF EXISTS public.failing_grades(email character varying);
DROP SCHEMA IF EXISTS public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: failing_grades(character varying); Type: FUNCTION; Schema: public; Owner: example
--

CREATE FUNCTION public.failing_grades(email character varying) RETURNS SETOF double precision
    LANGUAGE plpgsql
    AS $$
  DECLARE
    student_grade grades.grade%TYPE;
  BEGIN
    FOR student_grade IN 
      SELECT grade 
      FROM grades 
      WHERE student_email = email LOOP
        
      IF student_grade < .6 THEN 
        RETURN NEXT student_grade;
      END IF;
      
    end loop;    
    
    RETURN;
end;
  $$;


ALTER FUNCTION public.failing_grades(email character varying) OWNER TO example;

--
-- Name: insert_database_student(); Type: FUNCTION; Schema: public; Owner: example
--

CREATE FUNCTION public.insert_database_student() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
  BEGIN 
    INSERT INTO enroll(student_email, course_name, semester)
    VALUES (NEW.student_email, 'Database Systems', 'S19');
    RETURN NEW;
end
  $$;


ALTER FUNCTION public.insert_database_student() OWNER TO example;

--
-- Name: new_sum(double precision[]); Type: FUNCTION; Schema: public; Owner: example
--

CREATE FUNCTION public.new_sum(double precision[]) RETURNS integer
    LANGUAGE plpgsql
    AS $_$
  declare
    result integer := 0;
    i integer;
  begin
    foreach i in ARRAY $1 LOOP
      result := result + (i * 100);
    end loop;
    return result;
  end;
  $_$;


ALTER FUNCTION public.new_sum(double precision[]) OWNER TO example;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: course; Type: TABLE; Schema: public; Owner: example
--

CREATE TABLE public.course (
    name character varying(255) NOT NULL,
    semester character(3) NOT NULL,
    "time" character varying(63),
    location character varying(63),
    capacity integer
);


ALTER TABLE public.course OWNER TO example;

--
-- Name: enroll; Type: TABLE; Schema: public; Owner: example
--

CREATE TABLE public.enroll (
    student_email character varying(255),
    course_name character varying(255),
    semester character(3),
    registered timestamp without time zone DEFAULT now()
);


ALTER TABLE public.enroll OWNER TO example;

--
-- Name: database_enrollment; Type: VIEW; Schema: public; Owner: example
--

CREATE VIEW public.database_enrollment AS
 SELECT enroll.student_email,
    enroll.semester
   FROM public.enroll
  WHERE ((enroll.course_name)::text ~~ '%Database%'::text);


ALTER TABLE public.database_enrollment OWNER TO example;

--
-- Name: student; Type: TABLE; Schema: public; Owner: example
--

CREATE TABLE public.student (
    name character varying(255),
    email character varying(255) NOT NULL,
    major character(4)
);


ALTER TABLE public.student OWNER TO example;

--
-- Name: database_students; Type: VIEW; Schema: public; Owner: example
--

CREATE VIEW public.database_students AS
 SELECT student.name AS student_name,
    student.email AS student_email
   FROM public.student,
    public.enroll
  WHERE (((student.email)::text = (enroll.student_email)::text) AND ((enroll.course_name)::text ~~ '%Database%'::text));


ALTER TABLE public.database_students OWNER TO example;

--
-- Name: grades; Type: TABLE; Schema: public; Owner: example
--

CREATE TABLE public.grades (
    student_email character varying(255),
    course_name character varying(255),
    semester character(3),
    assignment character varying(255),
    comments text,
    grade double precision
);


ALTER TABLE public.grades OWNER TO example;

--
-- Name: professor; Type: TABLE; Schema: public; Owner: example
--

CREATE TABLE public.professor (
    name character varying(255),
    email character varying(255) NOT NULL
);


ALTER TABLE public.professor OWNER TO example;

--
-- Name: teaching; Type: TABLE; Schema: public; Owner: example
--

CREATE TABLE public.teaching (
    course character varying(255),
    semester character(3),
    professor_email character varying(255)
);


ALTER TABLE public.teaching OWNER TO example;

--
-- Data for Name: course; Type: TABLE DATA; Schema: public; Owner: example
--

INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Database Systems', 'S19', 'mr4-6', 'DCC-318', 168);
INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Database Systems', 'F18', 'w6-9', 'LOW-3039', 20);
INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Operating Systems', 'S19', 'tf10-12', 'DCC-318', 200);
INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Programming Languages', 'S19', 'mr12-2', 'DCC-318', 120);
INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Calculus 1', 'S19', NULL, 'DCC-308', NULL);
INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Ethics', 'F19', NULL, NULL, NULL);
INSERT INTO public.course (name, semester, "time", location, capacity) VALUES ('Better Art History', 'F19', NULL, NULL, NULL);


--
-- Data for Name: enroll; Type: TABLE DATA; Schema: public; Owner: example
--

INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('bob@example.com', 'Database Systems', 'S19', '2018-11-30 00:00:00');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('alice@example.com', 'Ethics', 'F19', '2019-02-07 22:10:45.606704');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('bob@example.com', 'Ethics', 'F19', '2019-02-07 22:10:45.606704');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('faith', 'Ethics', 'F19', '2019-02-07 22:10:45.606704');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('harry@example.com', 'Ethics', 'F19', '2019-02-07 22:10:45.606704');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('ed@example.com', NULL, 'S19', '2019-02-19 21:22:34.97641');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('alice2@example.com', 'Database Systems', 'S19', '2019-02-04 16:03:39.245031');
INSERT INTO public.enroll (student_email, course_name, semester, registered) VALUES ('ed@example.com', 'Database Systems', 'S19', '2019-02-19 21:38:28.551858');


--
-- Data for Name: grades; Type: TABLE DATA; Schema: public; Owner: example
--

INSERT INTO public.grades (student_email, course_name, semester, assignment, comments, grade) VALUES ('alice@example.com', 'Database Systems', 'S19', 'HW-1', NULL, 0.800000000000000044);
INSERT INTO public.grades (student_email, course_name, semester, assignment, comments, grade) VALUES ('alice@example.com', 'Database Systems', 'S19', 'HW-2', NULL, 0.699999999999999956);
INSERT INTO public.grades (student_email, course_name, semester, assignment, comments, grade) VALUES ('bob@example.com', 'Database Systems', 'S19', 'HW-1', NULL, 0.900000000000000022);
INSERT INTO public.grades (student_email, course_name, semester, assignment, comments, grade) VALUES ('bob@example.com', 'Database Systems', 'S19', 'HW-2', NULL, 0.550000000000000044);


--
-- Data for Name: professor; Type: TABLE DATA; Schema: public; Owner: example
--



--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: example
--

INSERT INTO public.student (name, email, major) VALUES ('alice', 'alice@example.com', 'CSCI');
INSERT INTO public.student (name, email, major) VALUES ('bob', 'bob@example.com', 'CSCI');
INSERT INTO public.student (name, email, major) VALUES ('dave', 'dave@example.com', 'ARCH');
INSERT INTO public.student (name, email, major) VALUES ('edward', 'ed@example.com', 'CSCI');
INSERT INTO public.student (name, email, major) VALUES ('harold', 'harry@example.com', 'CSCI');
INSERT INTO public.student (name, email, major) VALUES ('george', 'george@example.com', 'CHEM');
INSERT INTO public.student (name, email, major) VALUES ('carol', 'carol@example.com', 'CHEM');


--
-- Data for Name: teaching; Type: TABLE DATA; Schema: public; Owner: example
--



--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (name, semester);


--
-- Name: professor professor_pkey; Type: CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_pkey PRIMARY KEY (email);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (email);


--
-- Name: teaching teaching_course_semester_key; Type: CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.teaching
    ADD CONSTRAINT teaching_course_semester_key UNIQUE (course, semester);


--
-- Name: teaching teaching_professor_email_key; Type: CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.teaching
    ADD CONSTRAINT teaching_professor_email_key UNIQUE (professor_email);


--
-- Name: database_students insert_database_student_trigger; Type: TRIGGER; Schema: public; Owner: example
--

CREATE TRIGGER insert_database_student_trigger INSTEAD OF INSERT ON public.database_students FOR EACH ROW EXECUTE PROCEDURE public.insert_database_student();


--
-- Name: professor professor_teaching_fk; Type: FK CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_teaching_fk FOREIGN KEY (email) REFERENCES public.teaching(professor_email);


--
-- Name: teaching teaching_course_fkey; Type: FK CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.teaching
    ADD CONSTRAINT teaching_course_fkey FOREIGN KEY (course, semester) REFERENCES public.course(name, semester);


--
-- Name: teaching teaching_professor_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: example
--

ALTER TABLE ONLY public.teaching
    ADD CONSTRAINT teaching_professor_email_fkey FOREIGN KEY (professor_email) REFERENCES public.professor(email);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

