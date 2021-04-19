# Midterm Exam Topics

Exam Date: **Thursday February 28, 4:00pm-5:50pm, DCC 318**

Exam will be:
- Open Note
- Open Book
- No electronic devices of any kind
- Individual Effort (no collaboration with others)
- 1 hour and 50 minutes long

## Database Overview

Know what a database (DBMS) is expected to do

Be able to identify which component of the database is responsible for what aspects of database operation

## Relational Model

Have a thorough understanding of the relational model

Know the notation for defining relations, attributes, and keys

### Keys

Know what a key is (vs a superkey)

Know what a key implies about its relation

### Defining relations in SQL

Be able to write a `CREATE TABLE` statement
- Have a good understanding of the various datatypes we've discussed. Know when each might be appropriate
- Keys and default values
- foreign keys
    - Default Policy
    - Cascade Policy
    - Set Null Policy
- Attribute and tuple constraints (e.g., `CHECK`)

Understand the difference between a table and a view, and what the implications are

### Algebraic Query Language

Know the operators, as applied to both sets and bags
- Set operators
- Operations that remove data
    - Selection (removes tuples)
    - Projection (including the "enhanced" projection we applied to bags) (removes columns)
- Operations that join tuples
    - Product 
    - Joins
        - Natural Join
        - Theta Join
        - Outer/Left/Right Joins
- Renaming
- Grouping and Aggregation
- Sorting

Know how we express constraints on relations

## Design Theory for Relational Databases

### Functional Dependencies

Know what they are and what they assert about the associated relation

Be able to find the key, given a set of FDs

Be able to compute the closure of attributes. Understand how to use the closure of attributes to determine if something is a key or superkey.

Be able to determine if a set of FDs forms a minimal basis

Understand and be able to apply the algorithm for **Projection of Functional Dependencies**

### Decomposing Relations

Know the three main types of anomalies

#### BCNF

Be able to determine if a relation is in BCNF

Be familiar with the algorithm for decomposing into BCNF

#### 3NF

Be able to determine if a relation is in 3NF

Be familiar with the algorithm for decomposing into 3NF

### Database Design

#### Entity-Relationship Model

Know the components of an E/R Diagram, what they represent:
- Entity Sets
- Attributes
- Relationships
- Multiplicity of relationships
- Subclasses
- Weak Entity Sets

Know how to convert an E/R diagram to a relational model

#### Design Principles

We outlined a few principles for good data model design. Be familiar with them.

## SQL Queries

Be able to read and write basic SQL queries

Know the role played by each of the `SELECT`, `FROM`, and `WHERE` clauses

Know the basics of `INSERT`, `UPDATE`, and `DELETE`

Understand how subqueries work (you won't have to write them)

Understand how Grouping works

We aren't looking for perfect syntax, but any SQL you write should reflect an understanding of how the language works.

Know what transactions do

Triggers and Stored Procedures will not be covered

## Secondary Storage Management

Understand how to calculate Parity

Know how each of RAID 1, RAID 4, and RAID 5 store data and parity information on disk, and how data would be restored in the case of disk failure

### Storage of records on Disk

Will not be covered.

# Examples

## Boyce Codd Normal Form

R(a, b, c, d, e, f)

FDs: ab->c, d->ef, f->c

Keys: abd

R1(a, b, c)
FDs: ab->c
a+ = a
b+ = b
c+ = c
ab+ = abc
bc+ = bc
ac+ = ac


R2(a, b, d, e, f)

FDs: d->ef

Keys: abd

a+ = a
b+ = b
d+ = defc
e+ = e
f+ = fc
ab+ = abc
ad+ = adefc
ae+ = ae
af+ = afc
...

R21(d, e, f)
FDs: d->ef


R22(d, a, b)

## 3NF

R(a, b, c, d, e, f)
c->ab, cd->f, fe->abc

c->a
c->b
fe->a
fe->b
fe->c

Keys: cde, fed

R1(c, a, b) <-- Don't need this, as it's part of R3
R2(c, d, f)
R3(f, e, a, b, c)
R4(c, d, e) or R4(f, e, d)