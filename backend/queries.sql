--show all cashiers
SELECT employee_id, name, pay
FROM personnel
WHERE role = 'cashier';

--show the average pay by role
SELECT role, AVG(pay) AS average_salary
FROM personnel
GROUP BY role;