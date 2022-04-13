drop view if exists leaderboard;

create view leaderboard as
select ID, `name`, sum(marks) as total_marks from assign
join correct_option on correct_option.qid = assign.qid and correct_option.oid = assign.attempted_option
natural join student join question on question.qid = correct_option.qid
group by ID order by total_marks desc;
