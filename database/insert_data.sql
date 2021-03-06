-- insert into student

delete from assign where true;
delete from correct_option where true;
delete from option_choices where true;
delete from question where true;

-- insert into question
call insert_questioninfo(1, 3, 'q1');
call insert_questioninfo(2, 3, 'q2');
call insert_questioninfo(3, 3, 'q3');
call insert_questioninfo(4, 3, 'q4');
call insert_questioninfo(5, 3, 'q5');
call insert_questioninfo(6, 3, 'q6');
call insert_questioninfo(7, 3, 'q7');
call insert_questioninfo(8, 3, 'q8');
call insert_questioninfo(9, 3, 'q9');
call insert_questioninfo(10, 3, 'q10');
call insert_questioninfo(11, 3, 'q11');
call insert_questioninfo(12, 3, 'q12');
call insert_questioninfo(13, 3, 'q13');
call insert_questioninfo(14, 3, 'q14');
call insert_questioninfo(15, 3, 'q15');
call insert_questioninfo(16, 3, 'q16');
call insert_questioninfo(17, 3, 'q17');
call insert_questioninfo(18, 3, 'q18');
call insert_questioninfo(19, 3, 'q19');
call insert_questioninfo(20, 3, 'q20');

-- insert into option_choices
call insert_questionoptions(1, 1, 'o1');
call insert_questionoptions(1, 2, 'o2');
call insert_questionoptions(1, 3, 'o3');
call insert_questionoptions(1, 4, 'o4');
call insert_questionoptions(2, 1, 'o1');
call insert_questionoptions(2, 2, 'o2');
call insert_questionoptions(2, 3, 'o3');
call insert_questionoptions(2, 4, 'o4');
call insert_questionoptions(3, 1, 'o1');
call insert_questionoptions(3, 2, 'o2');
call insert_questionoptions(3, 3, 'o3');
call insert_questionoptions(3, 4, 'o4');
call insert_questionoptions(4, 1, 'o1');
call insert_questionoptions(4, 2, 'o2');
call insert_questionoptions(4, 3, 'o3');
call insert_questionoptions(4, 4, 'o4');
call insert_questionoptions(5, 1, 'o1');
call insert_questionoptions(5, 2, 'o2');
call insert_questionoptions(5, 3, 'o3');
call insert_questionoptions(5, 4, 'o4');
call insert_questionoptions(6, 1, 'o1');
call insert_questionoptions(6, 2, 'o2');
call insert_questionoptions(6, 3, 'o3');
call insert_questionoptions(6, 4, 'o4');
call insert_questionoptions(7, 1, 'o1');
call insert_questionoptions(7, 2, 'o2');
call insert_questionoptions(7, 3, 'o3');
call insert_questionoptions(7, 4, 'o4');
call insert_questionoptions(8, 1, 'o1');
call insert_questionoptions(8, 2, 'o2');
call insert_questionoptions(8, 3, 'o3');
call insert_questionoptions(8, 4, 'o4');
call insert_questionoptions(9, 1, 'o1');
call insert_questionoptions(9, 2, 'o2');
call insert_questionoptions(9, 3, 'o3');
call insert_questionoptions(9, 4, 'o4');
call insert_questionoptions(10, 1, 'o1');
call insert_questionoptions(10, 2, 'o2');
call insert_questionoptions(10, 3, 'o3');
call insert_questionoptions(10, 4, 'o4');
call insert_questionoptions(11, 1, 'o1');
call insert_questionoptions(11, 2, 'o2');
call insert_questionoptions(11, 3, 'o3');
call insert_questionoptions(11, 4, 'o4');
call insert_questionoptions(12, 1, 'o1');
call insert_questionoptions(12, 2, 'o2');
call insert_questionoptions(12, 3, 'o3');
call insert_questionoptions(12, 4, 'o4');
call insert_questionoptions(13, 1, 'o1');
call insert_questionoptions(13, 2, 'o2');
call insert_questionoptions(13, 3, 'o3');
call insert_questionoptions(13, 4, 'o4');
call insert_questionoptions(14, 1, 'o1');
call insert_questionoptions(14, 2, 'o2');
call insert_questionoptions(14, 3, 'o3');
call insert_questionoptions(14, 4, 'o4');
call insert_questionoptions(15, 1, 'o1');
call insert_questionoptions(15, 2, 'o2');
call insert_questionoptions(15, 3, 'o3');
call insert_questionoptions(15, 4, 'o4');
call insert_questionoptions(16, 1, 'o1');
call insert_questionoptions(16, 2, 'o2');
call insert_questionoptions(16, 3, 'o3');
call insert_questionoptions(16, 4, 'o4');
call insert_questionoptions(17, 1, 'o1');
call insert_questionoptions(17, 2, 'o2');
call insert_questionoptions(17, 3, 'o3');
call insert_questionoptions(17, 4, 'o4');
call insert_questionoptions(18, 1, 'o1');
call insert_questionoptions(18, 2, 'o2');
call insert_questionoptions(18, 3, 'o3');
call insert_questionoptions(18, 4, 'o4');
call insert_questionoptions(19, 1, 'o1');
call insert_questionoptions(19, 2, 'o2');
call insert_questionoptions(19, 3, 'o3');
call insert_questionoptions(19, 4, 'o4');
call insert_questionoptions(20, 1, 'o1');
call insert_questionoptions(20, 2, 'o2');
call insert_questionoptions(20, 3, 'o3');
call insert_questionoptions(20, 4, 'o4');

-- insert into correct_options
call insert_correctoption(1, 1);
call insert_correctoption(2, 2);
call insert_correctoption(3, 3);
call insert_correctoption(4, 4);
call insert_correctoption(5, 1);
call insert_correctoption(6, 2);
call insert_correctoption(7, 3);
call insert_correctoption(8, 4);
call insert_correctoption(9, 1);
call insert_correctoption(10, 2);
call insert_correctoption(11, 3);
call insert_correctoption(12, 4);
call insert_correctoption(13, 1);
call insert_correctoption(14, 2);
call insert_correctoption(15, 3);
call insert_correctoption(16, 4);
call insert_correctoption(17, 1);
call insert_correctoption(18, 2);
call insert_correctoption(19, 3);
call insert_correctoption(20, 4);