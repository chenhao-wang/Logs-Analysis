# Logs Analysis
> Chenhao Wang

## To Run

### Prepare the software and data

- The virtual machine: This project makes use of the Linux-based virtual machine (VM) Vagrant
- Download the data: [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 
- Python3
- Clone this project

### Steps

- Open terminal and locate in vagrant directory
- Run 'vagrant up' to launch VM and run 'vagrant ssh' to log in
- To load the data, 'cd /vagrant' directory and use the command psql -d news -f newsdata.sql.
- To execute the program, run 'python3 newsdb.py' then you will see the results

## Goal

In this project, a large database with a million of rows is explored by building SQL queries to get three conclusions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

## Outputs

What are the most popular three articles of all time?
- Candidate is jerk, alleges rival   	338647 views
- Bears love berries, alleges bear   	253801 views
- Bad things gone, say good people   	170098 views

Who are the most popular article authors of all time?
- Ursula La Multa                    	507594 views
- Rudolf von Treppenwitz             	423457 views
- Anonymous Contributor              	170098 views
- Markoff Chaney                     	 84557 views

On which days did more than 1% of requests lead to errors?
- 2016-07-17                         	  2.26 % errors
