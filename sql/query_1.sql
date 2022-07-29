SELECT salespeople.salesperson_name FROM sales 
INNER JOIN salespeople ON sales.salesperson_id = salespeople.salesperson_id
INNER JOIN products ON sales.product_id = products.product_id
WHERE EXTRACT(MONTH FROM sale_date) = 11 
GROUP BY salespeople.salesperson_name
ORDER BY SUM(sales.quantity_sold * products.unit_price) DESC LIMIT 1;