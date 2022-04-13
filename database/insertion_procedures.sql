drop procedure if exists insert_studentinfo;
drop procedure if exists insert_questioninfo;
drop procedure if exists insert_questionoptions;
drop procedure if exists insert_correctoption;
drop procedure if exists insert_assign;

-- insert values into student table
delimiter //
create procedure insert_studentinfo(in s_id char(13), in s_name varchar(100))
begin
	start transaction;
		insert into student(id, name) values (s_id, s_name);
	commit;
end //
delimiter ;

-- insert values into question table
delimiter //
create procedure insert_questioninfo(in q_qid int, in q_marks int, in q_qstring varchar(1024))
begin
	start transaction;
		insert into question(qid, marks, qstring) values (q_qid, q_marks, q_qstring);
	commit;
end //
delimiter ;

-- insert option for questions
delimiter //
create procedure insert_questionoptions(in q_qid int, in q_oid int, in ostring varchar(1024))
begin
	start transaction;
		insert into option_choices(qid, oid, ostring) values (q_qid, q_oid, ostring);
	commit;
end //
delimiter ;

-- insert correct option for question
delimiter //
create procedure insert_correctoption(in q_qid int, in q_oid int)
begin
	start transaction;
		insert into correct_option(qid, oid) values (q_qid, q_oid);
	commit;
end //
delimiter ;

-- assign questions to students
delimiter //
create procedure insert_assign(in s_id char(13), in q_qid int)
begin
	start transaction;
		insert into assign(id, qid) values (s_id, q_qid);
	commit;
end //
delimiter ;
