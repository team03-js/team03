create database homework;
use homework;

create table post(
    userId varchar(255) not null,
    id bigint auto_increment primary key,
    title varchar(255) not null,
    body varchar(255) not null
);

select * from post;

delete from post where userId = 1000;