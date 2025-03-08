-- Write your PostgreSQL query statement below

SELECT class FROM (SELECT count(student) as Count,class FROM Courses
Group by class
)
WHERE count >=5


