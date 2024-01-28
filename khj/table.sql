use test;
create database test;

/*
album
------------
id(pk)
------------
user id (nn)
title (nn)
completd (nn)
*/
create table tbl_todos(
    id bigint auto_increment primary key,
    userId int not null,
    title varchar(255) not null,
    completed boolean not null
);

select * from tbl_todos;
/*---------------------------------------------------------------------------------*/
create table tbl_users(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255)not null,
    email varchar(255)not null,
    phone varchar(255)not null,
    website varchar(255)not null
);

create table tbl_address (
    id bigint auto_increment primary key,
    street varchar(255) not null,
    suite varchar(255) not null,
    city varchar(255) not null,
    zipcode varchar(255) not null,
    users_id bigint not null,
    constraint fk_address_user foreign key (users_id)
    references tbl_users(id)
);

create table tbl_geo(
    id bigint auto_increment primary key,
    lat decimal(9,6) not null,
    lng decimal(9,6) not null,
    address_id bigint not null,
    constraint fk_geo_address foreign key (address_id)
    references  tbl_address(id)
);


create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    catchPhrase varchar(255),
    bs varchar(255),
    users_id bigint not null,
    constraint fk_company_users foreign key (users_id)
    references tbl_users(id)
);

select * from tbl_users;
select * from tbl_address;
select * from tbl_geo;
select * from tbl_company;