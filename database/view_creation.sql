drop view if exists leaderboard;

create view leaderboard as
select student.id as ID, `name`, coalesce(sum(marks), 0) as total_marks from assign
left join correct_option on correct_option.qid = assign.qid and correct_option.oid = assign.attempted_option
natural join student left join question on question.qid = correct_option.qid
group by ID order by total_marks desc;
