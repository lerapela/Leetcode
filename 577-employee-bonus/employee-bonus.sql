-- Write your PostgreSQL query statement below
SELECT 
e.name,b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId=b.empId
WHERE coalesce(bonus,0) < 1000;