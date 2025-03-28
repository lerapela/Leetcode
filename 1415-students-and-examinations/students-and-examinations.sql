-- Write your PostgreSQL query statement below
SELECT 
S.student_id,
S.student_name,
SB.subject_name,
COALESCE(COUNT(E.subject_name), 0) AS attended_exams
FROM Students S
CROSS JOIN Subjects SB 
LEFT JOIN Examinations E ON S.student_id = E.student_id AND SB.subject_name = E.subject_name
GROUP BY S.student_id,S.student_name,SB.subject_name
ORDER BY S.student_id ASC;


