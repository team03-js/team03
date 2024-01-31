create database test;
use test;
#
/*
--------------  Users   ----------------------
/*
--  geo 테이블
*/
create table tbl_geo(
    id bigint auto_increment primary key,
    lat decimal(9,6),
    lng decimal(9,6)
);
/*
--  company 테이블
*/
create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    catchPhrase varchar(255),
    bs varchar(255)
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
    geo_id bigint,
    constraint fk_address_geo foreign key (geo_id) references tbl_geo(id)
);


-- users의 테이블

create table tbl_users(

    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255)not null,
    email varchar(255)not null,
    phone varchar(255)not null,
    website varchar(255)not null,
    address_id bigint,
    company_id bigint,
    constraint fk_users_address foreign key (address_id) references tbl_address(id),
    constraint fk_users_company foreign key (company_id) references tbl_company(id)
);
/*
------
*/

/*
   --------------  Albums   ----------------------
    Albums 테이블
   on delete cascade:
   부모 테이블에서 레코드가 삭제될 경우, 해당 레코드와 관련된 자식 테이블의 레코드도 자동으로 삭제
*/
create table tbl_albums(
    user_id varchar(255) not null,
    id bigint auto_increment primary key,
    title varchar(255) not null,
    constraint fk_albums_user foreign key (user_id)
                    references tbl_users(id)
                    on delete cascade
);

/*
    --------------- posts ---------------------
*/
create table tbl_posts(
    user_id bigint,
    id bigint auto_increment primary key,
    title varchar(255),
    body varchar(255),
    constraint fk_posts_user foreign key (user_id)
                references tbl_users(id)
                on delete cascade);

/*
    --------------- comments --------------------
*/
create table tbl_comments(
    post_id bigint,
    id bigint auto_increment primary key,
    name varchar(255) not null ,
    email varchar(255) not null,
    body varchar(255),
    constraint fk_comments_user foreign key (post_id)
        references tbl_posts(id)
        on delete cascade
);
/*
    --------------- photos ----------------------
*/
create table tbl_photos(
    albums_id bigint,
    id bigint auto_increment primary key,
    title varchar(255),
    url varchar(255),
    thumbnail_url varchar(255),
    constraint fk_photos_albums foreign key (albums_id)
                       references tbl_albums(id)
                       on delete cascade
);

/*
    -------------- todos  -----------------
*/

create table tbl_todos(
    user_id bigint,
    id bigint auto_increment primary key,
    title varchar(255) not null,
    completed boolean,
    constraint fk_todos_user foreign key (user_id)
        references tbl_users(id)
        on delete cascade
);

select * from tbl_albums;
drop table tbl_albums;
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

