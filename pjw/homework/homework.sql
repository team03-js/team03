create database homework;
use homework;

create table tbl_posts(
    userId varchar(255) not null,
    id bigint auto_increment primary key,
    title varchar(255) not null,
    body varchar(255) not null
);
#
# create table tbl_comments(
#     postId varchar(255) not null,
#     id bigint auto_increment primary key,
#     name varchar(255) not null,
#     email varchar(255) not null,
#     body varchar(255) not null
# );
#
# create table tbl_albums(
#     userId varchar(255) not null,
#     id bigint auto_increment primary key,
#     title varchar(255) not null
# );
#
# create table tbl_photos(
#     albumId varchar(255) not null,
#     id bigint auto_increment primary key,
#     title varchar(255) not null,
#     url varchar(255) not null,
#     thumbnailUrl varchar(255) not null
# );
#
# create table tbl_todos(
#     userId varchar(255) not null,
#     id bigint auto_increment primary key,
#     title varchar(255) not null,
#     completed varchar(255) not null
# );

select * from tbl_posts;
# select * from tbl_comments;
# select * from tbl_albums;
# select * from tbl_photos;
# select * from tbl_todos;



