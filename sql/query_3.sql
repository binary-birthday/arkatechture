SELECT sales.sale_date FROM sales 
INNER JOIN products ON sales.product_id = products.product_id
GROUP BY sales.sale_date
ORDER BY SUM(sales.quantity_sold * products.unit_price) desc LIMIT 1;