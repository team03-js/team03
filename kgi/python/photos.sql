create table tbl_photos(
    id bigint auto_increment primary key,
    albumId bigint not null,
    title varchar(255) not null,
    url varchar(255) not null,
    thumbnailUrl varchar(255) not null
);

drop table tbl_photos;
select * from tbl_photos;