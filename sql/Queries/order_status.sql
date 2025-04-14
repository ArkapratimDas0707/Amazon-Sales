-- name: order_status_summary
SELECT 
    Status,
    COUNT(*) AS num_orders,
    ROUND(SUM("Total Sales"), 2) AS total_sales
FROM sales_fact
GROUP BY Status
ORDER BY num_orders DESC;
