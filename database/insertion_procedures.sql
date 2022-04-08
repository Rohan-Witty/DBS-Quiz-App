-- drop procedure if exists insert_studentinfo;

-- insert values into student table
delimiter //
create procedure insert_studentinfo(in s_id char(13), in s_name varchar(100), in s_pwd varchar(50))
begin
	start transaction;
		insert into student(id, name, password) values (s_id, s_name, s_pwd);
	commit;
end //
delimiter ;

-- insert values into question table
delimiter //
create procedure insert_questioninfo(in q_qid int, in q_marks int, in q_qstring varchar(1024))
begin
	start transaction;
		insert into question(q_qid, q_marks, q_qstring) values (qid, marks, qstring);
	commit;
end //
delimiter ;

-- insert option for questions
delimiter //
create procedure insert_questionoptions(in q_qid int, in q_oid int, in ostring varchar(1024))
begin
	start transaction;
		insert into option_choices(q_qid, q_oid, ostring) values (qid, marks, qstring);
	commit;
end //
delimiter ;

-- insert correct option for question
delimiter //
create procedure insert_correctoption(in q_qid int, in q_oid int)
begin
	start transaction;
		insert into correct_option(q_qid, q_oid) values (qid, oid);
	commit;
end //
delimiter ;

-- assign questions to students
delimiter //
create procedure insert_assign(in s_id char(13), in q_qid int)
begin
	start transaction;
		insert into assign(s_id, q_qid) values (id, qid);
	commit;
end //
delimiter ;

-- delete from student where id like '%78P';

-- call insert_studentinfo('2020A7PS078P', 'Shashank Shreedhar Bhatt', 'ssb123');
