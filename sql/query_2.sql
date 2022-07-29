SELECT products.product_name FROM sales 
INNER JOIN products ON sales.product_id = products.product_id
GROUP BY products.product_name
ORDER BY SUM(sales.quantity_sold) ASC LIMIT 1;