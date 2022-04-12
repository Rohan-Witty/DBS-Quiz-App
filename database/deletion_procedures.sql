drop procedure if exists delete_student;
drop procedure if exists delete_question;
drop procedure if exists delete_options;
drop procedure if exists delete_assign;

-- delete student
delimiter //
create procedure delete_student(in s_id char(13))
begin
	start transaction;
		delete from assign where id = s_id;
        delete from student where id = s_id;
	commit;
end //
delimiter ;

-- delete question
delimiter //
create procedure delete_question(in q_qid int)
begin
	start transaction;
		delete from assign where qid = q_qid;
        delete from correct_option where qid = q_qid;
        delete from option_choices where qid = q_qid;
        delete from question where qid = q_qid;
	commit;
end //
delimiter ;

-- call delete_question(15);

-- delete options for a question
delimiter //
create procedure delete_options(in q_qid int)
begin
	start transaction;
		delete from option_choices where qid = q_qid;
	commit;
end //
delimiter ;

-- delete assigned questions for a given student
delimiter //
create procedure delete_assign(in s_id char(13))
begin
	start transaction;
		delete from assign where id = s_id;
	commit;
end //
delimiter ;
