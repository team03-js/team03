# /*
# --------------  Albums   ----------------------
#
#     Albums 테이블
# */
create table tbl_albums(
    userId varchar(255) not null,
    id bigint auto_increment primary key,
    title varchar(255) not null
);

select * from tbl_albums;
drop table tbl_albums;

