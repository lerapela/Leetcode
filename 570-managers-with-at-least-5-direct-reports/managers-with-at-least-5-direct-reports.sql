SELECT
    M.name
FROM 
    Employee e
JOIN 
    Employee M ON e.managerId = M.id
GROUP BY 
    M.id, M.name
HAVING 
    COUNT(M.id) >= 5;
