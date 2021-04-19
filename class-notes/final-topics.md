# Final Exam Topics 

Exam Date: **Saturday May 4, 11:30am-2:30pm, Location TBA**

Exam will be:
- Open Note
- Open Book
- No electronic devices of any kind
- Individual Effort (no collaboration with others)
- 3 hours long

A portion of the exam will be multiple choice. Points will be awarded for correct answers, and a percentage of the number of incorrect answers will be deducted (specifics given on the exam).

The remainder will be short-answer, similar to the midterm.

## Previous Topics

All [topics from the midterm](midterm-topics.md) are potentially covered (comprehensive exam). Previous topics will make up no more than a quarter of the exam.

In addition, the following topics which were exempted from the midterm may be included:

Views and Indexes

Triggers and Stored procedures

Storage of records on disk

## SQL in Applications

Know about the SQL environment
- Schemas
- Catalogs
- Clusters

Basics of JDBC and connecting with python
- recognize and fix SQL injection

Understand the difference between data stored with symmetric and asymmetric encryption

## User Authorization

Understand the concept of authorization IDs

### Privileges

Understand the different types of privileges

Know how they're created and passed from user to user

Understand how they're revoked

## Semi-Structured Data

Understand the differences between relational and semi-structured data

Know the motivations for using semi-structured data

### XML

Know the basic syntax/structure

Know about well-formed vs valid XML

Be able to understand DTDs and XML Schemas

Be able to read XPaths, possibly construct simple ones

## Arranging Data on Disk

Fixed Length Records

Different address spaces (logical vs physical vs memory)

## Index Structures

Sparse vs Dense

Primary vs Secondary

Indirection in indexes (buckets)

### B-Trees

Know about B-Trees

How they're structured 

Understand querying/inserting

### Hash Tables

Understand secondary storage hash tables 

Understand extensible hashtables 

*Multidimensional indexes will not be covered*

## Physical Query Plans

Know about the basic operators (table scan, index scan, sort-scan)

Know the basics of the cost model:
- M 
- B 
- t

Know the basics of each algorithm we discussed

- One-pass algorithms
- One-and-a-half (nested loop) algorithms
- Two-pass algorithms

Understand how each works and the associated costs 

## Query Optimizations

Parse-trees: know how they're constructed

Operations allowed on logical query plans 
- Pushing selection/projection/duplicate elimination up and down the tree 
- What optimizations do we typically want to do

Don't need to be able to convert between parse-tree and logical query plan

## Coping with System failure

Understand the concept of a transaction

Understand how each type of logging allows us to return to a consistent state
- Undo
- Redo 
- Undo/Redo 

Understand checkpointing 

## NoSQL

Will not be on the exam

## Parallelism

Understand the basic architectures

Understand the map/reduce framework

Be able to write simple map and reduce functions 