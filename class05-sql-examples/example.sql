DROP TABLE if exists person;

CREATE TABLE person (
   id INTEGER primary key NOT null,
   name VARCHAR2(20),
   surname VARCHAR2(30),
   age INTEGER
);

DROP TABLE if exists mariage_records;
CREATE TABLE mariage_records (
   id INTEGER primary key NOT null,
   person1_id INTEGER,
   person2_id INTEGER,
   marriage_date DATE
);

insert into person values(1,'John','Smith', 23);
insert into person values(2,'Cindy','Lovegood', 46);
insert into person values(3,'Harry','Potter', 30);
insert into person values(4,'Ginny','Weasley', 29);
insert into person values(5,'Sherlok','Holmes', 60);
insert into person values(6,'John','Watson', 65);

insert into mariage_records values(1, 3, 4, '2013-09-27');
insert into mariage_records values(2, 5, 6, '1994-03-13');

