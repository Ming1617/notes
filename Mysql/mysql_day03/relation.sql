create table teacher(
id int primary key,
tname varchar(20),
level varchar(20)
)charset=utf8;
insert into teacher values(1,'郭小闹','牛X'),(2,'魏哥哥','牛XX');

create table course(
id int primary key,
cname varchar(20)
)charset=utf8;
insert into course values(1,'Django'),(2,'Mysql'),(3,'Project');