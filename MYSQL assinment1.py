#Assignment –1 

##Creating sample tables and inserting values. 

 

Create the following tables with the given structures and insert sample data as specified: - 
 
A) SALESPEOPLE 

Snum number(4) 

Sname varchar2(10) 

city varchar2(10) 

Comm number(3,2) 

Answer: 

Create table salespeople 

( 

snum number(4), 

sname varchar2(10), 

city varchar2(10), 

comm number(3,2) 

); 

 

B) CUSTOMERS 

Cnum number(4) 

Cname varchar2(10) 

City varchar2(10) 

Rating number(4) 

Snum number(4) 

 

Answer: 

Create table customers 

( 

cnum number(4), 

cname varchar2(10), 

city varchar2(10), 

rating number(4), 

snum number(4) 

); 


C) ORDERS 

Onum number(4) 

Amt number(7,2) 

Odate date 

Cnum number(4) 

Snum number(4) 

Answer: 

Create table orders 

( 

onum number(4), 

amt number(7,2), 

odate date, 

cnum number(4), 

snum number(4) 

); 

 
SALES PEOPLE 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

SNUM 	 	SNAME 	 	CITY 	 		COMM 

1001 	 	Peel 	 	London 	 		.12 

1002 	 	Serres 	 	San Jose 	 	.13 

1004		Motika 	 	London 	 		.11 

1007 	 	Rifkin 	 	Barcelona 	 	.15 

1003 	 	Axelrod 	New York 	 	.10 

 

Insert into salespeople values(&snum,’&name’,’&city’,&comm); 


CUSTOMERS 


CNUM 	 	CNAME 	 		CITY 	 		RATING 	 	SNUM 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

2001		Hoffman 	 	London 	 		100 	 	1001 

2002		Giovanni 	 	Rome 	 		200 	 	1003 

2003 	 	Liu 	 		San Jose 	 	200 	 	1002 

2004 	 	Grass 	 		Berlin 	 		300 	 	1002 

2006 	 	Clemens 	 	London 	 		100 	 	1001 

2008 	 	Cisneros 	 	San Jose 	 	300 	 	1007 

2007 	 	Pereira 	 	Rome 	 		100 	 	1004 



ORDERS 

Insert into customers values(&cnum,’&cname’,’&city’,&rating,&snum); 

ONUM 	 	AMT 	 		ODATE		CNUM SNUM 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

3001 	 	18.69 	 		03- OCT -1990 	 	2008 1007 
3003 	 	767.19 	 		03- OCT -1990 	 	2001 1001 
3002 	 	1900.10 	 	03- OCT -1990 	 	2007 1004 
3005 	 	5160.45 	 	03- OCT -1990 	 	2003 1002 
3006 	 	1098.16 	 	03- OCT -1990 	 	2008 1007 
3009 	 	1713.23 	 	04- OCT -1990 	 	2002 1003 
3007 	 	75.75 	 		04- OCT -1990 	 	2004 1002 
3008 	 	4723.00 	 	05- OCT -1990 	 	2006 1001 
3010 	 	1309.95 	 	06- OCT -1990 	 	2004 1002 
3011 	 	9891.88 	 	06- OCT -1990 	 	2006 1001 


Insert into orders values(&onum,&amt,’&odate’,&cnum,&snum); 

ONUM AMT ODATE CNUM SNUM 

 

INSERT INTO ORDERS 

VALUES(3001,18.69,'03-OCT-1990',2008, 1007); 

 

INSERT INTO ORDERS 

VALUES(3003,767.19,'03- OCT -1990',2001,1001); 

 

INSERT INTO ORDERS 

VALUES(3002,1900.10,'03- OCT -1990',2007,1004); 

 

INSERT INTO ORDERS 

VALUES(3005,5160.45,'03- OCT -1990',2003,1002); 

 

INSERT INTO ORDERS 

VALUES(3006,1098.16,'03- OCT -1990',2008,1007); 

 

INSERT INTO ORDERS 

VALUES(3009,1713.23,’04- OCT -1990’,2002,1003); 

 

INSERT INTO ORDERS 

VALUES(3007,75.75,’04- OCT -1990’,2004,1002); 

 

INSERT INTO ORDERS 

VALUES(3008,4723.00,’05- OCT -1990’,2006,1001); 

 

INSERT INTO ORDERS 

VALUES(3010,309.95,’06-OCT -1990’,2004,1002); 

 

INSERT INTO ORDERS 

VALUES(3011,9891.88,’06- OCT -1990’,2006,1001); 

