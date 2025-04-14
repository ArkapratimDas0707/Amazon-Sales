-- name: sales_by_category
SELECT 
    p.category,
    SUM(sf."Total Sales") AS revenue,
    SUM(sf.quantity) AS units_sold
FROM sales_fact sf
JOIN products p ON sf."Product ID" = p."Product ID"
GROUP BY p.category
ORDER BY revenue DESC;
