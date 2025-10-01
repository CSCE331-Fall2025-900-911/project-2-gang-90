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


--Total sales over all time
SELECT SUM(total_price) As profit 
From transactions;

--Total number of sales 
SELECT COUNT(*) As total_transations
From transactions;

--Select all transations given customer_name
DECLARE @name AS VARCHAR(100)='Test cutomer'
SELECT * From transactions
WHERE customer_name = @name;

--Bottom 5 popular menu items
SELECT item_name, item_popularity
From menu
ORDER BY item_popularity ASC 
LIMIT 5; 

--Order by porfit of each item
SELECT item_name, price * item_popularity
From menu
ORDER BY item_popularity DESC 


