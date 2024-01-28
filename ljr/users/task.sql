# create database test;
# use test;
#
/*
--------------  Users   ----------------------

-- users의 테이블
*/
create table tbl_users(

    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255)not null,
    email varchar(255)not null,
    phone varchar(255)not null,
    website varchar(255)not null
);
/*
--  address 테이블
*/
create table tbl_address (
    id bigint auto_increment primary key,
    street varchar(255) not null,
    suite varchar(255) not null,
    city varchar(255) not null,
    zipcode varchar(255),
    user_id bigint,
    constraint fk_address_user foreign key (user_id) references tbl_users(id)
);

/*
--  geo 테이블
*/
create table tbl_geo(
    id bigint auto_increment primary key,
    lat decimal(9,6),
    lng decimal(9,6),
    address_id bigint,
    constraint fk_geo_address foreign key (address_id) references  tbl_address(id)
);
/*
--  company 테이블
*/
create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    catchPhrase varchar(255),
    bs varchar(255),
    user_id bigint,
    constraint fk_company_user foreign key (user_id)
                        references tbl_users(id)
);

#
#
# select * from tbl_users;
# select * from tbl_address;
# select * from tbl_geo;
# select * from tbl_company;
#
#
# drop table tbl_address;
# drop table tbl_geo;
# drop table tbl_company;

