# Task-Manager and Reminder
This is a simple Python Programme that helps you remember things by following the concept of spaced-repetition. You can also add reminders to it for custom dates.

## Before Using
create a database named task_manager in mysql. Inside the database, create two tables by the name **schedule** and **reminders**. Both the tables should have two columns: 
  1. Task (varchar (10000))
  2. Due_on (DATE)
  
 Or you can type the following commands in your terminal after starting the mysql server.
  1. `create database task_manager;`
  2. `create table schedule(Task varchar(10000), Due_on DATE);`
  3. `create table reminders(Task varchar(10000), Due_on DATE);`
  4. `exit`
 
