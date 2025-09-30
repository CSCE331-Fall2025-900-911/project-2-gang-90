--show all cashiers
SELECT employee_id, name, pay
FROM personnel
WHERE role = 'cashier';

--show the average pay by role
SELECT role, AVG(pay) AS average_salary
FROM personnel
GROUP BY role;

--show menu items that cost less than $4.99
SELECT item_name, price
FROM menu
WHERE price < 4.99;

--Top 5 most popular menu items
SELECT item_name, item_popularity
FROM menu
ORDER BY item_popularity DESC
LIMIT 5;

--Average price of all menu items
SELECT AVG(price) AS average_item_price
FROM menu;