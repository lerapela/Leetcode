-- Write your PostgreSQL query statement below
WITH TopSalaries AS (
    SELECT departmentId, salary
    FROM Employee
    GROUP BY departmentId, salary
    HAVING salary IN (
        SELECT DISTINCT salary
        FROM Employee e
        WHERE e.departmentId = Employee.departmentId
        ORDER BY salary DESC
        LIMIT 3
    )
)
SELECT d.name AS Department, e.name AS Employee, e.salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
JOIN TopSalaries ts ON e.departmentId = ts.departmentId AND e.salary = ts.salary
ORDER BY d.name, e.salary DESC;




