drop view if exists leaderboard;
create view leaderboard as 
select ID, `name`, sum(marks) as total_marks from assign
join correct_option on
correct_option.qid = assign.qid and correct_option.oid = assign.attempted_option
natural join student join question on question.qid = correct_option.qid
group by ID order by total_marks desc;

drop view if exists assignedquestions;
create view AssignedQuestions as
select student.id ID, student.name Name, question.qid QID, question.qstring QSTRING, assign.attempted_option ATTEMPTED, correct_option.oid CORRECT, option_choices.oid OID, option_choices.ostring ostring from question join option_choices on question.qid = option_choices.qid join correct_option on question.qid = correct_option.qid 
join assign on question.qid = assign.qid join student on student.id = assign.id where name like 'Roh%';