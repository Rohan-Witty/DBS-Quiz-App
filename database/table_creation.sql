use quiz;

-- drop tables if they exist

drop table if exists correct_option;
drop table if exists assign;
drop table if exists option_choices;
drop table if exists question;
drop table if exists student;

-- create tables

create table student(
	id char(13),
    `name` varchar(100),
    `password` varchar(50),
    primary key (id)
);

create table question(
	qid int auto_increment,
    marks int,
    qstring varchar(1024),
    primary key(qid)
);

create table option_choices(
	oc_id int primary key auto_increment,
    qid int,
	oid int,
    ostring varchar(1024),
	unique qo_pair (qid, oid),
    foreign key (qid) references question(qid)
);

create table assign(
	id char(13),
    qid int,
    attempted_option int,
	primary key (id, qid),
    foreign key (id) references student(id),
    foreign key (qid) references question(qid),
    foreign key (qid, attempted_option) references option_choices(qid, oid)
);

create table correct_option(
	qid int,
    oid int,
    primary key (qid),
    foreign key (qid) references question(qid),
    foreign key (qid, oid) references option_choices(qid, oid)
)