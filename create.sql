create table student(
	id char(13),
    `name` varchar(100),
    `password` varchar(50),
    primary key (id)
);

insert into student values ('2020A7PS0081P', 'Rohan Srinivasan', 'rohan123');
insert into student values ('2020A7PS0141P', 'Abhirath Anand', 'abhi123');
insert into student values ('2020A7PS0021P', 'Samriddha Sinha', 'sammy123');
insert into student values ('2020A7B30091P', 'Srijan Shashwat', 'srijan123');
insert into student values ('2020A7PS0013P', 'Kaustab Chaudhary', 'kc123');

create table question(
	qid int auto_increment,
    marks int,
    qstring varchar(1024),
    primary key(qid)
);

-- show full columns from question;

-- drop table question;
-- drop table assign;

-- drop table option_choices;

create table option_choices(
	oid int,
    ostring int,
    qid int,
	primary key (qid, oid),
    foreign key (qid) references question(qid)
);

create table assign(
	id char(13),
    oid int,
    qid int,
    attempted_option int,
	primary key (id, qid),
    foreign key (id) references student(id),
    foreign key (qid) references question(qid),
    foreign key (attempted_option) references option_choices(oid)
);

-- drop table assign;

create table correct_option(
	qid int,
    oid int,
    primary key (qid),
    foreign key (qid) references question(qid),
    foreign key (oid) references option_choices(oid)
)
