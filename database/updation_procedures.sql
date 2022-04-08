-- update student's password
delimiter //
create procedure update_studentpwd(in p_id char(13), in old_pwd varchar(50), in new_pwd varchar(50))
begin
	declare olep varchar(50);
    select password into olep from student where id = p_id;
    if old_pwd != olep then
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'The old password entered does not match the existing password. Please try again.';
	end if;
	start transaction;
		update student
		set password = new_pwd where id = p_id and password = old_pwd;
	commit;
end //
delimiter ;

-- call update_pwd('2020A7PS0141P', 'abhi123', 'abhi456');

-- update correct option for a question
delimiter //
create procedure update_correctoption(in q_qid int, in q_oid int)
begin
	start transaction;
		update correct_option
		set oid = q_oid where qid = q_qid;
    commit;
end //
delimiter ;

-- update option attempted by a student
delimiter //
create procedure update_assign(in s_id char(13), in q_qid int, in q_oid int)
begin
	start transaction;
		update assign
        set attempted_option = q_oid where id = s_id and qid = q_qid;
	commit;
end //
delimiter ;